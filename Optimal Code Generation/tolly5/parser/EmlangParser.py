# Generated from Emlang.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,17,110,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,0,1,0,1,1,1,1,
        5,1,43,8,1,10,1,12,1,46,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,
        56,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,3,5,70,8,
        5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,
        9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,1,
        15,1,15,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,0,0,18,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,0,99,0,36,1,0,0,0,
        2,40,1,0,0,0,4,55,1,0,0,0,6,57,1,0,0,0,8,61,1,0,0,0,10,69,1,0,0,
        0,12,71,1,0,0,0,14,77,1,0,0,0,16,79,1,0,0,0,18,81,1,0,0,0,20,87,
        1,0,0,0,22,89,1,0,0,0,24,91,1,0,0,0,26,93,1,0,0,0,28,97,1,0,0,0,
        30,99,1,0,0,0,32,101,1,0,0,0,34,105,1,0,0,0,36,37,5,1,0,0,37,38,
        3,2,1,0,38,39,5,0,0,1,39,1,1,0,0,0,40,44,5,2,0,0,41,43,3,4,2,0,42,
        41,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,47,1,0,0,
        0,46,44,1,0,0,0,47,48,5,3,0,0,48,3,1,0,0,0,49,56,3,6,3,0,50,56,3,
        8,4,0,51,56,3,18,9,0,52,56,3,32,16,0,53,56,3,34,17,0,54,56,3,26,
        13,0,55,49,1,0,0,0,55,50,1,0,0,0,55,51,1,0,0,0,55,52,1,0,0,0,55,
        53,1,0,0,0,55,54,1,0,0,0,56,5,1,0,0,0,57,58,5,4,0,0,58,59,5,17,0,
        0,59,60,5,5,0,0,60,7,1,0,0,0,61,62,5,6,0,0,62,63,5,17,0,0,63,64,
        3,10,5,0,64,65,5,5,0,0,65,9,1,0,0,0,66,70,3,14,7,0,67,70,3,16,8,
        0,68,70,3,12,6,0,69,66,1,0,0,0,69,67,1,0,0,0,69,68,1,0,0,0,70,11,
        1,0,0,0,71,72,5,7,0,0,72,73,5,14,0,0,73,74,3,10,5,0,74,75,3,10,5,
        0,75,76,5,8,0,0,76,13,1,0,0,0,77,78,5,17,0,0,78,15,1,0,0,0,79,80,
        5,15,0,0,80,17,1,0,0,0,81,82,5,9,0,0,82,83,3,20,10,0,83,84,3,22,
        11,0,84,85,5,10,0,0,85,86,3,24,12,0,86,19,1,0,0,0,87,88,3,10,5,0,
        88,21,1,0,0,0,89,90,3,2,1,0,90,23,1,0,0,0,91,92,3,2,1,0,92,25,1,
        0,0,0,93,94,5,11,0,0,94,95,3,30,15,0,95,96,3,28,14,0,96,27,1,0,0,
        0,97,98,3,2,1,0,98,29,1,0,0,0,99,100,3,10,5,0,100,31,1,0,0,0,101,
        102,5,12,0,0,102,103,3,10,5,0,103,104,5,5,0,0,104,33,1,0,0,0,105,
        106,5,13,0,0,106,107,3,10,5,0,107,108,5,5,0,0,108,35,1,0,0,0,3,44,
        55,69
    ]

