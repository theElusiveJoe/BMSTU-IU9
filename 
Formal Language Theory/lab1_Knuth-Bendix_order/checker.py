from parser import Parser
from rule import Rule
from copy import deepcopy

nl = '\n'


class Decision(Exception):
    pass


class Checker():
    def __init__(self, p: Parser):
        self.variables = set(p.variables)
        self.constructors = set(p.constructors)
        self.order_param = (p.order_param == 'lexicographic') * \
            1 + (p.order_param == 'anti-lexicographic')*(-1)
        self.rules = set(p.rules)
        self.buffer = ['digraph G { node [shape = box]\n']

    def write_arrow_to_graph(self):
        self.buffer.append(' -> ')

    def write_state_to_graph(self, O, R):
        R, O = deepcopy(R), deepcopy(O)
        R, O = sorted(list(map(str, list(R)))), sorted(list(O))
        print('WRITEEEE', R, O)
        # if not R:
        self.buffer.append(
            f'"Order=[{nl}{nl.join(map(lambda x: f"{x[0]} > {x[1]}", [x for x in O]))}] {nl} Rules=[{nl}{nl.join(map(str, [x for x in R]))}]"')

    def write_label_to_graph(self, label):
        self.buffer.append(f'[label = {label}];' + '\n')

    def write_kb_to_graph(self, label, oldo, oldr, O, R):
        if not R:
            self.buffer.append('node [color = lightgreen, style = filled];')
        self.write_state_to_graph(oldo, oldr)
        self.write_arrow_to_graph()
        self.write_state_to_graph(O, R)
        # if not R:
        # self.buffer.append(f'[label = "label" fontcolor = green ];')
        # else:
        self.write_label_to_graph(f'"{label}"')

    def check_kb_1(self, rule, O, R, oldo, oldr):
        # я могу так сделать, т.к. отбросил тождественные правила переписывания
        # значит, если правый терм является подстрокой левого терма, то он является его аргументом,
        # или аргументом его аргумента, или ...
        #
        # пометочка для себя:
        # Получается довольно удобно, например можно сразу сказать, что :
        # f(x) >lg x
        # f(h(x)) >lg x
        # и так далее

        print('call kb1')
        oldo, oldr = deepcopy(oldo), deepcopy(oldr)
        O, R = deepcopy(O), deepcopy(R)

        if rule.right.string_representation() in rule.left.string_representation():
            self.write_kb_to_graph(f'KB1 drop {rule}', oldo, oldr, O, R)
            self.check_state(O, R)
            return True

    def check_kb_2(self, rule, O, R, oldo, oldr):
        print('KB2', O.difference(oldo), set(map(str, R.difference(oldr))))
        print('call kb2')
        oldo, oldr = deepcopy(oldo), deepcopy(oldr)
        O, R = deepcopy(O), deepcopy(R)

        left, right = rule.left, rule.right
        if left.type == 'var':
            print('XZ')
            raise Exception(
                'Я не знаю, как применять правило 2, если в левой части стоит переменная, а в правой части её нет')

        new_rules = ''
        for left_subterm in left.content:
            new_R = deepcopy(R)
            new_rules += ' ' + str(Rule(left_subterm, right))
            new_R.add(Rule(left_subterm, right))
            self.write_kb_to_graph(
                f'KB2 suppose {new_rules}', oldo, oldr, O, new_R)
            self.check_state(O=O, R=new_R)

    def check_kb_3(self, rule, O, R, oldo, oldr):
        """
        КБ3 вызывается только, если:
            1. в обеих частях правила стоят конструкторы
            2. имена этих конструкторов не совпадают
        """
        print('call kb3')
        left, right = rule.left, rule.right
        if right.name == left.name or left.type != 'constructor' or right.type != 'constructor':
            return

        oldo, oldr = deepcopy(oldo), deepcopy(oldr)
        O, R = deepcopy(O), deepcopy(R)

        if left.name == right.name:
            return
        O.add((left.name, right.name))

        print(left, right)
        for right_subterm in right.content:
            R.add(Rule(left, right_subterm))
        self.write_kb_to_graph(
            f'KB3 suppose {nl}{left.name} > {right.name}', oldo, oldr, O, R)
        self.check_state(O=O, R=R)

    def check_kb_4(self, rule, O, R, oldo, oldr):
        """
        КБ4 вызывается только, если:
            1. в обеих частях правила стоят конструкторы
            2. имена этих конструкторов совпадают
        """

        print('call kb4', rule)
        left, right = rule.left, rule.right
        if right.name != left.name or left.type != 'constructor' or right.type != 'constructor':
            return

        print('use kb4')
        oldo, oldr = deepcopy(oldo), deepcopy(oldr)
        O, R = deepcopy(O), deepcopy(R)

        new_rules = set()
        for right_subterm in right.content:
            print('adding', left, '>', right_subterm)
            R.add(Rule(left, right_subterm))

        print(R)

        for l, r in list(zip(left.content, right.content))[::self.order_param]:
            print('comparing', left, '&', right_subterm)
            if l != r:
                print(l, r)
                R.add(Rule(l, r))
                new_rules = R.difference(oldr)
                self.write_kb_to_graph(
                    {f'KB4 new:{nl}({nl.join(list(map(str, new_rules)))})'}, oldo, oldr, O, R)
                self.check_state(O=O, R=R)
                return

        print('faild use kb4')

    def simplify_and_check_o(self, O):
        O = deepcopy(O)
        print(len(O))
        O = set(filter(lambda x: x[0] != x[1], O))

        if len(O) == 0:
            return O, True

        first_pair = O.pop()
        reds = set(first_pair)
        while O:
            dest = O.pop()
            if dest in reds:
                return O, False
            reds.add(dest)

        return O, True

    def start_checking(self):
        for x in self.rules:
            print(x)

        self.buffer.append(f'"START"')
        self.write_arrow_to_graph()
        self.write_state_to_graph(O=set(), R=self.rules)
        self.write_label_to_graph('go')

        try:
            self.check_state(O=set(), R=self.rules)
            pass
        except Decision:
            pass
        except Exception as e:
            print(e)
        else:
            print('Не удалось построить порядок')
        finally:
            self.buffer.append('}')
            with open('graph.dot', 'w') as g:
                for x in self.buffer:
                    print(x)
                    g.write(x)

                # return self.buffer

    def check_state(self, O: set, R: set):
        """Принимает на вход состояние решателя:
        O(order) - множество отношений порядка между конструкторами,
        напр. ('f', 'g') - значит, что f >lg g

        R(rules) - множество правил переписывания, которые надо проверить

        Смысл этой функции:
        - проверить алгорим на окончание
        - отфильтровать тривиальные правила переписывания
        - проверить частичный порядок на наличие циклов
        - обнаружить очевидное невыполнение очередного правила
        - при отсутствии проблем предположить, что очередное правило выполняется
        и продить ветвление решателя
        """

        O, R = deepcopy(O), deepcopy(R)
        print('\nChecking new state')
        print(f'R:{R}, O:{O}')
        print('R:')
        for x in R:
            print('    ', x)

        # профильтруем на тривиальные правила переписывания - ведь chech_kb_2 создает новые правила
        print('filter:   ', R, end='')
        if R:
            R = set(filter(lambda rule: rule.left.string_representation()
                    != rule.right.string_representation(), R))
        print('     ', R)

        # если R пусто, то мы проверили все правила и не получили противоречий урааа!
        if len(R) == 0:
            print('Вроде, получилось:')
            for order in O:
                print(f'    lg: {order[0]} > {order[1]}')
            raise Decision
            return

        # O, result = self.simplify_and_check_o(O)
        # if not result:
        #     return

        # берем какое-нибудь правило переписывания

        rule = R.pop()
        oldo, oldr = O, R
        O, R = deepcopy(O), deepcopy(R)
        oldr.add(rule)
        # проверим это правило на тупость - ведь chech_kb_2 создает новые правила
        # тут будут отброшены правила типа x ::= f(x) или еще хуже

        if rule.left.string_representation() in rule.right.string_representation():
            print(f'Found stupid rule: {rule}')
            return

        print('\nbefore KBS:')
        print(oldo, O)
        print(oldr, R)

        # КБ1 отсекает правила типа f(x) ::= x
        # которые ломают остальные КБ
        if self.check_kb_1(rule=rule, O=O, R=R, oldo=oldo, oldr=oldr):
            pass
        else:
            self.check_kb_2(rule=rule, O=O, R=R, oldo=oldo, oldr=oldr)
            self.check_kb_4(rule=rule, O=O, R=R, oldo=oldo, oldr=oldr)
            self.check_kb_3(rule=rule, O=O, R=R, oldo=oldo, oldr=oldr)

        print('CHECK STATE ENDED')
