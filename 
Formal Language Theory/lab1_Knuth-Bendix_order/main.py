from parser import Parser
from checker import Checker

from subprocess import Popen, PIPE, STDOUT, run


if __name__ == '__main__':
    p = Parser()
    p.parse_file('tests/test3.txt')
    ch = Checker(p)
    ch.start_checking()