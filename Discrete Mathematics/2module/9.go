//<program> ::= <function> <program>.
//
//<function> ::= <ident> ( <formal-args-list> := <expr> ; .
//<formal-args-list> ::= <ident> <end-identlist> ) | )
//<end-identlist> ::= , <ident> <ident-list> | .

//Выражение – это либо выражение выбора, использующее тернарную операцию в духе языка C,
//либо выражение сравнения:
//<expr> ::=  <comparison_expr> <end-expr>
//<end-expr> ::= ? <comparison_expr> : <expr> | .

//Выражение сравнения представляет собой либо сравнение двух арифметичеких выражений,
//либо просто одно арифметическое выражение:
//<comp_expr> ::= <arith_expr> <end-comp_expr>
//<end-comp_expr> ::= <comparison_op> <arith_expr> | .
//<comparison_op> ::= = | <> | < | > | <= | >= .

//<arith_expr> ::= <term> <end-arith_expr>
//<end-arith_expr> ::= + <term> <end-arith_expr> | - <term> <end-arith_expr> | .
//<term> ::= <factor> <end-term>
//<end-term> ::= * <factor> <end-term> | / <factor> <end-term> | .
//<factor> ::= <number>  | ( <expr> ) | - <factor> | <some-ident>
//<some-ident> ::= <ident> <end-ident>
//<end-ident> ::= ( <actual_args_list> | .

//<actual_args_list> ::= <expr-list> ) | )
//<expr-list> ::= <expr> <end-expr-list>
//<end-expr-list> ::= , <expr>  <end-expr-list> | .
//
//по-сути нужно проверить текст на соответствие грамматике,
//а не разбивать его на токены (поэтому, например, знаки арифметических
//операций мне не важны)
//нужно лишь разобраться с соответствием формальных параметров для функций
//
//для этого хорошо-бы завести список функций,
//к нему прикрепить список формальных параметров,
//затем проверять каждый параметр из тела функции на наличие в списке формальных
//
//при встрече функции в теле программы нужно удостовериться,
//что количество параметров совпадает, тк язык поддерживает только один тип данных
//
//как будем проверять?
//по-сути нам нужно проверить всякие-разные соответствия параметров
//
//сначала находим все имена функций и сразу же считаем количество формальных параметров
//(будем делать это прямо во время синтаксического анализа)
//
//в теле функции должны присутствовать только формальные параметры или имена других функций
//
//при вызове функции количество формальных параметров должно совпадать
//
//считать количество параметров при вызове функций будем на стеке,
//потому что можно передать в качестве параметра вызов другой функции


package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

// для анализа:

type lexem struct {
	name    string
	content string
}

type function struct {
	name             string
	numOfParams      int
	namesOfParams    []string
	dependsOn        []string
	identsUsedInBody []string
}

type callfunc struct { // инфа о вызовах функций
	name    string
	counter int
}

// это кривой стек - тут top указывает на последний элемент в стеке
// так еще и работает он только с конкретной переменной
// так еще и все, что с него скидывается записывается в stDeleted
// ужас короче
type stack struct {
	data []callfunc
	top  int
}

func initi(n int) {
	st.data = make([]callfunc, n)
	stDeleted = make([]callfunc, 0)
	st.top = -1
}
func push(vertex callfunc) {
	st.top++
	st.data[st.top] = vertex
}
func pop() callfunc {
	stDeleted = append(stDeleted, st.data[st.top])
	st.top--
	return st.data[st.top+1]
}

var err bool
var lexems []lexem
var lindex int = 0
var functions []function
var st stack
var stDeleted []callfunc

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

