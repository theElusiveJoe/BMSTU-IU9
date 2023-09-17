// Code generated from Emlang.g4 by ANTLR 4.12.0. DO NOT EDIT.

package parser // Emlang

import (
	"fmt"
	_ "fmt"
)

// MyEmlangListener is a complete listener for a parse tree produced by EmlangParser.
type MyEmlangListener struct {
	blockCounter int
	blocks []*BB
	bbs []*BB
	stack [] string
	stackForWhileLoops []*BB
}

func createMyEmlangListener() *MyEmlangListener {
	return &MyEmlangListener{
		0,
		make([]*BB, 0),
		make([]*BB, 0),
		make([]string, 0),
		make([]*BB, 0),
	}
}


// СТЕК С ВЫРАЖЕНИЯМИ
func (s *MyEmlangListener) popExpr() string {
	expr := s.stack[len(s.stack)-1]
	s.stack = s.stack[:len(s.stack)-1]
	return expr
}
// func (s *MyEmlangListener) popExpr() *ir.InstLoad {
// 	expr := s.stack[len(s.stack)-1]
// 	s.stack = s.stack[:len(s.stack)-1]
// 	exprLoad := ir.NewLoad(types.I32, expr)
// 	return exprLoad
// }
func (s *MyEmlangListener) pushExpr(val string){
	s.stack = append(s.stack, val)
}

// СТЕК С БЛОКАМИ
func (s *MyEmlangListener) newBlock() *BB {
	bb :=&BB{
		s.blockCounter,
		make([]*Instruction, 0),
		false,
		make(map[string]*Variable),
		0,
		make(map[string][]int),
		
	}
	s.blockCounter++
	s.bbs = append(s.bbs, bb)
	return bb
}

func (s *MyEmlangListener) curBlock() *BB {
	return s.getBlock(0)
}

func (s *MyEmlangListener) getBlock(i int) *BB{
	return s.bbs[len(s.bbs) - 1 - i]
}

func (s *MyEmlangListener) popBlock() *BB {
	bb := s.curBlock()
	s.bbs = s.bbs[:len(s.bbs)-1]
	return bb
}

func (s *MyEmlangListener) pushBlock(bb *BB){
	s.bbs = append(s.bbs, bb)
}

func (s *MyEmlangListener) addBlockToMain(bb *BB){
	s.blocks = append(s.blocks, bb)
}

func (s *MyEmlangListener) setCurBlockRetTrue(){
	s.curBlock().returned = true
}
func (s *MyEmlangListener) isCurBlockRetTrue() bool{
	return s.curBlock().returned
}

func (s *MyEmlangListener) popwhileCondBlock() *BB {
	bb := s.stackForWhileLoops[len(s.stackForWhileLoops)-1]
	s.stackForWhileLoops = s.stackForWhileLoops[:len(s.stackForWhileLoops)-1]
	return bb
}

func (s *MyEmlangListener) pushwhileCondBlock(bb *BB){
	s.stackForWhileLoops = append(s.stackForWhileLoops, bb)
}

func (s *MyEmlangListener) String()  string{
	ret := ""
	for _, x := range s.blocks{
		ret += x.String() + "\n\n"
	}
	return ret
}

func (s *MyEmlangListener) Graph()  string{
	ret := "digraph G{\nnode [shape=box nojustify=false]\n"
	for _, x := range s.blocks{
		nodeDecl := fmt.Sprintf("%d [label=\n\"%s\"]", x.blockNum, x.String())
		ret += nodeDecl + "\n"
		last := x.instructions[len(x.instructions)-1]
		if last.typ == "br"{
			ret += fmt.Sprintf("%d -> %s \n", x.blockNum, last.args[0])
		} else if last.typ == "condbr" {
			ret += fmt.Sprintf("%d -> %s [label=true] \n", x.blockNum, last.args[1])
			ret += fmt.Sprintf("%d -> %s [label=false] \n", x.blockNum, last.args[2])
		}
	}
	ret += "}"
	return ret
}