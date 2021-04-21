package main

import "fmt"

type vertex struct {
	num int
	marked bool
	next *vertex
	hasnext bool
}

type queue struct {
	head, tail int
	arr []vertex
}

func initi (q *queue, n int){
	q.arr = make([]vertex, n)
}

func enqueue (q *queue, x vertex){
	q.arr[q.tail] = x
	q.tail++
}
func dequeue (q *queue) vertex{
	q.head++
	return q.arr[q.head-1]
}

func getLast(list *[]vertex, i int) *vertex{
	x := &(*list)[i]
	for (*x).hasnext{
		x = x.next
	}
	(*x).hasnext = true
	x.next = new(vertex)
	return x.next
}

func main() {
	var n, m , x, y int
	fmt.Scan(&n)
	vertexList := make([]vertex, n)
	for i:= 0; i < n; i++{
		vertexList[i].num = i;
	}
	fmt.Scan(&m)
	for i := 0; i < m; i++{
		fmt.Scanf("%d %d", &x, &y)
		t := getLast(&vertexList, x)
		(*t).num = y
		t = getLast(&vertexList, y)
		(*t).num = x
	}
	for _, x := range vertexList{
		fmt.Print(x.num, ": ")
		for x.hasnext{
			x = *x.next
			fmt.Print(x.num, "-->")
		}
		fmt.Println()
	}
}
