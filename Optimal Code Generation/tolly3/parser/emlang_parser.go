// Code generated from Emlang.g4 by ANTLR 4.12.0. DO NOT EDIT.

package parser // Emlang

import (
	"fmt"
	"strconv"
	"sync"

	"github.com/antlr/antlr4/runtime/Go/antlr/v4"
)

// Suppress unused import errors
var _ = fmt.Printf
var _ = strconv.Itoa
var _ = sync.Once{}

type EmlangParser struct {
	*antlr.BaseParser
}

var emlangParserStaticData struct {
	once                   sync.Once
	serializedATN          []int32
	literalNames           []string
	symbolicNames          []string
	ruleNames              []string
	predictionContextCache *antlr.PredictionContextCache
	atn                    *antlr.ATN
	decisionToDFA          []*antlr.DFA
}

func emlangParserInit() {
	staticData := &emlangParserStaticData
	staticData.literalNames = []string{
		"", "'main'", "'{'", "'}'", "'decl'", "';'", "'assign'", "'('", "')'",
		"'if'", "'else'", "'while'", "'return'", "'lol'",
	}
	staticData.symbolicNames = []string{
		"", "", "", "", "", "", "", "", "", "", "", "", "", "", "OP", "NUMBER",
		"WHITESPACE", "IDENT",
	}
	staticData.ruleNames = []string{
		"start", "block", "part", "declaration", "assignation", "expr", "pexp",
		"ident", "number", "ifElseStmt", "cond", "block1", "block2", "whileStmt",
		"wblock", "wcond", "returnStmt", "lolStmt",
	}
	staticData.predictionContextCache = antlr.NewPredictionContextCache()
	staticData.serializedATN = []int32{
		4, 1, 17, 110, 2, 0, 7, 0, 2, 1, 7, 1, 2, 2, 7, 2, 2, 3, 7, 3, 2, 4, 7,
		4, 2, 5, 7, 5, 2, 6, 7, 6, 2, 7, 7, 7, 2, 8, 7, 8, 2, 9, 7, 9, 2, 10, 7,
		10, 2, 11, 7, 11, 2, 12, 7, 12, 2, 13, 7, 13, 2, 14, 7, 14, 2, 15, 7, 15,
		2, 16, 7, 16, 2, 17, 7, 17, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 5, 1, 43,
		8, 1, 10, 1, 12, 1, 46, 9, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2,
		1, 2, 3, 2, 56, 8, 2, 1, 3, 1, 3, 1, 3, 1, 3, 1, 4, 1, 4, 1, 4, 1, 4, 1,
		4, 1, 5, 1, 5, 1, 5, 3, 5, 70, 8, 5, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6,
		1, 7, 1, 7, 1, 8, 1, 8, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 10, 1, 10,
		1, 11, 1, 11, 1, 12, 1, 12, 1, 13, 1, 13, 1, 13, 1, 13, 1, 14, 1, 14, 1,
		15, 1, 15, 1, 16, 1, 16, 1, 16, 1, 16, 1, 17, 1, 17, 1, 17, 1, 17, 1, 17,
		0, 0, 18, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32,
		34, 0, 0, 99, 0, 36, 1, 0, 0, 0, 2, 40, 1, 0, 0, 0, 4, 55, 1, 0, 0, 0,
		6, 57, 1, 0, 0, 0, 8, 61, 1, 0, 0, 0, 10, 69, 1, 0, 0, 0, 12, 71, 1, 0,
		0, 0, 14, 77, 1, 0, 0, 0, 16, 79, 1, 0, 0, 0, 18, 81, 1, 0, 0, 0, 20, 87,
		1, 0, 0, 0, 22, 89, 1, 0, 0, 0, 24, 91, 1, 0, 0, 0, 26, 93, 1, 0, 0, 0,
		28, 97, 1, 0, 0, 0, 30, 99, 1, 0, 0, 0, 32, 101, 1, 0, 0, 0, 34, 105, 1,
		0, 0, 0, 36, 37, 5, 1, 0, 0, 37, 38, 3, 2, 1, 0, 38, 39, 5, 0, 0, 1, 39,
		1, 1, 0, 0, 0, 40, 44, 5, 2, 0, 0, 41, 43, 3, 4, 2, 0, 42, 41, 1, 0, 0,
		0, 43, 46, 1, 0, 0, 0, 44, 42, 1, 0, 0, 0, 44, 45, 1, 0, 0, 0, 45, 47,
		1, 0, 0, 0, 46, 44, 1, 0, 0, 0, 47, 48, 5, 3, 0, 0, 48, 3, 1, 0, 0, 0,
		49, 56, 3, 6, 3, 0, 50, 56, 3, 8, 4, 0, 51, 56, 3, 18, 9, 0, 52, 56, 3,
		32, 16, 0, 53, 56, 3, 34, 17, 0, 54, 56, 3, 26, 13, 0, 55, 49, 1, 0, 0,
		0, 55, 50, 1, 0, 0, 0, 55, 51, 1, 0, 0, 0, 55, 52, 1, 0, 0, 0, 55, 53,
		1, 0, 0, 0, 55, 54, 1, 0, 0, 0, 56, 5, 1, 0, 0, 0, 57, 58, 5, 4, 0, 0,
		58, 59, 5, 17, 0, 0, 59, 60, 5, 5, 0, 0, 60, 7, 1, 0, 0, 0, 61, 62, 5,
		6, 0, 0, 62, 63, 5, 17, 0, 0, 63, 64, 3, 10, 5, 0, 64, 65, 5, 5, 0, 0,
		65, 9, 1, 0, 0, 0, 66, 70, 3, 14, 7, 0, 67, 70, 3, 16, 8, 0, 68, 70, 3,
		12, 6, 0, 69, 66, 1, 0, 0, 0, 69, 67, 1, 0, 0, 0, 69, 68, 1, 0, 0, 0, 70,
		11, 1, 0, 0, 0, 71, 72, 5, 7, 0, 0, 72, 73, 5, 14, 0, 0, 73, 74, 3, 10,
		5, 0, 74, 75, 3, 10, 5, 0, 75, 76, 5, 8, 0, 0, 76, 13, 1, 0, 0, 0, 77,
		78, 5, 17, 0, 0, 78, 15, 1, 0, 0, 0, 79, 80, 5, 15, 0, 0, 80, 17, 1, 0,
		0, 0, 81, 82, 5, 9, 0, 0, 82, 83, 3, 20, 10, 0, 83, 84, 3, 22, 11, 0, 84,
		85, 5, 10, 0, 0, 85, 86, 3, 24, 12, 0, 86, 19, 1, 0, 0, 0, 87, 88, 3, 10,
		5, 0, 88, 21, 1, 0, 0, 0, 89, 90, 3, 2, 1, 0, 90, 23, 1, 0, 0, 0, 91, 92,
		3, 2, 1, 0, 92, 25, 1, 0, 0, 0, 93, 94, 5, 11, 0, 0, 94, 95, 3, 30, 15,
		0, 95, 96, 3, 28, 14, 0, 96, 27, 1, 0, 0, 0, 97, 98, 3, 2, 1, 0, 98, 29,
		1, 0, 0, 0, 99, 100, 3, 10, 5, 0, 100, 31, 1, 0, 0, 0, 101, 102, 5, 12,
		0, 0, 102, 103, 3, 10, 5, 0, 103, 104, 5, 5, 0, 0, 104, 33, 1, 0, 0, 0,
		105, 106, 5, 13, 0, 0, 106, 107, 3, 10, 5, 0, 107, 108, 5, 5, 0, 0, 108,
		35, 1, 0, 0, 0, 3, 44, 55, 69,
	}
	deserializer := antlr.NewATNDeserializer(nil)
	staticData.atn = deserializer.Deserialize(staticData.serializedATN)
	atn := staticData.atn
	staticData.decisionToDFA = make([]*antlr.DFA, len(atn.DecisionToState))
	decisionToDFA := staticData.decisionToDFA
	for index, state := range atn.DecisionToState {
		decisionToDFA[index] = antlr.NewDFA(state, index)
	}
}

