import sys
from antlr4 import *
from parser.EmlangLexer import EmlangLexer
from parser.EmlangParser import EmlangParser
from parser.EmlangListenerMy import MyEmlangListener

def create_and_process_tree():
    n = int(sys.argv[1])

    filename = f'emlangProgs/prog{n}.emlang'
    input_stream = FileStream(filename)
    lexer = EmlangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = EmlangParser(stream)
    
    listener = MyEmlangListener()
    tree = parser.start()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    return listener

