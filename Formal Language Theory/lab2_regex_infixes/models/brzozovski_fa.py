from tools.graph_creator import Graph_creator
from copy import deepcopy
from models.regex_parser import Regex_parser


class Brozozovsky_fa():
    def __init__(self, init_regex, graph_filepath='bronzovki_fa.dot'):
        self.alphabeth = set(
            filter(lambda x: x.isalpha() and x != 'ɛ' or x == '$', str(init_regex)))

        self.nodes = {init_regex}
        # Regex_parser(raw_text='start').parse().simplify()
        self.start_node = init_regex
        self.finish_nodes = set()

        self.edges = []
        # self.edges = [(self.start_node, alpha, init_regex) for alpha in self.alphabeth]
        self.graph_edges_strings = []

        self.build_complete_automata()

    def __repr__(self):
        nl = '\n'
        return f'BFA: {self.start_node}{nl}{nl.join([str(e[0]) + "->" + e[1]+ "->" + str(e[2]) for e in self.edges])}'

    def add_drivative_by_symbol(self, s):
        for node in deepcopy(self.nodes):
            dnode = node.derivative(s).simplify()
            if type(dnode).__name__ == 'Null_node':
                continue

            dnodes = [dnode]
            if type(dnode).__name__ == 'Alternative_node':
                dnodes = dnode.children_list

            for dnode in dnodes:
                new_edge = (node, s, dnode)

                if not any(map(lambda x: str(x) == str(dnode), self.nodes)):
                    self.nodes.add(dnode)
                if not new_edge in self.edges:
                    self.edges.append(new_edge)

    def add_derivatives_by_alphabet(self):
        old_set = deepcopy(self.nodes)
        old_set_power = len(old_set)
        for s in self.alphabeth:
            self.add_drivative_by_symbol(s)
        new_set_power = len(self.nodes)
        return new_set_power > old_set_power

    def build_complete_automata(self):
        while self.add_derivatives_by_alphabet():
            pass
        return self

    def get_graph_edges(self):
        ret = []
        for e in self.edges:
            ret.append({
                'child': f'"{str(e[2])}"',
                'child_label': f'{str(e[2])}',

                'label': e[1],

                'parent': f'"{str(e[0])}"',
                'parent_label': f'{str(e[0])}',
            })
        return ret

    def get_states_set(self):
        states = set()
        for node in self.nodes:
            if type(node).__name__ == 'Alternative_node':
                states.update(node.children_list)
            else:
                states.add(node)
        return states

    def get_finals(self):
        return set(filter(lambda x: type(x.delta().simplify()).__name__ != 'Null_node', self.nodes))

    def get_node_input_alphabeth(self, node):
        return set(
            map(
                lambda x: x[1],
                (filter(lambda x: x[2] == node, self.edges))
            )
        )

    def get_uncycled_node_input_alphabeth(self, node):
        ret = set()
        for x in self.get_node_input_alphabeth(node):
            if (node, x, node) in self.edges:
                continue
            ret.add(x)
        return ret

    def get_cycled_node_input_alphabeth(self, node):
        ret = set()
        for x in self.get_node_input_alphabeth(node):
            if (node, x, node) not in self.edges:
                continue
            ret.add(x)
        return ret

    def get_node_output_alphabeth(self, node):
        return set(
            map(
                lambda x: x[1],
                (filter(lambda x: x[0] == node, self.edges))
            )
        )

    def get_parent_nodes_by_alpha(self, node, alpha):
        return set(map(
            lambda x: x[0],
            filter(lambda x: x[1] == alpha and x[2] == node, self.edges)
        ))

    def get_child(self, node, alpha):
        ret = False
        for x in self.edges:
            if x[0] == node and x[1] == alpha:
                ret = x[2]

        # print('| GET CHILD', node, alpha, ret)
        # print('|', self.edges)

        return ret

    def is_cycled_by(self, node, alpha):
        def loop(node, alpha, memory):
            new_node = self.get_child(node, alpha)
            if not new_node:
                return False

            if new_node in memory:
                return True

            memory.add(new_node)
            return loop(node, alpha, memory)

        res = loop(node, alpha, set())
        return res