// EmlangParserInit initializes any static state used to implement EmlangParser. By default the
// static state used to implement the parser is lazily initialized during the first call to
// NewEmlangParser(). You can call this function if you wish to initialize the static state ahead
// of time.
func EmlangParserInit() {
	staticData := &emlangParserStaticData
	staticData.once.Do(emlangParserInit)
}

// NewEmlangParser produces a new parser instance for the optional input antlr.TokenStream.
func NewEmlangParser(input antlr.TokenStream) *EmlangParser {
	EmlangParserInit()
	this := new(EmlangParser)
	this.BaseParser = antlr.NewBaseParser(input)
	staticData := &emlangParserStaticData
	this.Interpreter = antlr.NewParserATNSimulator(this, staticData.atn, staticData.decisionToDFA, staticData.predictionContextCache)
	this.RuleNames = staticData.ruleNames
	this.LiteralNames = staticData.literalNames
	this.SymbolicNames = staticData.symbolicNames
	this.GrammarFileName = "Emlang.g4"

	return this
}

// EmlangParser tokens.
const (
	EmlangParserEOF        = antlr.TokenEOF
	EmlangParserT__0       = 1
	EmlangParserT__1       = 2
	EmlangParserT__2       = 3
	EmlangParserT__3       = 4
	EmlangParserT__4       = 5
	EmlangParserT__5       = 6
	EmlangParserT__6       = 7
	EmlangParserT__7       = 8
	EmlangParserT__8       = 9
	EmlangParserT__9       = 10
	EmlangParserT__10      = 11
	EmlangParserT__11      = 12
	EmlangParserT__12      = 13
	EmlangParserOP         = 14
	EmlangParserNUMBER     = 15
	EmlangParserWHITESPACE = 16
	EmlangParserIDENT      = 17
)

