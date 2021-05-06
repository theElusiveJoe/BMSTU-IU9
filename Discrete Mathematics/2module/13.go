//<formula> ::= <left> = <right>
//
//<left ::= <ident> <endident>
//<endident ::= , <ident> <endident> | .
//
//<right> ::= <arith> <endright>
//<endright> ::= , <arith> <endright> | .

//<arith> ::= <term> <end_arith>
//<end_arith> ::= + <term> <end_arith> | - <term> <end_arith> | .
//<term> ::= <factor> <end_term>
//<end_term> ::= * <factor> <end_term> | / <factor> <end_term> | .
//<factor> ::= <number>  | ( <arith> ) | - <factor> | <ident>

// каждая формула представляет собой множество односторонних зависимостей
//одной переменной от других.
// поэтому после синтаксического анализа формулы,
//от неё должны остаться лишь пары переменная - множество переменных, от которых она зависит

package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	//"time"
)

type lexem struct {
	name    string
	content string
}

// для парсера
var lexems []lexem // временная штука для лексического анализа отдельной строки
var lindex int
var m map[string]int
var mm map[int]int
var define []int
var usedIn []int
// как все это хранить?
// создаем массив множеств односторонних зависимостей - formulas
// каждое множество этого массива - pairs
// элемент этого множества - структура pair

var formulas [][]pair
var pairs []pair // временная штука для синтаксического анализа отдельной строки
var lcount, rcount int

type pair struct {
	left  string
	right []string
}

// для графов

var tim = 0
var count = 0
type vertex struct {
	number    int
	formula string
	edges   []int
	usedIn  []int
	define  []int
	color   int
	time    int
}
var vertexList []vertex

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
	_, ok := m[expr[j:i]]
	if !ok{
		m[expr[j:i]] = count
		count++
	}

	return i
}

func exitwitherr() {
	fmt.Println("syntax error")
	os.Exit(0)
}

func lexer(program string) {
	leng := len(program)
	var lx lexem
	lexems = make([]lexem, 0)
	for i := 0; i < leng; i++ {
		switch program[i] {
		case ' ':
			break
		case '-':
			lx.name = "-"
			lx.content = "-"
			lexems = append(lexems, lx)
			break
		case '+':
			lx.name = "+"
			lx.content = "+"
			lexems = append(lexems, lx)
			break
		case '*':
			lx.name = "*"
			lx.content = "*"
			lexems = append(lexems, lx)
			break
		case '/':
			lx.name = "/"
			lx.content = "/"
			lexems = append(lexems, lx)
			break
		case '(':
			lx.name = "("
			lx.content = "("
			lexems = append(lexems, lx)
			break
		case ')':
			lx.name = ")"
			lx.content = ")"
			lexems = append(lexems, lx)
			break
		case ',':
			lx.name = ","
			lx.content = ","
			lexems = append(lexems, lx)
			break
		case '=':
			lx.name = "="
			lx.content = "="
			lexems = append(lexems, lx)
		default:
			if program[i] >= 48 && program[i] <= 57 {
				j := getNum(program, i)
				lx.name = "number"
				lx.content = program[i:j]
				lexems = append(lexems, lx)
				i = j - 1
			} else if (program[i] >= 65 && program[i] <= 90) || (program[i] >= 97 && program[i] <= 122) {
				j := getVar(program, i)
				lx.name = "ident"
				lx.content = program[i:j]
				lexems = append(lexems, lx)
				i = j - 1
			} else {
				exitwitherr()
			}
		}
	}
}

//<formula> ::= <left> = <right>
func parse_formula() {
	lindex = 0
	pairs = make([]pair, 0)
	lcount, rcount = 0, 0

	parse_left()

	if lindex < len(lexems) && lexems[lindex].name == "=" {
		lindex++
	} else {
		exitwitherr()
	}
	parse_right()

	if lcount != rcount || lindex < len(lexems){
		exitwitherr()
	}
	formulas = append(formulas, pairs)

}

func parse_left() {
	if lindex < len(lexems) && lexems[lindex].name == "ident" {
		var p pair
		p.left = lexems[lindex].content
		define = append(define, m[lexems[lindex].content])
		p.right = make([]string, 0)
		pairs = append(pairs, p)
		lindex++
	} else {

		exitwitherr()
	}

	parse_end_left()
}

func parse_end_left() {
	if lindex < len(lexems) && lexems[lindex].name == "," {
		lindex++
		lcount++
		if lindex < len(lexems) && lexems[lindex].name == "ident" {
			var p pair
			p.left = lexems[lindex].content
			define = append(define, m[lexems[lindex].content])
			p.right = make([]string, 0)
			pairs = append(pairs, p)
			lindex++
		} else {
			exitwitherr()
		}

		parse_end_left()
	}
}

func parse_right() {
	parse_arith()
	parse_end_right()
}

func parse_end_right() {
	if lindex < len(lexems) && lexems[lindex].name == "," {
		lindex++
		rcount++
		parse_arith()
		parse_end_right()
	}
}

//<arith_expr> ::= <term> <end-arith_expr>
func parse_arith() {
	parse_term()
	parse_end_arith()
}

//<end-arith_expr> ::= + <term> <end-arith_expr> | - <term> <end-arith_expr> | .
func parse_end_arith() {
	if lindex < len(lexems) && (lexems[lindex].content == "+" || lexems[lindex].content == "-") {
		////fmt.Println("found ", lexems[lindex].content)
		lindex++
		parse_term()
		parse_end_arith()
	}
}