func lexer(program string) {
	leng := len(program)
	var lx lexem
	for i := 0; i < leng; i++ {
		switch program[i] {
		case ' ':
			break
		case '-':
			lx.name = "minus"
			lx.content = "-"
			lexems = append(lexems, lx)
			break
		case '+':
			lx.name = "plus"
			lx.content = "+"
			lexems = append(lexems, lx)
			break
		case '*':
			lx.name = "mult"
			lx.content = "*"
			lexems = append(lexems, lx)
			break
		case '/':
			lx.name = "div"
			lx.content = "/"
			lexems = append(lexems, lx)
			break
		case '(':
			lx.name = "lparen"
			lx.content = "("
			lexems = append(lexems, lx)
			break
		case ')':
			lx.name = "rparen"
			lx.content = ")"
			lexems = append(lexems, lx)
			break
		case '?':
			lx.name = "questionmark"
			lx.content = "?"
			lexems = append(lexems, lx)
			break
		case ',':
			lx.name = "comma"
			lx.content = ","
			lexems = append(lexems, lx)
			break
		case ';':
			lx.name = "semicolon"
			lx.content = ";"
			lexems = append(lexems, lx)
			break
		case ':':
			if i+1 < leng && program[i+1] == '=' {
				lx.name = "funcdecl"
				lx.content = ":="
				lexems = append(lexems, lx)
				i++
			} else {
				lx.name = "colon"
				lx.content = ":"
				lexems = append(lexems, lx)
			}
			break
		case '=':
			lx.name = "compop"
			lx.content = "="
			lexems = append(lexems, lx)
		case '<':
			if i+1 < leng && program[i+1] == '=' {
				lx.name = "compop"
				lx.content = "<="
				lexems = append(lexems, lx)
				i++
			} else if i+1 < leng && program[i+1] == '>' {
				lx.name = "compop"
				lx.content = "<>"
				lexems = append(lexems, lx)
				i++
			} else {
				lx.name = "compop"
				lx.content = "<"
				lexems = append(lexems, lx)
			}
			break
		case '>':
			if i+1 < leng && program[i+1] == '=' {
				lx.name = "compop"
				lx.content = ">="
				lexems = append(lexems, lx)
				i++
			} else {
				lx.name = "compop"
				lx.content = ">"
				lexems = append(lexems, lx)
			}
			break
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
				lx.name = "err"
				lexems = append(lexems, lx)
				err = true
			}
		}
	}
}

func exitwitherr() {
	fmt.Println("error")
	os.Exit(0)
}

func parse() {
	if lexems[len(lexems)-1].content != ";" {
		exitwitherr()
	}
	initi(100)
	parse_program()
}

//<program> ::= <function> <program>.
func parse_program() {

	parse_function()
	if lindex < len(lexems) {
		parse_program()
	}
}

//<function> ::= <ident> ( <formal-args-list> := <expr> ;
func parse_function() {
	parse_func_name()
	if lexems[lindex].content != "(" {
		//fmt.Println("foundparse_function1 - expected (")
		exitwitherr()
	}
	//fmt.Println("found (")
	lindex++
	parse_formal_args_list()
	if lexems[lindex].content != ":=" {
		//fmt.Println("foundparse_function2  - expected :=")
		exitwitherr()
	}
	//fmt.Println("found :=")
	lindex++
	parse_expr()
	if lexems[lindex].content != ";" {
		//fmt.Println("foundparse_function3 - expected ;")
		exitwitherr()
	}
	//fmt.Println("found ;")
	lindex++
}

func parse_func_name() {
	if lexems[lindex].name == "ident" {
		//fmt.Println("found ident")
		var newfunc function
		newfunc.name = lexems[lindex].content
		newfunc.namesOfParams = make([]string, 0)
		newfunc.dependsOn = make([]string, 0)
		newfunc.identsUsedInBody = make([]string, 0)
		functions = append(functions, newfunc)
		lindex++
	} else {
		//fmt.Println("foundparse_ident - expected ident")
		exitwitherr()
	}
}

func parse_ident() {
	if lexems[lindex].name == "ident" {
		//fmt.Println("found ident")
		lindex++
	} else {
		//fmt.Println("foundparse_ident - expected ident")
		exitwitherr()
	}
}

//<formal-args-list> ::= <ident> <end-identlist> ) | )
func parse_formal_args_list() {
	if lexems[lindex].name == "ident" {
		//fmt.Println("found ident")
		functions[len(functions)-1].numOfParams++
		functions[len(functions)-1].namesOfParams = append(functions[len(functions)-1].namesOfParams, lexems[lindex].content)
		lindex++
		parse_end_identlist()
	}
	if lexems[lindex].content != ")" {
		exitwitherr()
	}
	//fmt.Println("found )")
	lindex++
}

//<end-identlist> ::= , <ident> <ident-list> | .
func parse_end_identlist() {
	if lexems[lindex].content == "," {
		//fmt.Println("found ,")
		lindex++ // скипаем запятую
		if lexems[lindex].name == "ident" {
			//fmt.Println("found ident")
			// тут надо бы добавить ident в список формальных параметров
			functions[len(functions)-1].numOfParams++
			functions[len(functions)-1].namesOfParams =
				append(functions[len(functions)-1].namesOfParams, lexems[lindex].content)
			lindex++
			parse_end_identlist()
		} else {
			exitwitherr()
		}
	}
}

