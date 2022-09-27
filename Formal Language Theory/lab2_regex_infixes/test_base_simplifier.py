import sys
from models.regex_parser import Regex_parser
from tools.graph_creator import Graph_creator
from copy import deepcopy
import re

if __name__ == '__main__':
    tests = open('tests/many_tests.txt', 'r').read().split('\n')

    for test in tests:
        print('\n####################')
        p = Regex_parser(raw_text= test)
        root_node = p.parse()
        print('#base:', root_node)

        root_node = root_node.simplify()
        print('#simplified:', root_node)

        root_node = root_node.derivative('a')
        print('#da:', root_node)

        root_node = root_node.simplify()
        print('#da_simplified:', root_node)

    

