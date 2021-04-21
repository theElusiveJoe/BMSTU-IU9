package main

import (
	"fmt"
)

type vertex struct {
	num  int
	comp int
	low  int
	t1   int
	entrance int

	edges []int
}

type stack struct {
	data []int
	top  int
}

func initi(s *stack, n int) {
	(*s).data = make([]int, n)
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
		for (*vertexList)[u].num != (*vertexList)[vNum].num {
			u = pop(st)
			(*vertexList)[u].comp = count
		}
		count++
	}
}

func main() {
	var m, n int
	fmt.Scanf("%d", &n)
	vertexList := make([]vertex, n)
	for i := 0; i < n; i++ {
		var v vertex
		v.num = i
		v.edges = make([]int, 0)
		v.comp = -1
		vertexList[i] = v
	}
	var x, y int
	fmt.Scanf("%d", &m)
	for i := 0; i < m; i++ {
		fmt.Scanf("%d %d", &x, &y)
		vertexList[x].edges = append(vertexList[x].edges, y)
	}


	time, count = 1, 0
	Tarjan(&vertexList)

	// создаем граф конденсации и находим его ребра
	vertexCondensation := make([]vertex, count);
	for i := 0; i < count; i++ {
		var v vertex
		v.num = i
		v.edges = make([]int, 0)
		v.comp = i
		vertexCondensation[i] = v
	}
	for x, _ := range vertexList{ // x - номер узла графа
		for _, y := range vertexList[x].edges{ // y - номер узла, связанного с x
			// если x и y в разныx компнентах
			// то говорим, что компонента, в которой y, имеет ненулевую степень вхождения
			if vertexList[x].comp != vertexList[y].comp{
				vertexCondensation[vertexList[y].comp].entrance++
			}
		}
	}

	for _, x := range  vertexCondensation{ // я имею право так делать из-за того, что vertexList отсортирован
		if x.entrance == 0{
			for i, y := range vertexList{
				if x.comp == y.comp {
					fmt.Print(y.num, " ")
					vertexList = vertexList[i:]
					break
				}
			}
		}
	}
}