//<expr> ::=  <comparison_expr> <end-expr>
func parse_expr() {
	parse_comp_expr()
	parse_end_expr()
}

//<end-expr> ::= ? <comparison_expr> : <expr> | .
func parse_end_expr() {
	if lexems[lindex].content == "?" {
		//fmt.Println("found ?")
		lindex++ // скипнули вопросик
		parse_comp_expr()
		if lexems[lindex].content != ":" {
			//fmt.Println("foundparse_end_expr  - expected :")
			exitwitherr()
		}
		//fmt.Println("found :")
		lindex++
		parse_expr()
	}
}

//<comp_expr> ::= <arith_expr> <end-comp_expr>
func parse_comp_expr() {
	parse_arith()
	parse_end_comp_expr()
}

//<end-comp_expr> ::= <comparison_op> <arith_expr> | .
func parse_end_comp_expr() {
	if lexems[lindex].name == "compop" {
		//fmt.Println("found ", lexems[lindex].content)
		lindex++ // съели compop
		parse_arith()
	}
}

//<arith_expr> ::= <term> <end-arith_expr>
func parse_arith() {
	parse_term()
	parse_end_arith()
}

//<end-arith_expr> ::= + <term> <end-arith_expr> | - <term> <end-arith_expr> | .
func parse_end_arith() {
	if lexems[lindex].content == "+" || lexems[lindex].content == "-" {
		//fmt.Println("found ", lexems[lindex].content)
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
	if lexems[lindex].content == "*" || lexems[lindex].content == "/" {
		//fmt.Println("found ", lexems[lindex].content)
		lindex++
		parse_factor()
		parse_end_term()
	}
}

//<factor> ::= <number>  | ( <expr> ) | - <factor> | <some-ident>
func parse_factor() {
	if lexems[lindex].name == "number" {
		//fmt.Println("found number: ", lexems[lindex].content)
		lindex++
	} else if lexems[lindex].content == "(" {
		//fmt.Println("found (")
		lindex++
		parse_expr()
		if lexems[lindex].content != ")" {
			//fmt.Println("foundparse_factor  - expected )")
			exitwitherr()
		}
		//fmt.Println("found )")
		lindex++
	} else if lexems[lindex].content == "-" {
		//fmt.Println("found -")
		lindex++
		parse_factor()
	} else {
		parse_some_ident()
	}
}

//<some-ident> ::= <ident> <end-ident>
//это или переменная, или вызов функции
func parse_some_ident() {
	parse_ident()
	parse_end_ident()
}

//<end-ident> ::= ( <actual_args_list> | .
func parse_end_ident() {
	if lexems[lindex].content == "(" {
		//значит в предыдущей лексеме было имя функции
		if !isInSlice(functions[len(functions)-1].dependsOn, lexems[lindex-1].content) {
			functions[len(functions)-1].dependsOn =
				append(functions[len(functions)-1].dependsOn, lexems[lindex-1].content)
		}
		// ухх! мы наткнулись на новый вызов
		var newcall callfunc
		newcall.name = lexems[lindex-1].content
		push(newcall)
		//fmt.Println("found (")
		lindex++
		parse_actual_arg_list()
		// отпарсили вызов и он закончился
		//..
		//..
		//..
		//..
		//..
		//..
		//..
		// логично
		pop()
	} else {
		//значит в предыдущей лексеме было имя переменной
		if !isInSlice(functions[len(functions)-1].identsUsedInBody, lexems[lindex-1].content) {
			functions[len(functions)-1].identsUsedInBody =
				append(functions[len(functions)-1].identsUsedInBody, lexems[lindex-1].content)
		}
	}
}

//<actual_args_list> ::= <expr-list> ) | )
func parse_actual_arg_list() {
	if lexems[lindex].content == ")" {
		//fmt.Println("found )")
		lindex++
	} else {
		parse_expr_list()
		if lexems[lindex].content != ")" {
			//fmt.Println("foundparse_actual_arg_list  - expected )")
			exitwitherr()
		}
		//fmt.Println("found )")
		lindex++
	}
}

//<expr-list> ::= <expr> <end-expr-list>
func parse_expr_list() {
	parse_expr()
	//это первый параметр, с которым вызывается функция
	st.data[st.top].counter++
	parse_end_expr_list()
}

//<end-expr-list> ::= , <expr>  <end-expr-list> | .
func parse_end_expr_list() {
	if lexems[lindex].content == "," {
		//fmt.Println("found ,")
		lindex++
		//а вот еще один
		parse_expr()
		st.data[st.top].counter++
		parse_end_expr_list()
	}
}

func isInSlice(sl []string, str string) bool {
	for _, x := range sl {
		if x == str {
			return true
		}
	}
	return false
}

func isSubset(inBody, params []string) bool {
	c := 0
	for _, x := range params {
		for _, y := range inBody {
			if x == y {
				c++
			}
		}
	}
	if c == len(inBody){
		return true
	}
	return false
}

// для графов:

type vertex struct {
	num      int
	comp     int
	low      int
	t1       int
	entrance int

	edges []int
}

type normalStack struct {
	data []int
	top  int
}

func normalIniti(s *normalStack, n int) {
	(*s).data = make([]int, n)
}
func normalPush(s *normalStack, vertex int) {
	(*s).data[(*s).top] = vertex
	(*s).top++
}
func normalPop(s *normalStack) int {
	(*s).top--
	return (*s).data[(*s).top]
}

var time, count int

func Tarjan(vertexList *[]vertex) {
	var st normalStack
	normalIniti(&st, len(*vertexList))
	for i, v := range *vertexList {
		if v.t1 == 0 {
			VisitVertexTarjan(vertexList, i, &st)
		}
	}
}

func VisitVertexTarjan(vertexList *[]vertex, vNum int, st *normalStack) {
	(*vertexList)[vNum].t1, (*vertexList)[vNum].low = time, time
	time++
	normalPush(st, vNum)
	for _, u := range (*vertexList)[vNum].edges {
		if (*vertexList)[u].t1 == 0 {
			VisitVertexTarjan(vertexList, u, st)
		}
		if (*vertexList)[u].comp == -1 && (*vertexList)[vNum].low > (*vertexList)[u].low {
			(*vertexList)[vNum].low = (*vertexList)[u].low
		}
	}
	if (*vertexList)[vNum].low == (*vertexList)[vNum].t1 {
		u := normalPop(st)
		(*vertexList)[u].comp = count
		for (*vertexList)[u].num != (*vertexList)[vNum].num {
			u = normalPop(st)
			(*vertexList)[u].comp = count
		}
		count++
	}
}

func main() {
	scanr := bufio.NewScanner(os.Stdin)
	var program string
	var newstr string
	for scanr.Scan() {
		newstr = scanr.Text()
		if newstr == "" {
			break
		}
		program += newstr
	}

	lexems = make([]lexem, 0)
	functions = make([]function, 0)
	lexer(program)
	parse()

	listoffuncs := make([]string, 0)
	for _, x := range functions {
		sort.Strings(x.namesOfParams)
		sort.Strings(x.identsUsedInBody)
		sort.Strings(x.dependsOn)
		listoffuncs = append(listoffuncs, x.name)
	}

	for _, x := range functions {
		if !isSubset(x.identsUsedInBody, x.namesOfParams) {
			exitwitherr()
		}
		for _, y := range stDeleted {
			if !isInSlice(listoffuncs, y.name) {
				exitwitherr()
			}
			if x.name == y.name {
				if x.numOfParams != y.counter {
					exitwitherr()
				}
			}
		}
	}
	sort.Strings(listoffuncs)

	m := make(map[string]int)
	for i, x := range listoffuncs {
		m[x] = i
	}
	//а тут тупо копирую код из другой задачи - не зря же решал)
	vertexList := make([]vertex, len(listoffuncs))
	for i := 0; i < len(listoffuncs); i++ {
		var v vertex
		v.num = i
		v.edges = make([]int, 0)
		v.comp = -1
		vertexList[i] = v
	}
	var a, b int
	for _, x := range functions {
		a = m[x.name]
		for _, y := range x.dependsOn {
			b = m[y]
			vertexList[a].edges = append(vertexList[a].edges, b)
		}
	}
	time, count = 1, 0
	Tarjan(&vertexList)
	fmt.Println(count)
}
