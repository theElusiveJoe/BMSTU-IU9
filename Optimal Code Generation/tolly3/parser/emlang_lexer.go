// Code generated from Emlang.g4 by ANTLR 4.12.0. DO NOT EDIT.

package parser

import (
	"fmt"
	"sync"
	"unicode"

	"github.com/antlr/antlr4/runtime/Go/antlr/v4"
)

// Suppress unused import error
var _ = fmt.Printf
var _ = sync.Once{}
var _ = unicode.IsLetter

type EmlangLexer struct {
	*antlr.BaseLexer
	channelNames []string
	modeNames    []string
	// TODO: EOF string
}

var emlanglexerLexerStaticData struct {
	once                   sync.Once
	serializedATN          []int32
	channelNames           []string
	modeNames              []string
	literalNames           []string
	symbolicNames          []string
	ruleNames              []string
	predictionContextCache *antlr.PredictionContextCache
	atn                    *antlr.ATN
	decisionToDFA          []*antlr.DFA
}

func emlanglexerLexerInit() {
	staticData := &emlanglexerLexerStaticData
	staticData.channelNames = []string{
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN",
	}
	staticData.modeNames = []string{
		"DEFAULT_MODE",
	}
	staticData.literalNames = []string{
		"", "'main'", "'{'", "'}'", "'decl'", "';'", "'assign'", "'('", "')'",
		"'if'", "'else'", "'while'", "'return'", "'lol'",
	}
	staticData.symbolicNames = []string{
		"", "", "", "", "", "", "", "", "", "", "", "", "", "", "OP", "NUMBER",
		"WHITESPACE", "IDENT",
	}
	staticData.ruleNames = []string{
		"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8",
		"T__9", "T__10", "T__11", "T__12", "OP", "NUMBER", "WHITESPACE", "IDENT",
	}
	staticData.predictionContextCache = antlr.NewPredictionContextCache()
	staticData.serializedATN = []int32{
		4, 0, 17, 108, 6, -1, 2, 0, 7, 0, 2, 1, 7, 1, 2, 2, 7, 2, 2, 3, 7, 3, 2,
		4, 7, 4, 2, 5, 7, 5, 2, 6, 7, 6, 2, 7, 7, 7, 2, 8, 7, 8, 2, 9, 7, 9, 2,
		10, 7, 10, 2, 11, 7, 11, 2, 12, 7, 12, 2, 13, 7, 13, 2, 14, 7, 14, 2, 15,
		7, 15, 2, 16, 7, 16, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 2, 1,
		2, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 4, 1, 4, 1, 5, 1, 5, 1, 5, 1, 5, 1,
		5, 1, 5, 1, 5, 1, 6, 1, 6, 1, 7, 1, 7, 1, 8, 1, 8, 1, 8, 1, 9, 1, 9, 1,
		9, 1, 9, 1, 9, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 11, 1, 11,
		1, 11, 1, 11, 1, 11, 1, 11, 1, 11, 1, 12, 1, 12, 1, 12, 1, 12, 1, 13, 1,
		13, 1, 14, 4, 14, 91, 8, 14, 11, 14, 12, 14, 92, 1, 15, 4, 15, 96, 8, 15,
		11, 15, 12, 15, 97, 1, 15, 1, 15, 1, 16, 1, 16, 5, 16, 104, 8, 16, 10,
		16, 12, 16, 107, 9, 16, 0, 0, 17, 1, 1, 3, 2, 5, 3, 7, 4, 9, 5, 11, 6,
		13, 7, 15, 8, 17, 9, 19, 10, 21, 11, 23, 12, 25, 13, 27, 14, 29, 15, 31,
		16, 33, 17, 1, 0, 5, 2, 0, 42, 43, 45, 45, 1, 0, 48, 57, 3, 0, 9, 10, 13,
		13, 32, 32, 2, 0, 65, 90, 97, 122, 3, 0, 48, 57, 65, 90, 97, 122, 110,
		0, 1, 1, 0, 0, 0, 0, 3, 1, 0, 0, 0, 0, 5, 1, 0, 0, 0, 0, 7, 1, 0, 0, 0,
		0, 9, 1, 0, 0, 0, 0, 11, 1, 0, 0, 0, 0, 13, 1, 0, 0, 0, 0, 15, 1, 0, 0,
		0, 0, 17, 1, 0, 0, 0, 0, 19, 1, 0, 0, 0, 0, 21, 1, 0, 0, 0, 0, 23, 1, 0,
		0, 0, 0, 25, 1, 0, 0, 0, 0, 27, 1, 0, 0, 0, 0, 29, 1, 0, 0, 0, 0, 31, 1,
		0, 0, 0, 0, 33, 1, 0, 0, 0, 1, 35, 1, 0, 0, 0, 3, 40, 1, 0, 0, 0, 5, 42,
		1, 0, 0, 0, 7, 44, 1, 0, 0, 0, 9, 49, 1, 0, 0, 0, 11, 51, 1, 0, 0, 0, 13,
		58, 1, 0, 0, 0, 15, 60, 1, 0, 0, 0, 17, 62, 1, 0, 0, 0, 19, 65, 1, 0, 0,
		0, 21, 70, 1, 0, 0, 0, 23, 76, 1, 0, 0, 0, 25, 83, 1, 0, 0, 0, 27, 87,
		1, 0, 0, 0, 29, 90, 1, 0, 0, 0, 31, 95, 1, 0, 0, 0, 33, 101, 1, 0, 0, 0,
		35, 36, 5, 109, 0, 0, 36, 37, 5, 97, 0, 0, 37, 38, 5, 105, 0, 0, 38, 39,
		5, 110, 0, 0, 39, 2, 1, 0, 0, 0, 40, 41, 5, 123, 0, 0, 41, 4, 1, 0, 0,
		0, 42, 43, 5, 125, 0, 0, 43, 6, 1, 0, 0, 0, 44, 45, 5, 100, 0, 0, 45, 46,
		5, 101, 0, 0, 46, 47, 5, 99, 0, 0, 47, 48, 5, 108, 0, 0, 48, 8, 1, 0, 0,
		0, 49, 50, 5, 59, 0, 0, 50, 10, 1, 0, 0, 0, 51, 52, 5, 97, 0, 0, 52, 53,
		5, 115, 0, 0, 53, 54, 5, 115, 0, 0, 54, 55, 5, 105, 0, 0, 55, 56, 5, 103,
		0, 0, 56, 57, 5, 110, 0, 0, 57, 12, 1, 0, 0, 0, 58, 59, 5, 40, 0, 0, 59,
		14, 1, 0, 0, 0, 60, 61, 5, 41, 0, 0, 61, 16, 1, 0, 0, 0, 62, 63, 5, 105,
		0, 0, 63, 64, 5, 102, 0, 0, 64, 18, 1, 0, 0, 0, 65, 66, 5, 101, 0, 0, 66,
		67, 5, 108, 0, 0, 67, 68, 5, 115, 0, 0, 68, 69, 5, 101, 0, 0, 69, 20, 1,
		0, 0, 0, 70, 71, 5, 119, 0, 0, 71, 72, 5, 104, 0, 0, 72, 73, 5, 105, 0,
		0, 73, 74, 5, 108, 0, 0, 74, 75, 5, 101, 0, 0, 75, 22, 1, 0, 0, 0, 76,
		77, 5, 114, 0, 0, 77, 78, 5, 101, 0, 0, 78, 79, 5, 116, 0, 0, 79, 80, 5,
		117, 0, 0, 80, 81, 5, 114, 0, 0, 81, 82, 5, 110, 0, 0, 82, 24, 1, 0, 0,
		0, 83, 84, 5, 108, 0, 0, 84, 85, 5, 111, 0, 0, 85, 86, 5, 108, 0, 0, 86,
		26, 1, 0, 0, 0, 87, 88, 7, 0, 0, 0, 88, 28, 1, 0, 0, 0, 89, 91, 7, 1, 0,
		0, 90, 89, 1, 0, 0, 0, 91, 92, 1, 0, 0, 0, 92, 90, 1, 0, 0, 0, 92, 93,
		1, 0, 0, 0, 93, 30, 1, 0, 0, 0, 94, 96, 7, 2, 0, 0, 95, 94, 1, 0, 0, 0,
		96, 97, 1, 0, 0, 0, 97, 95, 1, 0, 0, 0, 97, 98, 1, 0, 0, 0, 98, 99, 1,
		0, 0, 0, 99, 100, 6, 15, 0, 0, 100, 32, 1, 0, 0, 0, 101, 105, 7, 3, 0,
		0, 102, 104, 7, 4, 0, 0, 103, 102, 1, 0, 0, 0, 104, 107, 1, 0, 0, 0, 105,
		103, 1, 0, 0, 0, 105, 106, 1, 0, 0, 0, 106, 34, 1, 0, 0, 0, 107, 105, 1,
		0, 0, 0, 4, 0, 92, 97, 105, 1, 6, 0, 0,
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

// EmlangLexerInit initializes any static state used to implement EmlangLexer. By default the
// static state used to implement the lexer is lazily initialized during the first call to
// NewEmlangLexer(). You can call this function if you wish to initialize the static state ahead
// of time.
func EmlangLexerInit() {
	staticData := &emlanglexerLexerStaticData
	staticData.once.Do(emlanglexerLexerInit)
}

// NewEmlangLexer produces a new lexer instance for the optional input antlr.CharStream.
func NewEmlangLexer(input antlr.CharStream) *EmlangLexer {
	EmlangLexerInit()
	l := new(EmlangLexer)
	l.BaseLexer = antlr.NewBaseLexer(input)
	staticData := &emlanglexerLexerStaticData
	l.Interpreter = antlr.NewLexerATNSimulator(l, staticData.atn, staticData.decisionToDFA, staticData.predictionContextCache)
	l.channelNames = staticData.channelNames
	l.modeNames = staticData.modeNames
	l.RuleNames = staticData.ruleNames
	l.LiteralNames = staticData.literalNames
	l.SymbolicNames = staticData.symbolicNames
	l.GrammarFileName = "Emlang.g4"
	// TODO: l.EOF = antlr.TokenEOF

	return l
}

// EmlangLexer tokens.
const (
	EmlangLexerT__0       = 1
	EmlangLexerT__1       = 2
	EmlangLexerT__2       = 3
	EmlangLexerT__3       = 4
	EmlangLexerT__4       = 5
	EmlangLexerT__5       = 6
	EmlangLexerT__6       = 7
	EmlangLexerT__7       = 8
	EmlangLexerT__8       = 9
	EmlangLexerT__9       = 10
	EmlangLexerT__10      = 11
	EmlangLexerT__11      = 12
	EmlangLexerT__12      = 13
	EmlangLexerOP         = 14
	EmlangLexerNUMBER     = 15
	EmlangLexerWHITESPACE = 16
	EmlangLexerIDENT      = 17
)
