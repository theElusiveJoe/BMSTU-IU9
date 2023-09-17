package parser

// IF ELSE
func (s *MyEmlangListener) EnterIfElseStmt(ctx *IfElseStmtContext) {}
func (s *MyEmlangListener) EnterCond(ctx *CondContext)             {}

// создаем условие на основе последнего выражения
func (s *MyEmlangListener) ExitCond(ctx *CondContext) {
	block2, block1 := s.newBlock(), s.newBlock()
	// передаем область видимости
	block1.setMap(s.getBlock(2))
	block2.setMap(s.getBlock(2))
	cond := s.getBlock(2).newCompare(s.popExpr(), "0")
	s.getBlock(2).newCondBreak(cond, block2, block1)
	s.blocks = append(s.blocks, block1)
	s.blocks = append(s.blocks, block2)
}

func (s *MyEmlangListener) EnterBlock1(ctx *Block1Context) {}
func (s *MyEmlangListener) ExitBlock1(ctx *Block1Context)  {}
func (s *MyEmlangListener) EnterBlock2(ctx *Block2Context) {
	block1, block2 := s.popBlock(), s.popBlock()
	s.pushBlock(block1)
	s.pushBlock(block2)

}
func (s *MyEmlangListener) ExitBlock2(ctx *Block2Context) {}
func (s *MyEmlangListener) ExitIfElseStmt(ctx *IfElseStmtContext) {
	// Сейчас у нас стек блоков выглядит так:
	//[... блок_с_условием, блокThen, блокElse]
	// снимаем блоки
	block2 := s.popBlock()
	block1 := s.popBlock()

	oldBlock := s.popBlock()
	// создаем блок final
	nb := s.newBlock()
	nb.setMap(oldBlock)
	// и прокидываем переходы от блока then и блока else
	if !block1.returned {
		block1.newBreak(nb)
	}
	if !block2.returned {
		block2.newBreak(nb)
	}
	nb.updPhi(block1)
	nb.updPhi(block2)
	// и привязываем новый блок в main
	s.addBlockToMain(nb)
}

// RETURN
func (s *MyEmlangListener) EnterReturnStmt(ctx *ReturnStmtContext) {}
func (s *MyEmlangListener) ExitReturnStmt(ctx *ReturnStmtContext) {
	if s.isCurBlockRetTrue() {
		return
	}
	s.curBlock().newRet(s.popExpr())
	s.setCurBlockRetTrue()

}

// WHILE

func (s *MyEmlangListener) EnterWhileStmt(ctx *WhileStmtContext) {}
func (s *MyEmlangListener) EnterWcond(ctx *WcondContext) {

	// переход в condition block нужно сделать до генерации кода вычисления выражения
	// чтобы условие перехода вычислялось каждый раз
	// при заходе в блок
	baseBlock := s.popBlock()
	cb := s.newBlock()
	cb.setMap(baseBlock)
	s.addBlockToMain(cb)
	baseBlock.newBreak(cb)
	// запоминаем cb в стек, чтобы потом докинуть его при завершении loop block`а
	s.pushwhileCondBlock(cb)
}
func (s *MyEmlangListener) ExitWcond(ctx *WcondContext) {
	cb := s.popBlock()
	// after block
	// loop block - на верхушке стека
	ab := s.newBlock()
	// fmt.Println()
	ab.setMap(cb)
	// ab.block.NewRet(constant.NewInt(types.I32, 0))
	s.addBlockToMain(ab)
	lb := s.newBlock()
	lb.setMap(cb)
	s.addBlockToMain(lb)

	// создаем условный переход
	cond := cb.newCompare(s.popExpr(), "0")
	cb.newCondBreak(cond, ab, lb)
	// cb.block.NewCondBr(cond, ab.block, lb.block)
}
func (s *MyEmlangListener) EnterWblock(ctx *WblockContext) {}
func (s *MyEmlangListener) ExitWblock(ctx *WblockContext) {
	if !s.curBlock().returned {
		s.curBlock().newBreak(s.popwhileCondBlock())
	}
	// выкидываем, чтобы after block стал cur block`ом
	s.popBlock()
}
func (s *MyEmlangListener) ExitWhileStmt(ctx *WhileStmtContext) {
	// fmt.Println("-------------")
	// for _, b := range s.main.Blocks {
	// 	fmt.Println(b.Term)
	// }
}