//<term> ::= <factor> <end-term>
func parse_term() {
	parse_factor()
	parse_end_term()
}

//<end-term> ::= * <factor> <end-term> | / <factor> <end-term> | .
func parse_end_term() {
	if lindex < len(lexems) && ((lexems[lindex].content == "*" || lexems[lindex].content == "/")) {
		////fmt.Println("found ", lexems[lindex].content)
		lindex++
		parse_factor()
		parse_end_term()
	}
}

//<factor> ::= <number>  | ( <expr> ) | - <factor> | <ident>
func parse_factor() {
	if lindex < len(lexems) && lexems[lindex].name == "number" {
		////fmt.Println("found number: ", lexems[lindex].content)
		lindex++
	} else if lindex < len(lexems) && lexems[lindex].content == "(" {
		////fmt.Println("found (")
		lindex++
		parse_arith()
		if lindex >=  len(lexems) || lindex < len(lexems) && lexems[lindex].content != ")" {
			////fmt.Println("foundparse_factor  - expected )")
			exitwitherr()
		}
		////fmt.Println("found )")
		lindex++
	} else if lindex < len(lexems) && lexems[lindex].content == "-" {
		////fmt.Println("found -")
		lindex++
		parse_factor()
	} else if lindex < len(lexems) && lexems[lindex].name == "ident" {
		usedIn = append(usedIn, m[lexems[lindex].content])
		pairs[rcount].right = append(pairs[rcount].right, lexems[lindex].content)
		lindex++
	} else {
		exitwitherr()
	}
}

func isIn(str string, arr []string) bool {
	for _, x := range arr {
		if x == str {
			return true
		}
	}
	return false
}

func isSubset(arr1 []string, arr2 []string) bool {
	for _, x := range arr1 {
		if !isIn(x, arr2) {
			return false
		}
	}
	return true
}

func isIn2(str int, arr []int) bool {
	for _, x := range arr {
		if x == str {
			return true
		}
	}
	return false
}

func intersect(arr1 []int, arr2 []int) bool {
	for _, x := range arr1 {
		if isIn2(x, arr2) {
			return true
		}
	}
	return false
}

func DFS(vertexList *[]vertex)  {
	for i, _ := range *vertexList {
		if (*vertexList)[i].color == 0 {
			visitVertex(vertexList, i)
		}
		if (*vertexList)[i].color == 1 {
			fmt.Println("cycle")
			os.Exit(0)
		}
	}
}

func visitVertex(vertexList *[]vertex, v int)  {
	(*vertexList)[v].color = 1
	for _, e := range (*vertexList)[v].edges {
		if (*vertexList)[e].color == 0 {
			visitVertex(vertexList, e)
		}
		if (*vertexList)[e].color == 1 {
			fmt.Println("cycle")
			os.Exit(0)
		}
	}
	(*vertexList)[v].time = tim
	tim++
	(*vertexList)[v].color = 2
}

func main() {
	//t := time.Now()
	scanr := bufio.NewScanner(os.Stdin)
	var newstr string
	formulas = make([][]pair, 0)
	m = make(map[string]int, 0)
	mm = make(map[int]int, 0)
	formulanum := 0
	for scanr.Scan() {
		newstr = scanr.Text()
		if newstr == "" {
			break
		}
		lexer(newstr)
		////fmt.Println(lexems)
		define = make([]int, 0)
		usedIn = make([]int, 0)
		parse_formula()
		var v vertex
		v.number = formulanum
		v.formula = newstr
		v.define = define
		v.usedIn = usedIn
		for _, x:= range define{
			mm[x] = formulanum
		}
		////fmt.Println(usedIn)
		////fmt.Println(define)
		////fmt.Println(newstr)
		formulanum++
		////fmt.Println(mm)
		//fmt.Println()
		if intersect(define, usedIn){
			fmt.Println("cycle")
			os.Exit(0)
		}
		vertexList = append(vertexList, v)
	}

	lefts, rights := make([]string, 0), make([]string, 0) //
	for _, x := range formulas {
		for _, y := range x {
			lefts = append(lefts, y.left)
			rights = append(rights, y.right...)
		}
	}

	sort.Strings(lefts) // тут проверяем, сколько раз задается переменная
	// должна быть только один
	sort.Strings(rights)
	for i := 0; i < len(lefts)-1; i++ {
		if lefts[i] == lefts[i+1] {
			exitwitherr()
		}
	}
	for i := 0; i < len(rights)-1; i++ {
		if rights[i] == rights[i+1] {
			rights = append(rights[:i], rights[i+1:]...)
			i--
		}
	}

	// если мы используем "x" в usedIn, то он когда-то должен был быть объявлен в lefts
	if !isSubset(rights, lefts){
		exitwitherr()
	}

	// а теперь построим граф



	// задаем дуги
	// если в x использовалось то, что задавалось в y
	// значит есть ребро y->x
	for i, x:= range vertexList{
		//fmt.Println("formula: ", x.formula)
		//fmt.Println("usedIn: ", x.usedIn)
		for _, y := range x.usedIn{
			//fmt.Println(y, "->", vertexList[mm[y]].formula)
			vertexList[mm[y]].edges = append(vertexList[mm[y]].edges, i)
		}
		//fmt.Println()
	}




	DFS(&vertexList)

	sort.Slice(vertexList, func(i, j int) bool {
		return vertexList[i].time > vertexList[j].time
	})

	for _, v := range vertexList {
		fmt.Println(v.formula)
	}
	//fmt.Println(time.Since(t))

}
