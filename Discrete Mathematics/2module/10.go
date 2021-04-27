package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type vertex struct {
	//основные данные
	num   int
	name  string
	w     int
	edges []int
	color int
	// для тарзана
	comp int
	low  int
	t1   int

	dist   int
	parents []int
	//
	indeg int
}

type stack struct {
	data []int
	top  int
}

const (
	black int = iota
	red       = iota
	blue      = iota
)

func initi(s *stack, n int) {
	(*s).data = make([]int, n*2)
}
func push(s *stack, vertex int) {
	(*s).data[(*s).top] = vertex
	(*s).top++
}
func pop(s *stack) int {
	(*s).top--
	return (*s).data[(*s).top]
}

var time, count int

func Tarjan(vertexList *[]vertex) {
	var st stack
	initi(&st, len(*vertexList))
	for i, v := range *vertexList {
		if v.t1 == 0 {
			VisitVertexTarjan(vertexList, i, &st)
		}
	}
}

func VisitVertexTarjan(vertexList *[]vertex, vNum int, st *stack) {
	(*vertexList)[vNum].t1, (*vertexList)[vNum].low = time, time
	time++
	push(st, vNum)
	for _, u := range (*vertexList)[vNum].edges {
		if (*vertexList)[u].t1 == 0 {
			VisitVertexTarjan(vertexList, u, st)
		}
		if (*vertexList)[u].comp == -1 && (*vertexList)[vNum].low > (*vertexList)[u].low {
			(*vertexList)[vNum].low = (*vertexList)[u].low
		}
	}
	if (*vertexList)[vNum].low == (*vertexList)[vNum].t1 {
		u := pop(st)
		(*vertexList)[u].comp = count
		for _, x := range (*vertexList)[u].edges{
			if x == (*vertexList)[u].num{
				(*vertexList)[u].color = blue
			}
		}
		for (*vertexList)[u].num != (*vertexList)[vNum].num {
			u = pop(st)
			(*vertexList)[u].comp = count
			bluePart(vertexList, u)
		}
		count++
	}
}

func bluePart(vertexlist *[]vertex, num int) {
	(*vertexlist)[num].color = blue
	//(*vertexlist)[num].dist = -1 // чтобы дийкстра не зашел в него
	for _, x := range (*vertexlist)[num].edges {
		if (*vertexlist)[x].color != blue {
			bluePart(vertexlist, x)
		}
	}
}

type queue struct {
	head, tail, count, cap int
	arr                    []int
}

func initi2(q *queue, n int) {
	(*q).arr = make([]int, n)
	(*q).cap = n
}

func enqueue(q *queue, x int) {
	(*q).arr[(*q).tail] = x
	(*q).tail++
	(*q).count++
	if (*q).tail == (*q).cap {
		(*q).tail = 0
	}
}
func dequeue(q *queue) int {
	(*q).head++
	(*q).count--
	return (*q).arr[(*q).head-1]
}

func fillqueue(q *queue, vertexlist *[]vertex, num int){
	enqueue(q, -num-1)
	for _, x := range (*vertexlist)[num].edges{
		if (*vertexlist)[x].color != blue {
			enqueue(q, x)
		}
	}
	for _, x := range (*vertexlist)[num].edges{
		if (*vertexlist)[x].color != blue {
			fillqueue(q, vertexlist, x)
		}
	}
}

func critical(vertexlist *[]vertex, start int){
	var q queue
	initi2(&q, len(*vertexlist)*len(*vertexlist)*2)
	fillqueue(&q, vertexlist, start)
	(*vertexlist)[start].dist = (*vertexlist)[start].w
 	var parent, current int
	for q.count > 0{
		current = dequeue(&q)
		if current < 0{
			parent = -(current+1)
		} else {
			if (*vertexlist)[current].dist < (*vertexlist)[parent].dist	+ (*vertexlist)[current].w{
				//fmt.Println("now", (*vertexlist)[current].num, "parrent", "is", (*vertexlist)[parent].num)
				(*vertexlist)[current].dist = (*vertexlist)[parent].dist + (*vertexlist)[current].w
				parents := make([]int, 0)
				parents = append(parents, parent)
				(*vertexlist)[current].parents = parents
			} else if (*vertexlist)[current].dist == (*vertexlist)[parent].dist	+ (*vertexlist)[current].w {
				(*vertexlist)[current].parents = append((*vertexlist)[current].parents, parent)
			}
		}
	}
}

