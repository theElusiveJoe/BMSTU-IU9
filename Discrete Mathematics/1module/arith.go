package main

//<E>  ::= <T> <E’>.
//<E’> ::= + <T> <E’> | - <T> <E’> | .
//<T>  ::= <F> <T’>.
//<T’> ::= * <F> <T’> | / <F> <T’> | .
//<F>  ::= <number> | <var> | ( <E> ) | - <F>.

import (
	"fmt"
	"input"
	"strconv"
)

type Tag int

const (
	ERROR  Tag = 1 << iota // Неправильная лексема
	NUMBER                 // Целое число
	VAR                    // Имя переменной
	PLUS                   // Знак +
	MINUS                  // Знак -
	MUL                    // Знак *
	DIV                    // Знак /
	LPAREN                 // Левая круглая скобка
	RPAREN                 // Правая круглая скобка
)

type Lexem struct {
	Tag
	Image string
}

type Var struct {
	val  int
	name string
}

var lexems []Lexem
var lexemslen, lindex int
var tokens []string
var voc []Var
var err bool = false

func getNum(expr string, j int) int {
	var i int
	for i = j; i < len(expr); i++ {
		if !(expr[i] >= 48 && expr[i] <= 57) {
			break
		}
	}
	return i
}

func getVar(expr string, j int) int {
	var i int
	for i = j; i < len(expr); i++ {
		if !((expr[i] >= 48 && expr[i] <= 57) || (expr[i] >= 65 && expr[i] <= 90) || (expr[i] >= 97 && expr[i] <= 122)) {
			break
		}
	}
	return i
}

func lexer(expr string) {
	var lx Lexem
	var leng = len(expr)
	for i := 0; i < leng; i++ {
		lexemslen++
		switch expr[i] {
		case 32:
			lexemslen--
			continue
		case 43:
			lx.Tag = PLUS
			lx.Image = "+"
			lexems = append(lexems, lx)
			break
		case 45:
			lx.Tag = MINUS
			lx.Image = "-"
			lexems = append(lexems, lx)
			break
		case 42:
			lx.Tag = MUL
			lx.Image = "*"
			lexems = append(lexems, lx)
			break
		case 47:
			lx.Tag = DIV
			lx.Image = "/"
			lexems = append(lexems, lx)
			break
		case 40:
			lx.Tag = LPAREN
			lx.Image = "("
			lexems = append(lexems, lx)
			break
		case 41:
			lx.Tag = RPAREN
			lx.Image = ")"
			lexems = append(lexems, lx)
			break
		default:
			if expr[i] >= 48 && expr[i] <= 57 {
				j := getNum(expr, i)
				lx.Tag = NUMBER
				lx.Image = expr[i:j]
				lexems = append(lexems, lx)
				i = j - 1
			} else if (expr[i] >= 65 && expr[i] <= 90) || (expr[i] >= 97 && expr[i] <= 122) {
				j := getVar(expr, i)
				lx.Tag = VAR
				lx.Image = expr[i:j]
				lexems = append(lexems, lx)
				i = j - 1
			} else {
				lx.Tag = ERROR
				lexems = append(lexems, lx)
				err = true
			}
		}
	}
}

func parseE() {
	parseT()
	parseEE()
}

func parseEE() {
	if lexemslen > lindex {
		lx := lexems[lindex]
		if lx.Tag&(PLUS|MINUS) != 0 {
			lindex++
			parseT()
			tokens = append(tokens, lx.Image)
			parseEE()
		} else if (lx.Tag&(VAR|NUMBER)) != 0 {
			err = true
		}
	}
}

func parseT() {
	parseF()
	parseTT()
}

func parseTT() {
	if lexemslen > lindex {
		lx := lexems[lindex]
		if lx.Tag&(DIV|MUL) != 0 {
			lindex++
			parseF()
			tokens = append(tokens, lx.Image)
			parseTT()
		}
	}
}

func parseF() {
	if lexemslen > lindex {
		lx := lexems[lindex]
		if lx.Tag&(NUMBER|VAR) != 0 {
			lindex++
			tokens = append(tokens, lx.Image)
		} else if lx.Tag&MINUS != 0 {
			lindex++
			tokens = append(tokens, "-1")
			parseF()
			tokens = append(tokens, "*")
		} else if lx.Tag&LPAREN != 0 {
			lindex++
			parseE()
			if lexemslen > lindex {
				lx := lexems[lindex]
				lindex++
				if lx.Tag&RPAREN == 0 {
					err = true
				}
			} else {
				err = true
			}
		} else {
			err = true
		}
	} else {
		err = true
	}
}

func getVal(str string) int {
	for _, v := range voc {
		if v.name == str {
			return v.val
		}
	}
	return 0
}

func inVoc(str string) int {
	for _, v := range voc {
		if v.name == str {
			return 1
		}
	}
	return 0
}

func evaller() int {
	stack := []int{}
	for _, t := range tokens{
		if t[0] >= 48 && t[0] <= 57 || (t[0]=='-' && len(t)>1){
			num, _ := strconv.Atoi(t)
			stack = append(stack, num)
		} else if ( t[0] >= 65 &&  t[0] <= 90) || ( t[0] >= 97 &&  t[0] <= 122) {
			num := getVal(t)
			stack = append(stack, num)
		} else {
			switch t {
			case "+":
				stack = append(stack[:len(stack)-2], stack[len(stack)-1] + stack[len(stack)-2])
				break
			case "-":
				stack = append(stack[:len(stack)-2], stack[len(stack)-2] - stack[len(stack)-1])
				break
			case "*":
				stack = append(stack[:len(stack)-2], stack[len(stack)-1] * stack[len(stack)-2])
				break
			case "/":
				if stack[len(stack)-2] == 0{
					stack = append(stack[:len(stack)-2], 0)
				}else {
					stack = append(stack[:len(stack)-2], stack[len(stack)-2]/stack[len(stack)-1])
				}
				break
			}
		}
	}
	return stack[0]
}

func main() {
	expr := input.Gets()
	lexer(expr)
	parseE()
	lindex = len(tokens) - 1
	if err {
		fmt.Println("error")
	} else {
		var x int
		var v Var
		for _, lx := range lexems{
			if lx.Tag & VAR != 0 && inVoc(lx.Image) == 0{
				input.Scanf("%d", &x)
				v.name = lx.Image
				v.val = x
				voc = append(voc, v)
			}
		}
		fmt.Println(evaller())
	}
}