// EmlangParser rules.
const (
	EmlangParserRULE_start       = 0
	EmlangParserRULE_block       = 1
	EmlangParserRULE_part        = 2
	EmlangParserRULE_declaration = 3
	EmlangParserRULE_assignation = 4
	EmlangParserRULE_expr        = 5
	EmlangParserRULE_pexp        = 6
	EmlangParserRULE_ident       = 7
	EmlangParserRULE_number      = 8
	EmlangParserRULE_ifElseStmt  = 9
	EmlangParserRULE_cond        = 10
	EmlangParserRULE_block1      = 11
	EmlangParserRULE_block2      = 12
	EmlangParserRULE_whileStmt   = 13
	EmlangParserRULE_wblock      = 14
	EmlangParserRULE_wcond       = 15
	EmlangParserRULE_returnStmt  = 16
	EmlangParserRULE_lolStmt     = 17
)

// IStartContext is an interface to support dynamic dispatch.
type IStartContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	Block() IBlockContext
	EOF() antlr.TerminalNode

	// IsStartContext differentiates from other interfaces.
	IsStartContext()
}

type StartContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyStartContext() *StartContext {
	var p = new(StartContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = EmlangParserRULE_start
	return p
}

func (*StartContext) IsStartContext() {}

func NewStartContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *StartContext {
	var p = new(StartContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = EmlangParserRULE_start

	return p
}

func (s *StartContext) GetParser() antlr.Parser { return s.parser }

func (s *StartContext) Block() IBlockContext {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IBlockContext); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(IBlockContext)
}

func (s *StartContext) EOF() antlr.TerminalNode {
	return s.GetToken(EmlangParserEOF, 0)
}

func (s *StartContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *StartContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *StartContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.EnterStart(s)
	}
}

func (s *StartContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.ExitStart(s)
	}
}

func (p *EmlangParser) Start() (localctx IStartContext) {
	this := p
	_ = this

	localctx = NewStartContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 0, EmlangParserRULE_start)

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(36)
		p.Match(EmlangParserT__0)
	}
	{
		p.SetState(37)
		p.Block()
	}
	{
		p.SetState(38)
		p.Match(EmlangParserEOF)
	}

	return localctx
}

// IBlockContext is an interface to support dynamic dispatch.
type IBlockContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	AllPart() []IPartContext
	Part(i int) IPartContext

	// IsBlockContext differentiates from other interfaces.
	IsBlockContext()
}

type BlockContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyBlockContext() *BlockContext {
	var p = new(BlockContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = EmlangParserRULE_block
	return p
}

func (*BlockContext) IsBlockContext() {}

func NewBlockContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *BlockContext {
	var p = new(BlockContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = EmlangParserRULE_block

	return p
}

func (s *BlockContext) GetParser() antlr.Parser { return s.parser }

func (s *BlockContext) AllPart() []IPartContext {
	children := s.GetChildren()
	len := 0
	for _, ctx := range children {
		if _, ok := ctx.(IPartContext); ok {
			len++
		}
	}

	tst := make([]IPartContext, len)
	i := 0
	for _, ctx := range children {
		if t, ok := ctx.(IPartContext); ok {
			tst[i] = t.(IPartContext)
			i++
		}
	}

	return tst
}

func (s *BlockContext) Part(i int) IPartContext {
	var t antlr.RuleContext
	j := 0
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IPartContext); ok {
			if j == i {
				t = ctx.(antlr.RuleContext)
				break
			}
			j++
		}
	}

	if t == nil {
		return nil
	}

	return t.(IPartContext)
}

func (s *BlockContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *BlockContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *BlockContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.EnterBlock(s)
	}
}

func (s *BlockContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.ExitBlock(s)
	}
}

func (p *EmlangParser) Block() (localctx IBlockContext) {
	this := p
	_ = this

	localctx = NewBlockContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 2, EmlangParserRULE_block)
	var _la int

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(40)
		p.Match(EmlangParserT__1)
	}
	p.SetState(44)
	p.GetErrorHandler().Sync(p)
	_la = p.GetTokenStream().LA(1)

	for (int64(_la) & ^0x3f) == 0 && ((int64(1)<<_la)&14928) != 0 {
		{
			p.SetState(41)
			p.Part()
		}

		p.SetState(46)
		p.GetErrorHandler().Sync(p)
		_la = p.GetTokenStream().LA(1)
	}
	{
		p.SetState(47)
		p.Match(EmlangParserT__2)
	}

	return localctx
}

