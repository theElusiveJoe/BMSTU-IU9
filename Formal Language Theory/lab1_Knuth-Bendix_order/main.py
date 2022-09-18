from parser import Parser
from checker import Checker
import sys


if __name__ == '__main__':
    p = Parser()
    p.parse_file(sys.argv[1])
    ch = Checker(p)
    ch.start_checking()