package parser

import (
	"fmt"
)

// EXPR
func (s *MyEmlangListener) EnterExpr(ctx *ExprContext) {}
func (s *MyEmlangListener) ExitExpr(ctx *ExprContext)  {}
func (s *MyEmlangListener) EnterPexp(ctx *PexpContext) {}
func (s *MyEmlangListener) ExitPexp(ctx *PexpContext) {
	if s.isCurBlockRetTrue() {
		return
	}
	op := ctx.OP().GetText()
	oper2, oper1 := s.popExpr(), s.popExpr()
	tempvar := s.curBlock().createTempVariable()
	newinstr := &Instruction{"", []string{oper1, oper2, tempvar.name}}
	switch op {
	case "+":
		newinstr.typ = "add"
	case "-":
		newinstr.typ = "sub"
	case "*":
		newinstr.typ = "mul"
	}
	s.curBlock().addInstr(newinstr)
	s.pushExpr(tempvar.name)
}

// NUMBER
func (s *MyEmlangListener) EnterNumber(ctx *NumberContext) {}
func (s *MyEmlangListener) ExitNumber(ctx *NumberContext) {
	if s.isCurBlockRetTrue() {
		return
	}
	num := ctx.NUMBER().GetText()
	s.pushExpr(num)
}

// IDENT
func (s *MyEmlangListener) EnterIdent(ctx *IdentContext) {}
func (s *MyEmlangListener) ExitIdent(ctx *IdentContext) {
	// Записываем переменную как выражение в стек
	destName := ctx.IDENT().GetText()
	if s.curBlock().isVariableIn(destName) {
		destVal := s.curBlock().variables[destName]
		destLoad := destVal.name
		s.pushExpr(destLoad)
	} else {
		panic(fmt.Sprintf("NO SUCH VARIABLE DEFINED IN THIS SCOPE: %s", destName))
	}
}
