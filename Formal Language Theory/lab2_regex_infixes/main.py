import sys
from models.regex_node import Symbol_node
from models.regex_parser import Regex_parser
from models.brzozovski_fa import Brozozovsky_fa
from tools.graph_creator import Graph_creator
from copy import deepcopy
import re

if __name__ == '__main__':
    p = Regex_parser(filepath = sys.argv[1])
    root = p.parse().simplify()
    
    Graph_creator('graph_1_initial.dot', root.get_graph_edges()).write_to_file()
    print('#base:', root)

    bfa = Brozozovsky_fa(root).build_complete_automata() 
    Graph_creator('bronzovki_fa.dot', bfa.get_graph_edges()).write_to_file()

    result_regexps = set()
    for state in bfa.get_states_set():
        state = state.reverse()
        insf_to_rev = Brozozovsky_fa(state).build_complete_automata().get_states_set()
        for inf_r in insf_to_rev:
            # print(inf_r)
            result_regexps.add(inf_r.reverse())

    result_regexps.remove(Symbol_node(''))
    res = list(result_regexps)
    res.sort(key=str)
    print('INFIXES:')
    for x in res:
        print('->>', x)

