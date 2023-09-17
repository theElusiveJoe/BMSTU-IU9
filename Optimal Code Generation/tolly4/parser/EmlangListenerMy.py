# Generated from Emlang.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .EmlangParser import EmlangParser
else:
    from EmlangParser import EmlangParser

from parser.myBB import *

# This class defines a complete listener for a parse tree produced by EmlangParser.
class MyEmlangListener(ParseTreeListener):
    def __init__(self):
        super().__init__()
        self.block_counter = 0
        self.blocks = []
        self.main = []
        self.stack = []
        self.stack_for_while_loops = []

    def __str__(self):
        return '\n'.join(map(str, self.main))

    def to_graph(self):
        ret = "digraph G{\nnode [shape=box nojustify=false]\n"
        for x in self.main:
            ret += f'{x.block_num} [label=\"\b{str(x)}\"]\n'
            last = x.instructions[-1]
            if last.typ == BR:
                ret += f'{x.block_num} -> {last.args["dest"]}\n'
            elif last.typ == CONDBR:
                ret += f'{x.block_num} -> {last.args["dest1"]} [label=true]\n'
                ret += f'{x.block_num} -> {last.args["dest2"]} [label=false]\n'
        ret += "}\n"
        return ret

    def pop_expr(self):
        return self.stack.pop()

    def push_expr(self, expr):
        self.stack.append(expr)

    def new_block(self):
        bb = BB()
        bb.block_num = self.block_counter
        self.block_counter +=1
        self.blocks.append(bb)
        return bb

    def cur_block(self):
        return self.blocks[-1]

    def get_block(self, i):
        return self.blocks[len(self.blocks)-1-i]

    def pop_block(self):
        return self.blocks.pop()
    
    def push_block(self, bb):
        self.blocks.append(bb)

    def add_block_to_main(self, bb):
        self.main.append(bb)
    
    def set_cur_block_ret_true(self):
        self.cur_block().returned =True

    def is_cur_block_ret_true(self):
        return self.cur_block().returned

    def pop_while_cond_block(self):
        return self.stack_for_while_loops.pop()

    def push_while_cond_block(self, bb):
        self.stack_for_while_loops.append(bb)

    
    # Enter a parse tree produced by EmlangParser#start.
    def enterStart(self, ctx:EmlangParser.StartContext):
        self.new_block()
        self.add_block_to_main(self.cur_block())

    # Exit a parse tree produced by EmlangParser#start.
    def exitStart(self, ctx:EmlangParser.StartContext):
        pass


    # Enter a parse tree produced by EmlangParser#block.
    def enterBlock(self, ctx:EmlangParser.BlockContext):
        pass

    # Exit a parse tree produced by EmlangParser#block.
    def exitBlock(self, ctx:EmlangParser.BlockContext):
        pass


    # Enter a parse tree produced by EmlangParser#part.
    def enterPart(self, ctx:EmlangParser.PartContext):
        pass

    # Exit a parse tree produced by EmlangParser#part.
    def exitPart(self, ctx:EmlangParser.PartContext):
        pass


    # Enter a parse tree produced by EmlangParser#declaration.
    def enterDeclaration(self, ctx:EmlangParser.DeclarationContext):
        pass

    # Exit a parse tree produced by EmlangParser#declaration.
    def exitDeclaration(self, ctx:EmlangParser.DeclarationContext):
        name = ctx.IDENT().getText()
        if self.cur_block().is_variable_in(name):
            return
        self.cur_block().alloca_variable(name)


    # Enter a parse tree produced by EmlangParser#assignation.
    def enterAssignation(self, ctx:EmlangParser.AssignationContext):
        pass

    # Exit a parse tree produced by EmlangParser#assignation.
    def exitAssignation(self, ctx:EmlangParser.AssignationContext):
        dst_name = ctx.IDENT().getText()
        expr = self.pop_expr()
        if self.cur_block().is_variable_in(dst_name):
            self.cur_block().set_variable(dst_name, expr)
        else:
            raise Exception(f'переменная не определена: {dst_name}')


    # Enter a parse tree produced by EmlangParser#expr.
    def enterExpr(self, ctx:EmlangParser.ExprContext):
        pass

    # Exit a parse tree produced by EmlangParser#expr.
    def exitExpr(self, ctx:EmlangParser.ExprContext):
        pass


    # Enter a parse tree produced by EmlangParser#pexp.
    def enterPexp(self, ctx:EmlangParser.PexpContext):
        pass

    # Exit a parse tree produced by EmlangParser#pexp.
    def exitPexp(self, ctx:EmlangParser.PexpContext):
        # if self.is_cur_block_ret_true():
        #     return
        
        op = ctx.OP().getText()
        oper1, oper2 = self.pop_expr(), self.pop_expr()
        tmpvar = self.cur_block().create_tmp_var()
        typ = ADD if op == '+' else SUB if op == '-' else MUL
        self.cur_block().add_instr(Instruction(typ, {"oper1": oper1, "oper2":oper2, "to":tmpvar}))
        self.push_expr(tmpvar)


    # Enter a parse tree produced by EmlangParser#ident.
    def enterIdent(self, ctx:EmlangParser.IdentContext):
        pass

    # Exit a parse tree produced by EmlangParser#ident.
    def exitIdent(self, ctx:EmlangParser.IdentContext):
        dest = ctx.IDENT().getText()
        if self.cur_block().is_variable_in(dest):
            self.push_expr(self.cur_block().variables[dest])
        else:
            raise Exception(f'переменная не определена: {dest}')
            


    # Enter a parse tree produced by EmlangParser#number.
    def enterNumber(self, ctx:EmlangParser.NumberContext):
        pass

    # Exit a parse tree produced by EmlangParser#number.
    def exitNumber(self, ctx:EmlangParser.NumberContext):
        num = int(ctx.NUMBER().getText())
        self.push_expr(IntConst(num))


    # Enter a parse tree produced by EmlangParser#ifElseStmt.
    def enterIfElseStmt(self, ctx:EmlangParser.IfElseStmtContext):
        pass

    # Exit a parse tree produced by EmlangParser#ifElseStmt.
    def exitIfElseStmt(self, ctx:EmlangParser.IfElseStmtContext):
        b2, b1 = self.pop_block(), self.pop_block()
        oldb = self.pop_block()
        # if oldb.returned:
        #     return
        nb = self.new_block()
        nb.set_map(oldb)

        if not b1.returned:
            b1.new_break(nb)
        if not b2.returned:
            b2.new_break(nb)
        self.add_block_to_main(nb)
        


    # Enter a parse tree produced by EmlangParser#cond.
    def enterCond(self, ctx:EmlangParser.CondContext):
        pass

    # Exit a parse tree produced by EmlangParser#cond.
    def exitCond(self, ctx:EmlangParser.CondContext):
        b1, b2 = self.new_block(), self.new_block()
        b1.set_map(self.get_block(2))
        b2.set_map(self.get_block(2))
        cond = self.get_block(2).new_compare(self.pop_expr(), IntConst(0))
        self.get_block(2).new_cond_break(cond, b2, b1)
        self.add_block_to_main(b1)
        self.add_block_to_main(b2)


    # Enter a parse tree produced by EmlangParser#block1.
    def enterBlock1(self, ctx:EmlangParser.Block1Context):
        pass

    # Exit a parse tree produced by EmlangParser#block1.
    def exitBlock1(self, ctx:EmlangParser.Block1Context):
        pass


    # Enter a parse tree produced by EmlangParser#block2.
    def enterBlock2(self, ctx:EmlangParser.Block2Context):
        self.blocks[-1], self.blocks[-2] = self.blocks[-2], self.blocks[-1]

    # Exit a parse tree produced by EmlangParser#block2.
    def exitBlock2(self, ctx:EmlangParser.Block2Context):
        pass


    # Enter a parse tree produced by EmlangParser#whileStmt.
    def enterWhileStmt(self, ctx:EmlangParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by EmlangParser#whileStmt.
    def exitWhileStmt(self, ctx:EmlangParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by EmlangParser#wblock.
    def enterWblock(self, ctx:EmlangParser.WblockContext):
        pass

    # Exit a parse tree produced by EmlangParser#wblock.
    def exitWblock(self, ctx:EmlangParser.WblockContext):
        if not self.cur_block().returned:
            self.cur_block().new_break(self.pop_while_cond_block())
        self.pop_block()


    # Enter a parse tree produced by EmlangParser#wcond.
    def enterWcond(self, ctx:EmlangParser.WcondContext):
        base = self.pop_block()
        cb = self.new_block()
        cb.set_map(base)
        self.add_block_to_main(cb)
        base.new_break(cb)
        self.push_while_cond_block(cb)

    # Exit a parse tree produced by EmlangParser#wcond.
    def exitWcond(self, ctx:EmlangParser.WcondContext):
        cb = self.pop_block()
        ab = self.new_block()
        ab.set_map(cb)
        self.add_block_to_main(ab)
        lb = self.new_block()
        lb.set_map(cb)
        self.add_block_to_main(lb)

        cond = cb.new_compare(self.pop_expr(), IntConst(0))
        cb.new_cond_break(cond, ab, lb)


    # Enter a parse tree produced by EmlangParser#returnStmt.
    def enterReturnStmt(self, ctx:EmlangParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by EmlangParser#returnStmt.
    def exitReturnStmt(self, ctx:EmlangParser.ReturnStmtContext):
        if self.is_cur_block_ret_true():
            return
        self.cur_block().new_ret(self.pop_expr())
        self.set_cur_block_ret_true()


    # Enter a parse tree produced by EmlangParser#lolStmt.
    def enterLolStmt(self, ctx:EmlangParser.LolStmtContext):
        pass

    # Exit a parse tree produced by EmlangParser#lolStmt.
    def exitLolStmt(self, ctx:EmlangParser.LolStmtContext):
        pass

    
     