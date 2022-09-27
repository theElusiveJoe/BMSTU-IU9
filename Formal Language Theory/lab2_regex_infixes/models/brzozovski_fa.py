from tools.graph_creator import Graph_creator
from copy import deepcopy


class Brozozovsky_fa():
    def __init__(self, init_regex, graph_filepath='bronzovki_fa.dot'):
        self.alphabeth = set(
            filter(lambda x: x.isalpha() and x != 'ɛ', str(init_regex)))
        self.init_regex = init_regex
        self.nodes = {init_regex}
        self.graph_edges = []

    def add_drivative_by_symbol(self, s):
        for node in deepcopy(self.nodes):
            dnode = node.derivative(s).simplify()
            if type(dnode).__name__ == 'Null_node' or any(map(lambda x: str(x) == str(dnode), self.nodes)):
                continue
            self.nodes.add(dnode)
            self.graph_edges.append({
                'parent': f'"{str(node)}"',
                'parent_label': f'{str(node)}',
                'child': f'"{str(dnode)}"',
                'child_label': f'{str(dnode)}',
                'label': s
            })

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
        return self.graph_edges

    def get_states_set(self):
        states = set()
        for node in self.nodes:
            if type(node).__name__ == 'Alternative_node':
                states.update(node.children_list)
            else:
                states.add(node)
        return states