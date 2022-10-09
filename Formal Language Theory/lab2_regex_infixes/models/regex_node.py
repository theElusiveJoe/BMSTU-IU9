from copy import deepcopy


class Regex_node():
    def __init__(self, children_list):
        self.children_list = children_list

    def get_graph_edges(self):
        edges = []
        for child in self.children_list:
            edges.extend(child.get_graph_edges())
            edges.append(
                {
                    'parent': str(id(self)),
                    'parent_label': str(self),
                    'child': str(id(child)),
                    'child_label': str(child),
                    'label': ''
                }
            )

        return edges


class Alternative_node(Regex_node):
    def __init__(self, children_list):
        Regex_node.__init__(self, children_list)

        self.children_list = list(filter(
            lambda x: type(x).__name__ != 'Null_node',
            self.children_list
        ))

        if len(self.children_list) > 2:
            self.children_list = [self.children_list[0],
                                  Alternative_node(self.children_list[1:])]
        

    def __str__(self):
        return '﴾' + '|'.join(map(str, self.children_list)) + '﴿'

    def __repr__(self):
        return str(self)

    def nodes_str(self):
        return ', '.join(map(str, self.children_list))

    def simplify(self):
        # упрощаем дочерние узлы
        for i in range(len(self.children_list)):
            self.children_list[i] = self.children_list[i].simplify()

        # print('*********\nальтернатива:\n', self.nodes_str())

        while(any(map(lambda x: type(x).__name__ == type(self).__name__, self.children_list))):
            for i in range(len(self.children_list)):
                if type(self.children_list[i]).__name__ == type(self).__name__:
                    self.children_list.extend(
                        self.children_list[i].children_list)
                    self.children_list.pop(i)

        # если все альтернативы - null, то результат - тоже null
        if all(map(lambda x: type(x).__name__ == 'Null_node', self.children_list)):
            return Null_node()

        # выкидываем null
        self.children_list = list(filter(
            lambda x: type(x).__name__ != 'Null_node',
            self.children_list
        ))

        # уникализруем
        self.children_list = list(set(self.children_list))

        # если остался только один лемент
        if len(self.children_list) == 1:
            return self.children_list[0]

        # упорядочиваем
        self.children_list.sort(key=str)

        # соблюдаем древовидную структуру
        if len(self.children_list) > 2:
            self.children_list = [self.children_list[0],
                                  Alternative_node(self.children_list[1:])]
        return self

    def __eq__(self, o):
        return type(self).__name__ == type(o).__name__ and set(self.children_list) == set(o.children_list)

    def __hash__(self):
        return len(str(self))

    def derivative(self, s):
        new_children = []
        for i in range(len(self.children_list)):
            new_children.append(self.children_list[i].derivative(s))
        return Alternative_node(new_children)

    def delta(self):
        new_children = []
        for i in range(len(self.children_list)):
            new_children.append(self.children_list[i].delta())
        return Alternative_node(new_children)

    def reverse(self):
        # print('reverse', self)
        rev = deepcopy(self)
        for i in range(len(rev.children_list)):
            rev.children_list[i] = rev.children_list[i].reverse()
        rev.children_list.sort(key=str)
        return rev