// IPartContext is an interface to support dynamic dispatch.
type IPartContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	Declaration() IDeclarationContext
	Assignation() IAssignationContext
	IfElseStmt() IIfElseStmtContext
	ReturnStmt() IReturnStmtContext
	LolStmt() ILolStmtContext
	WhileStmt() IWhileStmtContext

	// IsPartContext differentiates from other interfaces.
	IsPartContext()
}

type PartContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyPartContext() *PartContext {
	var p = new(PartContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = EmlangParserRULE_part
	return p
}

func (*PartContext) IsPartContext() {}

func NewPartContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *PartContext {
	var p = new(PartContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = EmlangParserRULE_part

	return p
}

func (s *PartContext) GetParser() antlr.Parser { return s.parser }

func (s *PartContext) Declaration() IDeclarationContext {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IDeclarationContext); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(IDeclarationContext)
}

func (s *PartContext) Assignation() IAssignationContext {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IAssignationContext); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(IAssignationContext)
}

func (s *PartContext) IfElseStmt() IIfElseStmtContext {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IIfElseStmtContext); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(IIfElseStmtContext)
}

func (s *PartContext) ReturnStmt() IReturnStmtContext {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IReturnStmtContext); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(IReturnStmtContext)
}

func (s *PartContext) LolStmt() ILolStmtContext {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(ILolStmtContext); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(ILolStmtContext)
}

func (s *PartContext) WhileStmt() IWhileStmtContext {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IWhileStmtContext); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(IWhileStmtContext)
}

func (s *PartContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *PartContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *PartContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.EnterPart(s)
	}
}

func (s *PartContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.ExitPart(s)
	}
}

func (p *EmlangParser) Part() (localctx IPartContext) {
	this := p
	_ = this

	localctx = NewPartContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 4, EmlangParserRULE_part)

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.SetState(55)
	p.GetErrorHandler().Sync(p)

	switch p.GetTokenStream().LA(1) {
	case EmlangParserT__3:
		p.EnterOuterAlt(localctx, 1)
		{
			p.SetState(49)
			p.Declaration()
		}

	case EmlangParserT__5:
		p.EnterOuterAlt(localctx, 2)
		{
			p.SetState(50)
			p.Assignation()
		}

	case EmlangParserT__8:
		p.EnterOuterAlt(localctx, 3)
		{
			p.SetState(51)
			p.IfElseStmt()
		}

	case EmlangParserT__11:
		p.EnterOuterAlt(localctx, 4)
		{
			p.SetState(52)
			p.ReturnStmt()
		}

	case EmlangParserT__12:
		p.EnterOuterAlt(localctx, 5)
		{
			p.SetState(53)
			p.LolStmt()
		}

	case EmlangParserT__10:
		p.EnterOuterAlt(localctx, 6)
		{
			p.SetState(54)
			p.WhileStmt()
		}

	default:
		panic(antlr.NewNoViableAltException(p, nil, nil, nil, nil, nil))
	}

	return localctx
}

// IDeclarationContext is an interface to support dynamic dispatch.
type IDeclarationContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	IDENT() antlr.TerminalNode

	// IsDeclarationContext differentiates from other interfaces.
	IsDeclarationContext()
}

type DeclarationContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyDeclarationContext() *DeclarationContext {
	var p = new(DeclarationContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = EmlangParserRULE_declaration
	return p
}

func (*DeclarationContext) IsDeclarationContext() {}

func NewDeclarationContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *DeclarationContext {
	var p = new(DeclarationContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = EmlangParserRULE_declaration

	return p
}

func (s *DeclarationContext) GetParser() antlr.Parser { return s.parser }

func (s *DeclarationContext) IDENT() antlr.TerminalNode {
	return s.GetToken(EmlangParserIDENT, 0)
}

func (s *DeclarationContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *DeclarationContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *DeclarationContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.EnterDeclaration(s)
	}
}

func (s *DeclarationContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.ExitDeclaration(s)
	}
}

func (p *EmlangParser) Declaration() (localctx IDeclarationContext) {
	this := p
	_ = this

	localctx = NewDeclarationContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 6, EmlangParserRULE_declaration)

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(57)
		p.Match(EmlangParserT__3)
	}
	{
		p.SetState(58)
		p.Match(EmlangParserIDENT)
	}
	{
		p.SetState(59)
		p.Match(EmlangParserT__4)
	}

	return localctx
}

// IAssignationContext is an interface to support dynamic dispatch.
type IAssignationContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	IDENT() antlr.TerminalNode
	Expr() IExprContext

	// IsAssignationContext differentiates from other interfaces.
	IsAssignationContext()
}

type AssignationContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyAssignationContext() *AssignationContext {
	var p = new(AssignationContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = EmlangParserRULE_assignation
	return p
}

func (*AssignationContext) IsAssignationContext() {}

func NewAssignationContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *AssignationContext {
	var p = new(AssignationContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = EmlangParserRULE_assignation

	return p
}

func (s *AssignationContext) GetParser() antlr.Parser { return s.parser }

func (s *AssignationContext) IDENT() antlr.TerminalNode {
	return s.GetToken(EmlangParserIDENT, 0)
}

func (s *AssignationContext) Expr() IExprContext {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IExprContext); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(IExprContext)
}

func (s *AssignationContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *AssignationContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *AssignationContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.EnterAssignation(s)
	}
}