class EmlangParser ( Parser ):

    grammarFileName = "Emlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'{'", "'}'", "'decl'", "';'", 
                     "'assign'", "'('", "')'", "'if'", "'else'", "'while'", 
                     "'return'", "'lol'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "OP", "NUMBER", "WHITESPACE", 
                      "IDENT" ]

    RULE_start = 0
    RULE_block = 1
    RULE_part = 2
    RULE_declaration = 3
    RULE_assignation = 4
    RULE_expr = 5
    RULE_pexp = 6
    RULE_ident = 7
    RULE_number = 8
    RULE_ifElseStmt = 9
    RULE_cond = 10
    RULE_block1 = 11
    RULE_block2 = 12
    RULE_whileStmt = 13
    RULE_wblock = 14
    RULE_wcond = 15
    RULE_returnStmt = 16
    RULE_lolStmt = 17

    ruleNames =  [ "start", "block", "part", "declaration", "assignation", 
                   "expr", "pexp", "ident", "number", "ifElseStmt", "cond", 
                   "block1", "block2", "whileStmt", "wblock", "wcond", "returnStmt", 
                   "lolStmt" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    OP=14
    NUMBER=15
    WHITESPACE=16
    IDENT=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(EmlangParser.BlockContext,0)


        def EOF(self):
            return self.getToken(EmlangParser.EOF, 0)

        def getRuleIndex(self):
            return EmlangParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = EmlangParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(EmlangParser.T__0)
            self.state = 37
            self.block()
            self.state = 38
            self.match(EmlangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EmlangParser.PartContext)
            else:
                return self.getTypedRuleContext(EmlangParser.PartContext,i)


        def getRuleIndex(self):
            return EmlangParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = EmlangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(EmlangParser.T__1)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 14928) != 0):
                self.state = 41
                self.part()
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 47
            self.match(EmlangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(EmlangParser.DeclarationContext,0)


        def assignation(self):
            return self.getTypedRuleContext(EmlangParser.AssignationContext,0)


        def ifElseStmt(self):
            return self.getTypedRuleContext(EmlangParser.IfElseStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(EmlangParser.ReturnStmtContext,0)


        def lolStmt(self):
            return self.getTypedRuleContext(EmlangParser.LolStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(EmlangParser.WhileStmtContext,0)


        def getRuleIndex(self):
            return EmlangParser.RULE_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPart" ):
                listener.enterPart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPart" ):
                listener.exitPart(self)




    def part(self):

        localctx = EmlangParser.PartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_part)
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.declaration()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.assignation()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.ifElseStmt()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 52
                self.returnStmt()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 5)
                self.state = 53
                self.lolStmt()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 6)
                self.state = 54
                self.whileStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(EmlangParser.IDENT, 0)

        def getRuleIndex(self):
            return EmlangParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = EmlangParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(EmlangParser.T__3)
            self.state = 58
            self.match(EmlangParser.IDENT)
            self.state = 59
            self.match(EmlangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(EmlangParser.IDENT, 0)

        def expr(self):
            return self.getTypedRuleContext(EmlangParser.ExprContext,0)


        def getRuleIndex(self):
            return EmlangParser.RULE_assignation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignation" ):
                listener.enterAssignation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignation" ):
                listener.exitAssignation(self)




    def assignation(self):

        localctx = EmlangParser.AssignationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(EmlangParser.T__5)
            self.state = 62
            self.match(EmlangParser.IDENT)
            self.state = 63
            self.expr()
            self.state = 64
            self.match(EmlangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(EmlangParser.IdentContext,0)


        def number(self):
            return self.getTypedRuleContext(EmlangParser.NumberContext,0)


        def pexp(self):
            return self.getTypedRuleContext(EmlangParser.PexpContext,0)


        def getRuleIndex(self):
            return EmlangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = EmlangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expr)
        try:
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.ident()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.number()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.pexp()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP(self):
            return self.getToken(EmlangParser.OP, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EmlangParser.ExprContext)
            else:
                return self.getTypedRuleContext(EmlangParser.ExprContext,i)


        def getRuleIndex(self):
            return EmlangParser.RULE_pexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPexp" ):
                listener.enterPexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPexp" ):
                listener.exitPexp(self)




    def pexp(self):

        localctx = EmlangParser.PexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_pexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(EmlangParser.T__6)
            self.state = 72
            self.match(EmlangParser.OP)
            self.state = 73
            self.expr()
            self.state = 74
            self.expr()
            self.state = 75
            self.match(EmlangParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(EmlangParser.IDENT, 0)

        def getRuleIndex(self):
            return EmlangParser.RULE_ident

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdent" ):
                listener.enterIdent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdent" ):
                listener.exitIdent(self)




    def ident(self):

        localctx = EmlangParser.IdentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ident)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(EmlangParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(EmlangParser.NUMBER, 0)

        def getRuleIndex(self):
            return EmlangParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = EmlangParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(EmlangParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfElseStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cond(self):
            return self.getTypedRuleContext(EmlangParser.CondContext,0)


        def block1(self):
            return self.getTypedRuleContext(EmlangParser.Block1Context,0)


        def block2(self):
            return self.getTypedRuleContext(EmlangParser.Block2Context,0)


        def getRuleIndex(self):
            return EmlangParser.RULE_ifElseStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfElseStmt" ):
                listener.enterIfElseStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfElseStmt" ):
                listener.exitIfElseStmt(self)




    def ifElseStmt(self):

        localctx = EmlangParser.IfElseStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ifElseStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(EmlangParser.T__8)
            self.state = 82
            self.cond()
            self.state = 83
            self.block1()
            self.state = 84
            self.match(EmlangParser.T__9)
            self.state = 85
            self.block2()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(EmlangParser.ExprContext,0)


        def getRuleIndex(self):
            return EmlangParser.RULE_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond" ):
                listener.enterCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond" ):
                listener.exitCond(self)




    def cond(self):

        localctx = EmlangParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(EmlangParser.BlockContext,0)


        def getRuleIndex(self):
            return EmlangParser.RULE_block1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock1" ):
                listener.enterBlock1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock1" ):
                listener.exitBlock1(self)




    def block1(self):

        localctx = EmlangParser.Block1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_block1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(EmlangParser.BlockContext,0)


        def getRuleIndex(self):
            return EmlangParser.RULE_block2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock2" ):
                listener.enterBlock2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock2" ):
                listener.exitBlock2(self)




    def block2(self):

        localctx = EmlangParser.Block2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_block2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def wcond(self):
            return self.getTypedRuleContext(EmlangParser.WcondContext,0)


        def wblock(self):
            return self.getTypedRuleContext(EmlangParser.WblockContext,0)


        def getRuleIndex(self):
            return EmlangParser.RULE_whileStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)




    def whileStmt(self):

        localctx = EmlangParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(EmlangParser.T__10)
            self.state = 94
            self.wcond()
            self.state = 95
            self.wblock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WblockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(EmlangParser.BlockContext,0)


        def getRuleIndex(self):
            return EmlangParser.RULE_wblock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWblock" ):
                listener.enterWblock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWblock" ):
                listener.exitWblock(self)




    def wblock(self):

        localctx = EmlangParser.WblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_wblock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WcondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(EmlangParser.ExprContext,0)


        def getRuleIndex(self):
            return EmlangParser.RULE_wcond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWcond" ):
                listener.enterWcond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWcond" ):
                listener.exitWcond(self)




    def wcond(self):

        localctx = EmlangParser.WcondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_wcond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(EmlangParser.ExprContext,0)


        def getRuleIndex(self):
            return EmlangParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)




    def returnStmt(self):

        localctx = EmlangParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(EmlangParser.T__11)
            self.state = 102
            self.expr()
            self.state = 103
            self.match(EmlangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LolStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(EmlangParser.ExprContext,0)


        def getRuleIndex(self):
            return EmlangParser.RULE_lolStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLolStmt" ):
                listener.enterLolStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLolStmt" ):
                listener.exitLolStmt(self)




    def lolStmt(self):

        localctx = EmlangParser.LolStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_lolStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(EmlangParser.T__12)
            self.state = 106
            self.expr()
            self.state = 107
            self.match(EmlangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





