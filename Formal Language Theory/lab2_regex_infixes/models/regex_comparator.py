from models.brzozovski_fa import Brozozovsky_fa
from tools.graph_creator import Graph_creator


class Is_in_checker():
    def __init__(self):
        pass

    def l1_in_l2(self, r1, r2):
        self.b1, self.b2 = Brozozovsky_fa(r1), Brozozovsky_fa(r2)
        self.b1.build_complete_automata()
        self.b2.build_complete_automata()
        self.F1, self.F2 = self.b1.get_finals(), self.b2.get_finals()
        self.S1, self.S2 = self.b1.start_node, self.b2.start_node
        self.memory = set()
        self.edge_num = 1

        Graph_creator('graph_re1.dot',
                      self.b1.get_graph_edges()).write_to_file()
        Graph_creator('graph_re2.dot',
                      self.b2.get_graph_edges()).write_to_file()

        print('L({0:<15s} L({1:<15s}'.format(
            str(r1)+')', str(r2)+')'), end='  <-  ')

        self.f_num = 0
        self.edges_buffer = []
        for f1 in self.F1:
            self.f_num += 1
            # print('NEW f1:', f1)
            for f2 in self.F2:
                # print('TRY f2:', f2)
                if self.rec_foo(f1, f2):
                    # print(f1, 'isin', f2)
                    break
            else:
                # print('no valid subgraph for final state', f1)
                Graph_creator('f_subgraphs.dot',
                              self.edges_buffer).write_to_file()
                return False

        Graph_creator('f_subgraphs.dot',
                      self.edges_buffer).write_to_file()
        return True

    def rec_foo(self, q1, q2):
        # print(self.f_num, '#### checking pair:', q1, q2)
        
        alph1_uncycled = self.b1.get_uncycled_node_input_alphabeth(q1)
        alph1_cycled = self.b1.get_cycled_node_input_alphabeth(q1)
        alph2 = self.b2.get_node_input_alphabeth(q2)
        # print(f'{q1} is cycled by {alph1_cycled}')
        # print(f'{q1} is uncycled by {alph1_uncycled}')
        
        if alph1_cycled:
            for alpha in alph1_cycled:
                if self.b2.is_cycled_by(q2, alpha):
                    pass
                else:
                    return False

        if not alph1_uncycled.issubset(alph2):
            return False

        if q1 == self.S1 and q2 != self.S2:
            # print('path in second automata is longer')
            return False

        if q1 == self.S1 and q2 == self.S2:
            # print(self.f_num, 'they are both start')
            return True

        # print(self.f_num, 'now check for alphas')
        for alpha in alph1_uncycled:
            # print(self.f_num, 'alpha =', alpha)
            Q1 = self.b1.get_parent_nodes_by_alpha(q1, alpha)
            Q2 = self.b2.get_parent_nodes_by_alpha(q2, alpha)
            # print(self.f_num, 'Qs', Q1, Q2)

            for q1_p in Q1:
                for q2_p in Q2:
                    if (alpha, q1_p, q2_p) in self.memory:
                        # print('already checked')
                        break
                    else:
                        self.memory.add((alpha, q1_p, q2_p))
                        # print(f'NEW_EDGE {q2_p} {alpha} {q2}')
                        self.edges_buffer.append({
                            'child': f'"{str(q2) + str(self.f_num)}"',
                            'child_label': f'{str(q2)}',

                            'label': f'{alpha} {self.edge_num}',

                            'parent': f'"{str(q2_p) + str(self.f_num)}"',
                            'parent_label': f'{str(q2_p)}',
                        })
                        self.edge_num += 1

                        if self.rec_foo(q1_p, q2_p):
                            break

                else:
                    return False
        # print('all paths matched:', q1, q2)
        return True