func (s *AssignationContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.ExitAssignation(s)
	}
}

func (p *EmlangParser) Assignation() (localctx IAssignationContext) {
	this := p
	_ = this

	localctx = NewAssignationContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 8, EmlangParserRULE_assignation)

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(61)
		p.Match(EmlangParserT__5)
	}
	{
		p.SetState(62)
		p.Match(EmlangParserIDENT)
	}
	{
		p.SetState(63)
		p.Expr()
	}
	{
		p.SetState(64)
		p.Match(EmlangParserT__4)
	}

	return localctx
}

// IExprContext is an interface to support dynamic dispatch.
type IExprContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	Ident() IIdentContext
	Number() INumberContext
	Pexp() IPexpContext

	// IsExprContext differentiates from other interfaces.
	IsExprContext()
}

type ExprContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyExprContext() *ExprContext {
	var p = new(ExprContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = EmlangParserRULE_expr
	return p
}

func (*ExprContext) IsExprContext() {}

func NewExprContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *ExprContext {
	var p = new(ExprContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = EmlangParserRULE_expr

	return p
}

func (s *ExprContext) GetParser() antlr.Parser { return s.parser }

func (s *ExprContext) Ident() IIdentContext {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IIdentContext); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(IIdentContext)
}

func (s *ExprContext) Number() INumberContext {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(INumberContext); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(INumberContext)
}

func (s *ExprContext) Pexp() IPexpContext {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IPexpContext); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(IPexpContext)
}

func (s *ExprContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *ExprContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *ExprContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.EnterExpr(s)
	}
}

func (s *ExprContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.ExitExpr(s)
	}
}

func (p *EmlangParser) Expr() (localctx IExprContext) {
	this := p
	_ = this

	localctx = NewExprContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 10, EmlangParserRULE_expr)

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.SetState(69)
	p.GetErrorHandler().Sync(p)

	switch p.GetTokenStream().LA(1) {
	case EmlangParserIDENT:
		p.EnterOuterAlt(localctx, 1)
		{
			p.SetState(66)
			p.Ident()
		}

	case EmlangParserNUMBER:
		p.EnterOuterAlt(localctx, 2)
		{
			p.SetState(67)
			p.Number()
		}

	case EmlangParserT__6:
		p.EnterOuterAlt(localctx, 3)
		{
			p.SetState(68)
			p.Pexp()
		}

	default:
		panic(antlr.NewNoViableAltException(p, nil, nil, nil, nil, nil))
	}

	return localctx
}

// IPexpContext is an interface to support dynamic dispatch.
type IPexpContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	OP() antlr.TerminalNode
	AllExpr() []IExprContext
	Expr(i int) IExprContext

	// IsPexpContext differentiates from other interfaces.
	IsPexpContext()
}

type PexpContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyPexpContext() *PexpContext {
	var p = new(PexpContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = EmlangParserRULE_pexp
	return p
}

func (*PexpContext) IsPexpContext() {}

func NewPexpContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *PexpContext {
	var p = new(PexpContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = EmlangParserRULE_pexp

	return p
}

func (s *PexpContext) GetParser() antlr.Parser { return s.parser }

func (s *PexpContext) OP() antlr.TerminalNode {
	return s.GetToken(EmlangParserOP, 0)
}

func (s *PexpContext) AllExpr() []IExprContext {
	children := s.GetChildren()
	len := 0
	for _, ctx := range children {
		if _, ok := ctx.(IExprContext); ok {
			len++
		}
	}

	tst := make([]IExprContext, len)
	i := 0
	for _, ctx := range children {
		if t, ok := ctx.(IExprContext); ok {
			tst[i] = t.(IExprContext)
			i++
		}
	}

	return tst
}

func (s *PexpContext) Expr(i int) IExprContext {
	var t antlr.RuleContext
	j := 0
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IExprContext); ok {
			if j == i {
				t = ctx.(antlr.RuleContext)
				break
			}
			j++
		}
	}

	if t == nil {
		return nil
	}

	return t.(IExprContext)
}

func (s *PexpContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *PexpContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *PexpContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.EnterPexp(s)
	}
}

func (s *PexpContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.ExitPexp(s)
	}
}

func (p *EmlangParser) Pexp() (localctx IPexpContext) {
	this := p
	_ = this

	localctx = NewPexpContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 12, EmlangParserRULE_pexp)

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(71)
		p.Match(EmlangParserT__6)
	}
	{
		p.SetState(72)
		p.Match(EmlangParserOP)
	}
	{
		p.SetState(73)
		p.Expr()
	}
	{
		p.SetState(74)
		p.Expr()
	}
	{
		p.SetState(75)
		p.Match(EmlangParserT__7)
	}

	return localctx
}

