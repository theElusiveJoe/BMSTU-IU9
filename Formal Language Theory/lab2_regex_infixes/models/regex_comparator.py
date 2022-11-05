from models.brzozovski_fa import Brozozovsky_fa
from tools.graph_creator import Graph_creator
from models import regex_node
from copy import deepcopy
from models.regex_node import *


class Is_in_checker():
    def __init__(self):
        pass

    def l1_in_l2(self, r1, r2):
        r1 = Concat_node([Symbol_node('$'), r1])
        r2 = Concat_node([Symbol_node('$'), r2])
        self.b1, self.b2 = Brozozovsky_fa(r1), Brozozovsky_fa(r2)

        # собираем множество финальных состояний
        self.F1, self.F2 = self.b1.get_finals(), self.b2.get_finals()

        # берем начальные узлы
        self.S1, self.S2 = self.b1.start_node, self.b2.start_node

        # запоминаем, где мы уже были
        self.memory = set()
        # и ведем счет узлам, в которых побывали
        self.edge_num = 1

        # нарисуем графы
        Graph_creator('graph_re1.dot',
                      self.b1.get_graph_edges()).write_to_file()
        Graph_creator('graph_re2.dot',
                      self.b2.get_graph_edges()).write_to_file()

        # print('L({0:<15s} L({1:<15s}'.format(str(r1)+')', str(r2)+')'), end='  <-  ')

        self.f_num = 0
        self.edges_buffer = []
        # каждому финальному узлу r1 пытаемся сопоставить все финальные узлы r2
        for f1 in self.F1:
            self.f_num += 1
            # print('NEW f1:', f1)
            if self.rec_foo(f1, set(self.F2)):
                pass
                # print(f1, 'is in', self.F2)
            else:
                # print('no valid subgraph for final state', f1)
                Graph_creator('f_subgraphs.dot',
                              self.edges_buffer).write_to_file()
                return False

        Graph_creator('f_subgraphs.dot',
                      self.edges_buffer).write_to_file()
        return True

    def rec_foo(self, q1, Q22):
        # q1 - узел из r1, Q22 - узлы, которые мы хотим ему сопоставить
        # print(self.f_num, '#### checking pair:', q1, Q22)

        # если q1 - стартовый, а в Q22 нет ни одного стартового, то q1 не может в них вложиться
        if q1 == self.S1 and not (any(map(lambda q: q == self.S2, Q22))):
            # print('path in secon automata is longer')
            return False

        # выделим входной алфавит первого узла
        alph1 = self.b1.get_node_input_alphabeth(q1)
        # и объединение входных алфавитов узлов Q22
        alph2 = set()
        for q2 in Q22:
            alph2.update(set(self.b2.get_node_input_alphabeth(q2)))
        # если есть буква, по которой можно прийти в q1, но ни в один из Q22, то вложения нет
        if not alph1.issubset(alph2):
            # print(self.f_num, 'alphabeth false')
            return False


        # print(list(Q22)[0])
        # print(*(map(lambda q: q == self.S2, set(Q22))))


        # этот кусок кода полностью опционален (по крайней мере, на наборе тестов)
        if q1 == self.S1 and any(map(lambda q: q == self.S2, list(Q22))):
            # print(self.f_num, 'they are both start')
            return True

        # print(self.f_num, 'now check for alphas')

        # для каждой буквы из входного алфавита q1
        for alpha in alph1:
            # print(self.f_num, 'alpha =', alpha)
            # берем множество родиткельских узлов для q1
            Q1 = self.b1.get_parent_nodes_by_alpha(q1, alpha)

            Q2 = set()
            # в Q2 помещаем множества множеств родительских узлов из Q22
            for q2 in Q22:
                Q2.update(set(self.b2.get_parent_nodes_by_alpha(q2, alpha)))
            # print(self.f_num, 'Qs', Q1, *Q2)
            print(Q1, Q2)
            print(len(Q1), len(Q2))
            for q1_p in Q1:
                # for Q2_p in Q2:
                    # print(q1_p, Q2_p, ' - new pair')
                    # если такая пара уже встречалась
                if (alpha, q1_p, frozenset(Q2)) in self.memory:
                    # print('already checked')
                    # то не рассматриваем ее во второй раз
                    break
                else:
                    self.memory.add((alpha, q1_p, frozenset(Q2)))
                    # print(f'NEW_EDGE {Q2_p} {alpha} {Q22}')
                    self.edges_buffer.append({
                        'child': f'"{str(Q22) + str(self.f_num)}"',
                        'child_label': f'{str(Q22)}',

                        'label': f'{alpha} {self.edge_num}',

                        'parent': f'"{str(Q2) + str(self.f_num)}"',
                        'parent_label': f'{str(Q2)}',
                    })
                    self.edge_num += 1

                    if self.rec_foo(q1_p, Q2):
                        break

            else:
                    # если не разу не брейкнули цикл
                return False
        # print('all paths matched:', q1, Q22)
        return True

    def filter_set(self, sett):
        c_sett = deepcopy(sett)
        for re in c_sett:
            if any(map(lambda x: self.l1_in_l2(re, x) and not (x == re), sett)):
                # print('Excessive: ', re)
                sett.remove(re)
        return sett