class Concat_node(Regex_node):
    def __init__(self, children_list):
        Regex_node.__init__(self, children_list)
        if len(self.children_list) > 2:
            self.children_list = [self.children_list[0],
                                  Concat_node(self.children_list[1:])]

        if any(map(lambda x: type(x).__name__ == 'Null_node', self.children_list)):
            # print(' В конкатенации найден null!!!')
            self = Null_node()

    def nodes_str(self):
        return ', '.join(map(str, self.children_list))

    def __str__(self):
        return ''.join(map(str, self.children_list))

    def __repr__(self):
        return str(self)

    def simplify(self):
        # упрощаем дочерние узлы
        for i in range(len(self.children_list)):
            self.children_list[i] = self.children_list[i].simplify()

        # если в списке конкатенантов есть null, то вся конкатенация - null
        if any(map(lambda x: type(x).__name__ == 'Null_node', self.children_list)):
            # print(' В конкатенации найден null!!!')
            return Null_node()

        # если все конкатенаты - пустые строки, то результат конкатенации - пустая строка
        if all(map(lambda x: type(x).__name__ == 'Symbol_node' and x.symbol == '', self.children_list)):
            # print(' тут все пустое')
            return Symbol_node('')

        # если есть хотя бы одна непустая строка, то выбрасываем все пустые
        self.children_list = list(filter(lambda x: type(
            x).__name__ != 'Symbol_node' or x.symbol != '', self.children_list))

        # если остался один
        if len(self.children_list) == 1:
            return self.children_list[0]

        if len(self.children_list) > 2:
            self.children_list = [self.children_list[0],
                                  Concat_node(self.children_list[1:])]

        # if type(self.children_list[0]).__name__ == 'Alternative_node':
        #     return Alternative_node([
        #         deepcopy(Concat_node([self.children_list[0].children_list[0], self.children_list[1]]).simplify()),
        #         deepcopy(Concat_node([self.children_list[0].children_list[1], self.children_list[1]]).simplify()),
        #     ]).simplify()
        
        # if type(self.children_list[1]).__name__ == 'Alternative_node':
        #     return Alternative_node([
        #         deepcopy(Concat_node([self.children_list[0], self.children_list[1].children_list[0]]).simplify()),
        #         deepcopy(Concat_node([self.children_list[0], self.children_list[1].children_list[1]]).simplify()),
        #     ]).simplify()

        return self

    def __eq__(self, o):
        return type(self).__name__ == type(o).__name__ and self.children_list == o.children_list

    def __hash__(self):
        return len(str(self))

    def derivative(self, s):
        l, r = self.children_list
        ret = Alternative_node([
            Concat_node([l.delta(), r.derivative(s)]),
            Concat_node([l.derivative(s), r])
        ]).simplify()
        return ret

    def delta(self):
        new_children = []
        for i in range(len(self.children_list)):
            new_children.append(self.children_list[i].delta())
        return Concat_node(new_children)

    def reverse(self):
        # print('reverse concat', self)
        rev = deepcopy(self)
        for i in range(len(rev.children_list)):
            rev.children_list[i] = rev.children_list[i].reverse()
        # print(rev.children_list)
        rev.children_list = rev.children_list[::-1]
        # print(rev.children_list)
        # print('reverse concat', rev)
        return rev


class Asterix_node(Regex_node):
    def __init__(self, children_list):
        Regex_node.__init__(self, children_list)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'﴾{self.children_list[0]}﴿*'

    def simplify(self):
        self.children_list[0] = self.children_list[0].simplify()

        if type(self.children_list[0]).__name__ == 'Null_node':
            return Null_node()

        if type(self.children_list[0]).__name__ == 'Symbol_node' and self.children_list[0].symbol == '' or type(self.children_list[0]).__name__ == 'Asterix_node':
            return self.children_list[0]

        return self

    def __eq__(self, o):
        return type(self).__name__ == type(o).__name__ and self.children_list[0] == o.children_list[0]

    def __hash__(self):
        return len(str(self))

    def derivative(self, s):
        new_children = [self.children_list[0].derivative(s), deepcopy(self)]
        return Concat_node(new_children)

    def delta(self):
        return Symbol_node('')

    def reverse(self):
        # print('reverse', self)
        rev = deepcopy(self)
        rev.children_list[0] = rev.children_list[0].reverse()
        return rev


class Symbol_node():
    def __init__(self, symbol):
        self.symbol = symbol

    def __repr__(self):
        return str(self)

    def __str__(self):
        if self.symbol == '':
            return 'ɛ'
        return self.symbol

    def simplify(self):
        return self

    def get_graph_edges(self):
        return []

    def __eq__(self, o):
        return type(self).__name__ == type(o).__name__ and self.symbol == o.symbol

    def __hash__(self):
        return len(str(self))

    def derivative(self, s):
        if self.symbol == s:
            return Symbol_node('')
        else:
            return Null_node()

    def delta(self):
        if self.symbol == '':
            return Symbol_node('')
        else:
            return Null_node()

    def reverse(self):
        # print('reverse', self)
        return deepcopy(self)


class Null_node(Regex_node):
    def __init__(self):
        Regex_node.__init__(self, [])

    def simplify(self):
        return self

    def get_graph_edges(self):
        return []

    def __repr__(self):
        return str(self)

    def __str__(self):
        return 'null'

    def derivative(self, s):
        return Null_node()

    def delta(self):
        return Null_node()

    def reverse(self):
        # print('reverse', self)
        return Null_node()


if __name__ == '__main__':
    a = Symbol_node('a')
    b = Symbol_node('b')
    # print(a == b)