// IIdentContext is an interface to support dynamic dispatch.
type IIdentContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	IDENT() antlr.TerminalNode

	// IsIdentContext differentiates from other interfaces.
	IsIdentContext()
}

type IdentContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyIdentContext() *IdentContext {
	var p = new(IdentContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = EmlangParserRULE_ident
	return p
}

func (*IdentContext) IsIdentContext() {}

func NewIdentContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *IdentContext {
	var p = new(IdentContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = EmlangParserRULE_ident

	return p
}

func (s *IdentContext) GetParser() antlr.Parser { return s.parser }

func (s *IdentContext) IDENT() antlr.TerminalNode {
	return s.GetToken(EmlangParserIDENT, 0)
}

func (s *IdentContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *IdentContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *IdentContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.EnterIdent(s)
	}
}

func (s *IdentContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.ExitIdent(s)
	}
}

func (p *EmlangParser) Ident() (localctx IIdentContext) {
	this := p
	_ = this

	localctx = NewIdentContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 14, EmlangParserRULE_ident)

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(77)
		p.Match(EmlangParserIDENT)
	}

	return localctx
}

// INumberContext is an interface to support dynamic dispatch.
type INumberContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	NUMBER() antlr.TerminalNode

	// IsNumberContext differentiates from other interfaces.
	IsNumberContext()
}

type NumberContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyNumberContext() *NumberContext {
	var p = new(NumberContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = EmlangParserRULE_number
	return p
}

func (*NumberContext) IsNumberContext() {}

func NewNumberContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *NumberContext {
	var p = new(NumberContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = EmlangParserRULE_number

	return p
}

func (s *NumberContext) GetParser() antlr.Parser { return s.parser }

func (s *NumberContext) NUMBER() antlr.TerminalNode {
	return s.GetToken(EmlangParserNUMBER, 0)
}

func (s *NumberContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *NumberContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *NumberContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.EnterNumber(s)
	}
}

func (s *NumberContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.ExitNumber(s)
	}
}

func (p *EmlangParser) Number() (localctx INumberContext) {
	this := p
	_ = this

	localctx = NewNumberContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 16, EmlangParserRULE_number)

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(79)
		p.Match(EmlangParserNUMBER)
	}

	return localctx
}

// IIfElseStmtContext is an interface to support dynamic dispatch.
type IIfElseStmtContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	Cond() ICondContext
	Block1() IBlock1Context
	Block2() IBlock2Context

	// IsIfElseStmtContext differentiates from other interfaces.
	IsIfElseStmtContext()
}

type IfElseStmtContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyIfElseStmtContext() *IfElseStmtContext {
	var p = new(IfElseStmtContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = EmlangParserRULE_ifElseStmt
	return p
}

func (*IfElseStmtContext) IsIfElseStmtContext() {}

func NewIfElseStmtContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *IfElseStmtContext {
	var p = new(IfElseStmtContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = EmlangParserRULE_ifElseStmt

	return p
}

func (s *IfElseStmtContext) GetParser() antlr.Parser { return s.parser }

func (s *IfElseStmtContext) Cond() ICondContext {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(ICondContext); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(ICondContext)
}

func (s *IfElseStmtContext) Block1() IBlock1Context {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IBlock1Context); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(IBlock1Context)
}

func (s *IfElseStmtContext) Block2() IBlock2Context {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IBlock2Context); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(IBlock2Context)
}

func (s *IfElseStmtContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *IfElseStmtContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *IfElseStmtContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.EnterIfElseStmt(s)
	}
}

func (s *IfElseStmtContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.ExitIfElseStmt(s)
	}
}

func (p *EmlangParser) IfElseStmt() (localctx IIfElseStmtContext) {
	this := p
	_ = this

	localctx = NewIfElseStmtContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 18, EmlangParserRULE_ifElseStmt)

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(81)
		p.Match(EmlangParserT__8)
	}
	{
		p.SetState(82)
		p.Cond()
	}
	{
		p.SetState(83)
		p.Block1()
	}
	{
		p.SetState(84)
		p.Match(EmlangParserT__9)
	}
	{
		p.SetState(85)
		p.Block2()
	}

	return localctx
}

// ICondContext is an interface to support dynamic dispatch.
type ICondContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	Expr() IExprContext

	// IsCondContext differentiates from other interfaces.
	IsCondContext()
}

type CondContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyCondContext() *CondContext {
	var p = new(CondContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = EmlangParserRULE_cond
	return p
}

func (*CondContext) IsCondContext() {}

func NewCondContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *CondContext {
	var p = new(CondContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = EmlangParserRULE_cond

	return p
}

func (s *CondContext) GetParser() antlr.Parser { return s.parser }

func (s *CondContext) Expr() IExprContext {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IExprContext); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(IExprContext)
}

func (s *CondContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *CondContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *CondContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.EnterCond(s)
	}
}

func (s *CondContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.ExitCond(s)
	}
}

func (p *EmlangParser) Cond() (localctx ICondContext) {
	this := p
	_ = this

	localctx = NewCondContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 20, EmlangParserRULE_cond)

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(87)
		p.Expr()
	}

	return localctx
}

// IBlock1Context is an interface to support dynamic dispatch.
type IBlock1Context interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	Block() IBlockContext

	// IsBlock1Context differentiates from other interfaces.
	IsBlock1Context()
}

type Block1Context struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyBlock1Context() *Block1Context {
	var p = new(Block1Context)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = EmlangParserRULE_block1
	return p
}

func (*Block1Context) IsBlock1Context() {}

func NewBlock1Context(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *Block1Context {
	var p = new(Block1Context)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = EmlangParserRULE_block1

	return p
}

func (s *Block1Context) GetParser() antlr.Parser { return s.parser }

func (s *Block1Context) Block() IBlockContext {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IBlockContext); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(IBlockContext)
}

func (s *Block1Context) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *Block1Context) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *Block1Context) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.EnterBlock1(s)
	}
}

func (s *Block1Context) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.ExitBlock1(s)
	}
}

func (p *EmlangParser) Block1() (localctx IBlock1Context) {
	this := p
	_ = this

	localctx = NewBlock1Context(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 22, EmlangParserRULE_block1)

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(89)
		p.Block()
	}

	return localctx
}

// IBlock2Context is an interface to support dynamic dispatch.
type IBlock2Context interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	Block() IBlockContext

	// IsBlock2Context differentiates from other interfaces.
	IsBlock2Context()
}

type Block2Context struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyBlock2Context() *Block2Context {
	var p = new(Block2Context)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = EmlangParserRULE_block2
	return p
}

func (*Block2Context) IsBlock2Context() {}

func NewBlock2Context(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *Block2Context {
	var p = new(Block2Context)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = EmlangParserRULE_block2

	return p
}

func (s *Block2Context) GetParser() antlr.Parser { return s.parser }

func (s *Block2Context) Block() IBlockContext {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IBlockContext); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(IBlockContext)
}

func (s *Block2Context) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *Block2Context) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *Block2Context) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.EnterBlock2(s)
	}
}

func (s *Block2Context) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.ExitBlock2(s)
	}
}

func (p *EmlangParser) Block2() (localctx IBlock2Context) {
	this := p
	_ = this

	localctx = NewBlock2Context(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 24, EmlangParserRULE_block2)

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(91)
		p.Block()
	}

	return localctx
}

// IWhileStmtContext is an interface to support dynamic dispatch.
type IWhileStmtContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	Wcond() IWcondContext
	Wblock() IWblockContext

	// IsWhileStmtContext differentiates from other interfaces.
	IsWhileStmtContext()
}

type WhileStmtContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyWhileStmtContext() *WhileStmtContext {
	var p = new(WhileStmtContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = EmlangParserRULE_whileStmt
	return p
}

func (*WhileStmtContext) IsWhileStmtContext() {}

func NewWhileStmtContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *WhileStmtContext {
	var p = new(WhileStmtContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = EmlangParserRULE_whileStmt

	return p
}

func (s *WhileStmtContext) GetParser() antlr.Parser { return s.parser }

func (s *WhileStmtContext) Wcond() IWcondContext {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IWcondContext); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(IWcondContext)
}

func (s *WhileStmtContext) Wblock() IWblockContext {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IWblockContext); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(IWblockContext)
}

func (s *WhileStmtContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *WhileStmtContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *WhileStmtContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.EnterWhileStmt(s)
	}
}

func (s *WhileStmtContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.ExitWhileStmt(s)
	}
}

func (p *EmlangParser) WhileStmt() (localctx IWhileStmtContext) {
	this := p
	_ = this

	localctx = NewWhileStmtContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 26, EmlangParserRULE_whileStmt)

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(93)
		p.Match(EmlangParserT__10)
	}
	{
		p.SetState(94)
		p.Wcond()
	}
	{
		p.SetState(95)
		p.Wblock()
	}

	return localctx
}

// IWblockContext is an interface to support dynamic dispatch.
type IWblockContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	Block() IBlockContext

	// IsWblockContext differentiates from other interfaces.
	IsWblockContext()
}

type WblockContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyWblockContext() *WblockContext {
	var p = new(WblockContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = EmlangParserRULE_wblock
	return p
}

func (*WblockContext) IsWblockContext() {}

func NewWblockContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *WblockContext {
	var p = new(WblockContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = EmlangParserRULE_wblock

	return p
}

func (s *WblockContext) GetParser() antlr.Parser { return s.parser }

func (s *WblockContext) Block() IBlockContext {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IBlockContext); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(IBlockContext)
}

func (s *WblockContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *WblockContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *WblockContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.EnterWblock(s)
	}
}

func (s *WblockContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.ExitWblock(s)
	}
}

func (p *EmlangParser) Wblock() (localctx IWblockContext) {
	this := p
	_ = this

	localctx = NewWblockContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 28, EmlangParserRULE_wblock)

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(97)
		p.Block()
	}

	return localctx
}

// IWcondContext is an interface to support dynamic dispatch.
type IWcondContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	Expr() IExprContext

	// IsWcondContext differentiates from other interfaces.
	IsWcondContext()
}

type WcondContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyWcondContext() *WcondContext {
	var p = new(WcondContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = EmlangParserRULE_wcond
	return p
}

func (*WcondContext) IsWcondContext() {}

func NewWcondContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *WcondContext {
	var p = new(WcondContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = EmlangParserRULE_wcond

	return p
}

func (s *WcondContext) GetParser() antlr.Parser { return s.parser }

func (s *WcondContext) Expr() IExprContext {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IExprContext); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(IExprContext)
}

func (s *WcondContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *WcondContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *WcondContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.EnterWcond(s)
	}
}

func (s *WcondContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.ExitWcond(s)
	}
}

func (p *EmlangParser) Wcond() (localctx IWcondContext) {
	this := p
	_ = this

	localctx = NewWcondContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 30, EmlangParserRULE_wcond)

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(99)
		p.Expr()
	}

	return localctx
}

// IReturnStmtContext is an interface to support dynamic dispatch.
type IReturnStmtContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	Expr() IExprContext

	// IsReturnStmtContext differentiates from other interfaces.
	IsReturnStmtContext()
}

type ReturnStmtContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyReturnStmtContext() *ReturnStmtContext {
	var p = new(ReturnStmtContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = EmlangParserRULE_returnStmt
	return p
}

func (*ReturnStmtContext) IsReturnStmtContext() {}

func NewReturnStmtContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *ReturnStmtContext {
	var p = new(ReturnStmtContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = EmlangParserRULE_returnStmt

	return p
}

func (s *ReturnStmtContext) GetParser() antlr.Parser { return s.parser }

func (s *ReturnStmtContext) Expr() IExprContext {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IExprContext); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(IExprContext)
}

func (s *ReturnStmtContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *ReturnStmtContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *ReturnStmtContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.EnterReturnStmt(s)
	}
}

func (s *ReturnStmtContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.ExitReturnStmt(s)
	}
}

func (p *EmlangParser) ReturnStmt() (localctx IReturnStmtContext) {
	this := p
	_ = this

	localctx = NewReturnStmtContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 32, EmlangParserRULE_returnStmt)

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(101)
		p.Match(EmlangParserT__11)
	}
	{
		p.SetState(102)
		p.Expr()
	}
	{
		p.SetState(103)
		p.Match(EmlangParserT__4)
	}

	return localctx
}

// ILolStmtContext is an interface to support dynamic dispatch.
type ILolStmtContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// Getter signatures
	Expr() IExprContext

	// IsLolStmtContext differentiates from other interfaces.
	IsLolStmtContext()
}

type LolStmtContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyLolStmtContext() *LolStmtContext {
	var p = new(LolStmtContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = EmlangParserRULE_lolStmt
	return p
}

func (*LolStmtContext) IsLolStmtContext() {}

func NewLolStmtContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *LolStmtContext {
	var p = new(LolStmtContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = EmlangParserRULE_lolStmt

	return p
}

func (s *LolStmtContext) GetParser() antlr.Parser { return s.parser }

func (s *LolStmtContext) Expr() IExprContext {
	var t antlr.RuleContext
	for _, ctx := range s.GetChildren() {
		if _, ok := ctx.(IExprContext); ok {
			t = ctx.(antlr.RuleContext)
			break
		}
	}

	if t == nil {
		return nil
	}

	return t.(IExprContext)
}

func (s *LolStmtContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *LolStmtContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *LolStmtContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.EnterLolStmt(s)
	}
}

func (s *LolStmtContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(EmlangListener); ok {
		listenerT.ExitLolStmt(s)
	}
}

func (p *EmlangParser) LolStmt() (localctx ILolStmtContext) {
	this := p
	_ = this

	localctx = NewLolStmtContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 34, EmlangParserRULE_lolStmt)

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(105)
		p.Match(EmlangParserT__12)
	}
	{
		p.SetState(106)
		p.Expr()
	}
	{
		p.SetState(107)
		p.Match(EmlangParserT__4)
	}

	return localctx
}
