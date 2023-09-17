package parser

import (
	"fmt"

	"github.com/antlr/antlr4/runtime/Go/antlr/v4"
)

// START
func (s *MyEmlangListener) EnterStart(ctx *StartContext) {
	s.newBlock()
	s.addBlockToMain(s.curBlock())
}

func (s *MyEmlangListener) ExitStart(ctx *StartContext) {
	// for _, x := range s.blocks {
	// 	x.makePhi()
	// }
}

// DECLARATION
func (s *MyEmlangListener) EnterDeclaration(ctx *DeclarationContext) {}
func (s *MyEmlangListener) ExitDeclaration(ctx *DeclarationContext) {
	name := ctx.IDENT().GetText()
	if s.curBlock().isVariableIn(name) {
		return
	}
	s.curBlock().allocaVariable(name)
}

// ASSIGNATION
func (s *MyEmlangListener) EnterAssignation(ctx *AssignationContext) {}
func (s *MyEmlangListener) ExitAssignation(ctx *AssignationContext) {
	dstName := ctx.IDENT().GetText()
	expr := s.popExpr()
	if s.curBlock().isVariableIn(dstName) {
		s.curBlock().setVariable(dstName, expr)
	} else {
		panic(fmt.Sprintf("NO SUCH VARIABLE DEFINED IN THIS SCOPE: %s", dstName))
	}
}

// LOL
func (s *MyEmlangListener) EnterLolStmt(ctx *LolStmtContext) {}
func (s *MyEmlangListener) ExitLolStmt(ctx *LolStmtContext) {
	if s.isCurBlockRetTrue() {
		return
	}
	// fmt.Println("	NEWLOL IN", s.curBlock())
	s.popExpr()
}

func (s *MyEmlangListener) VisitTerminal(node antlr.TerminalNode)      {}
func (s *MyEmlangListener) VisitErrorNode(node antlr.ErrorNode)        {}
func (s *MyEmlangListener) EnterEveryRule(ctx antlr.ParserRuleContext) {}
func (s *MyEmlangListener) ExitEveryRule(ctx antlr.ParserRuleContext)  {}
func (s *MyEmlangListener) EnterBlock(ctx *BlockContext)               {}
func (s *MyEmlangListener) ExitBlock(ctx *BlockContext)                {}
func (s *MyEmlangListener) EnterPart(ctx *PartContext)                 {}
func (s *MyEmlangListener) ExitPart(ctx *PartContext)                  {}
