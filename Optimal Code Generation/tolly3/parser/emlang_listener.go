// Code generated from Emlang.g4 by ANTLR 4.12.0. DO NOT EDIT.

package parser // Emlang

import "github.com/antlr/antlr4/runtime/Go/antlr/v4"

// EmlangListener is a complete listener for a parse tree produced by EmlangParser.
type EmlangListener interface {
	antlr.ParseTreeListener

	// EnterStart is called when entering the start production.
	EnterStart(c *StartContext)

	// EnterBlock is called when entering the block production.
	EnterBlock(c *BlockContext)

	// EnterPart is called when entering the part production.
	EnterPart(c *PartContext)

	// EnterDeclaration is called when entering the declaration production.
	EnterDeclaration(c *DeclarationContext)

	// EnterAssignation is called when entering the assignation production.
	EnterAssignation(c *AssignationContext)

	// EnterExpr is called when entering the expr production.
	EnterExpr(c *ExprContext)

	// EnterPexp is called when entering the pexp production.
	EnterPexp(c *PexpContext)

	// EnterIdent is called when entering the ident production.
	EnterIdent(c *IdentContext)

	// EnterNumber is called when entering the number production.
	EnterNumber(c *NumberContext)

	// EnterIfElseStmt is called when entering the ifElseStmt production.
	EnterIfElseStmt(c *IfElseStmtContext)

	// EnterCond is called when entering the cond production.
	EnterCond(c *CondContext)

	// EnterBlock1 is called when entering the block1 production.
	EnterBlock1(c *Block1Context)

	// EnterBlock2 is called when entering the block2 production.
	EnterBlock2(c *Block2Context)

	// EnterWhileStmt is called when entering the whileStmt production.
	EnterWhileStmt(c *WhileStmtContext)

	// EnterWblock is called when entering the wblock production.
	EnterWblock(c *WblockContext)

	// EnterWcond is called when entering the wcond production.
	EnterWcond(c *WcondContext)

	// EnterReturnStmt is called when entering the returnStmt production.
	EnterReturnStmt(c *ReturnStmtContext)

	// EnterLolStmt is called when entering the lolStmt production.
	EnterLolStmt(c *LolStmtContext)

	// ExitStart is called when exiting the start production.
	ExitStart(c *StartContext)

	// ExitBlock is called when exiting the block production.
	ExitBlock(c *BlockContext)

	// ExitPart is called when exiting the part production.
	ExitPart(c *PartContext)

	// ExitDeclaration is called when exiting the declaration production.
	ExitDeclaration(c *DeclarationContext)

	// ExitAssignation is called when exiting the assignation production.
	ExitAssignation(c *AssignationContext)

	// ExitExpr is called when exiting the expr production.
	ExitExpr(c *ExprContext)

	// ExitPexp is called when exiting the pexp production.
	ExitPexp(c *PexpContext)

	// ExitIdent is called when exiting the ident production.
	ExitIdent(c *IdentContext)

	// ExitNumber is called when exiting the number production.
	ExitNumber(c *NumberContext)

	// ExitIfElseStmt is called when exiting the ifElseStmt production.
	ExitIfElseStmt(c *IfElseStmtContext)

	// ExitCond is called when exiting the cond production.
	ExitCond(c *CondContext)

	// ExitBlock1 is called when exiting the block1 production.
	ExitBlock1(c *Block1Context)

	// ExitBlock2 is called when exiting the block2 production.
	ExitBlock2(c *Block2Context)

	// ExitWhileStmt is called when exiting the whileStmt production.
	ExitWhileStmt(c *WhileStmtContext)

	// ExitWblock is called when exiting the wblock production.
	ExitWblock(c *WblockContext)

	// ExitWcond is called when exiting the wcond production.
	ExitWcond(c *WcondContext)

	// ExitReturnStmt is called when exiting the returnStmt production.
	ExitReturnStmt(c *ReturnStmtContext)

	// ExitLolStmt is called when exiting the lolStmt production.
	ExitLolStmt(c *LolStmtContext)
}