func redPart(vertexlist *[]vertex, num int) {
	(*vertexlist)[num].color = red
	//(*vertexlist)[num].dist = -1 // чтобы дийкстра не зашел в него
	if len((*vertexlist)[num].parents) == 0{
		return
	}
	for _, x := range (*vertexlist)[num].parents {
		if (*vertexlist)[x].color!= red {
			redPart(vertexlist, x)
		}
	}
}

func isIn(arr []int, x int) bool{
	for _, y := range arr{
		if x == y{
			return true
		}
	}
	return false
}

func main() {
	var str string
	//вбили строку
	scanr := bufio.NewScanner(os.Stdin)
	var newstr string
	for scanr.Scan() {
		newstr = scanr.Text()
		if newstr == "" {
			break
		}
		str += newstr
	}

	vertexlist := make([]vertex, 0)
	m := make(map[string]int)
	// сначала создадим узлы графа
	// для этого находим все описания с указанным временем
	str2 := strings.ReplaceAll(str, ";", "<")
	namesandnums := strings.Split(str2, "<")
	for i, x := range namesandnums {
		namesandnums[i] = strings.ReplaceAll(x, " ", "")
	}
	namesandonlynums := make([]string, 0)
	for _, x := range namesandnums {
		if x[len(x)-1] == ')' {
			namesandonlynums = append(namesandonlynums, x)
		}
	}

	counter := -1
	for _, x := range namesandonlynums {
		var start, end int
		for i, ch := range x {
			if ch == '(' {
				start = i
			}
			if ch == ')' {
				end = i
			}
		}

		if end == 0 {
			continue
		}

		counter++
		var v vertex
		m[x[:start]] = counter
		v.num = counter
		v.name = x[:start]
		v.w, _ = strconv.Atoi(x[start+1 : end])
		v.edges = make([]int, 0)
		v.comp = -1
		vertexlist = append(vertexlist, v)
	}

	// а теперь добавим ребра
	// для этого будем рассматривать каждую цепь по отдельности
	chains := strings.Split(str, ";")
	// для кадой цепочки:
	for _, x := range chains {
		// убрали пробелы
		x = strings.ReplaceAll(x, " ", "")
		// разбили на последовательность
		seq := strings.Split(x, "<")
		// для каждого слова последовательности
		for i, y := range seq {
			// пробегаем по буквам в словах
			// ищем скобочку и вырезаем все, что после неё
			for j, z := range y {
				if z == '(' {
					seq[i] = seq[i][:j]
				}
			}
		}
		for i := 0; i < len(seq)-1; i++ {
			a := m[seq[i]]
			b := m[seq[i+1]]
			if !isIn(vertexlist[a].edges, b) {
				vertexlist[a].edges = append(vertexlist[a].edges, b)
			}
			vertexlist[b].indeg++
		}
	}

	Tarjan(&vertexlist)

	for i, x := range vertexlist{
		if x.indeg == 0{
			vertexlist[i].dist = vertexlist[i].w
			critical(&vertexlist, i)
		}
	}



	var maxdist int
	for _, x := range vertexlist {
		if x.dist > maxdist {
			maxdist = x.dist
		}
	}

	maxdists := make([]int, 0)
	for _, x := range vertexlist {
		if x.dist == maxdist && x.color != blue{
			maxdists = append(maxdists, x.num)
		}
	}

	for _, max := range maxdists {
		redPart(&vertexlist, max)
	}

	fmt.Println("digraph {")
	for _, x := range vertexlist {
		var colstr string
		if x.color != black{
			colstr = "color = "
			if x.color == red{
				colstr += "red"
			} else {
				colstr += "blue"
			}
		}
		fmt.Printf("%s [label = \"%s(%d)\" %s]\n", x.name, x.name, x.w, colstr)
	}
	for _, x := range vertexlist {
		for _, y := range x.edges {
			var colstr string
			if x.color == red && vertexlist[y].color == red && isIn(vertexlist[y].parents, x.num){
					colstr = "[ color = red]"
			}
			if x.color == blue && vertexlist[y].color == blue{
				colstr = "[ color = blue]"
			}
			fmt.Printf("%s -> %s %s\n", x.name, vertexlist[y].name, colstr)
		}
	}
	fmt.Println("}")
}
