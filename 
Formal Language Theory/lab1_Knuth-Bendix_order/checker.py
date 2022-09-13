from parser import Parser
from rule import Rule
from copy import deepcopy
from cyclic import is_cyclic

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
        # if not R:
        self.buffer.append(
            f'"Order:{nl}{nl.join(map(lambda x: f"{x[0]} > {x[1]}", [x for x in O]))} {nl} Rules:{nl}{nl.join(map(str, [x for x in R]))}"')

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
        # print('KB1', rule)
        oldo, oldr = deepcopy(oldo), deepcopy(oldr)
        O, R = deepcopy(O), deepcopy(R)

        if rule.right.string_representation() in rule.left.string_representation():
            self.write_kb_to_graph(f'KB1 drop {rule}', oldo, oldr, O, R)
            self.check_state(O, R)
            return True
        
    def check_kb_2(self, rule, O, R, oldo, oldr):
        # print('KB2', rule)
        oldo, oldr = deepcopy(oldo), deepcopy(oldr)
        O, R = deepcopy(O), deepcopy(R)


        left, right = rule.left, rule.right
        if left.type == right.type == 'constructor':
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
        # print('KB3', rule)

        left, right = rule.left, rule.right
        if right.name == left.name or left.type != 'constructor' or right.type != 'constructor':
            return

        oldo, oldr = deepcopy(oldo), deepcopy(oldr)
        O, R = deepcopy(O), deepcopy(R)

        if left.name == right.name:
            return
        O.add((left.name, right.name))

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
        # print('KB4', rule)
        left, right = rule.left, rule.right
        if right.name != left.name or left.type != 'constructor' or right.type != 'constructor':
            return

        oldo, oldr = deepcopy(oldo), deepcopy(oldr)
        O, R = deepcopy(O), deepcopy(R)

        new_rules = set()
        for right_subterm in right.content:
            R.add(Rule(left, right_subterm))

        for l, r in list(zip(left.content, right.content))[::self.order_param]:
            if l != r:
                R.add(Rule(l, r))
                new_rules = R.difference(oldr)
                self.write_kb_to_graph(
                    {f'KB4 new:{nl}({nl.join(list(map(str, new_rules)))})'}, oldo, oldr, O, R)
                self.check_state(O=O, R=R)
                return

    def chech_cycles(self, O):
        O = deepcopy(O)        
        g = {}
        while(O):
            s, d = O.pop()
            if s in g:
                g[s].append(d)
            else:
                g[s] = [d]
        return is_cyclic(g)

    def start_checking(self):
        print(f'Rules:{nl}{nl.join(map(lambda x: str(x), self.rules))}{nl}')

        self.buffer.append(f'"START"')
        self.write_arrow_to_graph()
        self.write_state_to_graph(O=set(), R=self.rules)
        self.write_label_to_graph('go')

        try:
            self.check_state(O=set(), R=self.rules)
        except Decision:
            pass
        else:
            with open('result.txt', 'w') as res_file:
                for rule in self.rules:
                    res_file.write(f'{rule}{nl}')
                res_file.write('\n')
                res_file.write('Не получилось :(')
            print('Не удалось построить порядок')
        finally:
            self.buffer.append('}')
            with open('graph.dot', 'w') as g:
                for x in self.buffer:
                    g.write(x)

                # return self.buffer

    def check_state(self, O: set, R: set):
        """Принимает на вход состояние решателя:
        O(order) - множество отношений порядка между конструкторами,
        напр. ('f', 'g') - значит, что f >lg g

        R(rules) - множество правил переписывания, которые надо проверить
        ***видимо, R - это trs*** -______-

        Смысл этой функции:
        - проверить алгорим на окончание
        - отфильтровать тривиальные правила переписывания
        - проверить частичный порядок на наличие циклов
        - обнаружить очевидное невыполнение очередного правила
        - при отсутствии проблем предположить, что очередное правило выполняется
        и продить ветвление решателя
        """
        O, R = deepcopy(O), deepcopy(R)

        # Если в R есть идентичное правило переписывания, то такое сразу отвергаем
        if any(filter(lambda rule: rule.left == rule.right, R)):
            return

        # если R пусто, то мы проверили все правила и не получили противоречий урааа!
        if len(R) == 0:
            with open('result.txt', 'w') as res_file:
                for rule in self.rules:
                    res_file.write(f'{rule}{nl}')
                res_file.write('\n')
                print('***********************')
                print('Вроде, получилось:')
                res_file.write('Вроде, получилось:\n')
                for order in O:
                    print(f'    lg: {order[0]} > {order[1]}')
                    res_file.write(f'    lg: {order[0]} > {order[1]}{nl}')
                print('***********************')
                raise Decision # прекращаем поиск решения, сбрасываем стек вызова до start_checking()
                return

        O = set(filter(lambda ord: ord[0] != ord[1], O))
        if self.chech_cycles(O):
            return 

        # берем какое-нибудь правило переписывания
        rule = R.pop()
        oldo, oldr = O, R
        O, R = deepcopy(O), deepcopy(R)
        oldr.add(rule)

        # проверим это правило на тупость - ведь chech_kb_2 создает новые правила
        # тут будут отброшены правила типа x ::= f(x) или еще хуже
        if rule.left.string_representation() in rule.right.string_representation():
            # print(f'Found stupid rule: {rule}')
            return

        # КБ1 отсекает правила типа f(x) ::= x
        # которые ломают остальные КБ
        if self.check_kb_1(rule=rule, O=O, R=R, oldo=oldo, oldr=oldr):
            pass
        else:
            self.check_kb_2(rule=rule, O=O, R=R, oldo=oldo, oldr=oldr)
            self.check_kb_4(rule=rule, O=O, R=R, oldo=oldo, oldr=oldr)
            self.check_kb_3(rule=rule, O=O, R=R, oldo=oldo, oldr=oldr)