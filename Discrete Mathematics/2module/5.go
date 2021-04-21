package main

import "fmt"

type vertex struct {
	num      int
	roletime     int // эталонное время
	localtime int
	wasHere  bool
	startNum int
	edges    []int
}

type queue struct {
	head, tail, count, cap int
	arr                    []*vertex
}

func initi(q *queue, n int) {
	(*q).arr = make([]*vertex, n)
	(*q).cap = n
}

func enqueue(q *queue, x *vertex) {
	(*q).arr[(*q).tail] = x
	(*q).tail++
	(*q).count++
	if (*q).tail == (*q).cap {
		(*q).tail = 0
	}
}
func dequeue(q *queue) *vertex {
	(*q).head++
	(*q).count--
	if (*q).head == (*q).cap {
		(*q).head = 0
		return (*q).arr[(*q).cap-1]
	}
	return (*q).arr[(*q).head-1]
}

func BFS0(vertexList []*vertex, startNum int) { // первый обход будем считать эталонным
	// а все остальные должны ему соответствовать
	var q queue
	initi(&q, len(vertexList))
	enqueue(&q, vertexList[startNum])
	for q.count > 0 {
		v := dequeue(&q)
		//fmt.Println("now v = ", v.num, "(", v.time, ")")
		(*v).wasHere = true
		(*v).startNum = startNum
		for _, w := range (*v).edges {
			if (vertexList)[w].startNum != startNum { // если мы его еще не рассматривали
				(vertexList)[w].startNum = startNum // обозначаем, что мы рассмотрели этот узел в этом проходе
				(vertexList)[w].roletime = v.roletime+1    // записываем эталонное время
				enqueue(&q, (vertexList)[w])
			}
		}
	}
}

func BFS(vertexList []*vertex, startNum int) bool {
	//fmt.Println("new bfs")
	var q queue
	initi(&q, len(vertexList))
	enqueue(&q, vertexList[startNum])
	for q.count > 0 {
		v := dequeue(&q)
		//fmt.Println("now v = ", v.num, "(", v.localtime, ")")
		if !(*v).wasHere { // если в первом проходе нас тут не было, значит опорные вершины находятся в разных компонентах
			return false
		}
		for _, w := range (*v).edges {
			if (vertexList)[w].startNum != startNum { // если мы его еще не рассматривали в этом проходе
				(vertexList)[w].localtime = v.localtime+1
				(vertexList)[w].startNum = (vertexList)[startNum].startNum // обозначаем, что мы рассмотрели этот узел в этом проходе
				if (vertexList)[w].roletime != (vertexList)[w].localtime{ // здесь стоит какое-то эталонное время
					// если оно не совпадает со временем этого вхождения, то помечаем негодность
					(vertexList)[w].roletime = -1
				}
				enqueue(&q, (vertexList)[w])
			}
		}
	}
	return true
}

func main() {
	var n, m, k, a, b int
	fmt.Scan(&n)
	vertexList := make([]*vertex, n)
	//ввод вершин
	for i := 0; i < n; i++ {
		var v vertex
		v.num = i
		v.edges = make([]int, 0)
		v.startNum = -1
		vertexList[i] = &v
	}
	fmt.Scan(&m)
	//ввод ребер
	for i := 0; i < m; i++ {
		fmt.Scan(&a)
		fmt.Scan(&b)
		vertexList[a].edges = append(vertexList[a].edges, b)
		vertexList[b].edges = append(vertexList[b].edges, a)
	}

	fmt.Scan(&k)
	fmt.Scan(&a)
	BFS0(vertexList, a)
	//for _, x := range vertexList {
	//	fmt.Println((*x).num, "(",(*x).roletime, ") " )
	//}
	bol := true
	for i := 1; i < k; i++ {
		fmt.Scan(&a)
		(*vertexList[a]).startNum = a
		(*vertexList[a]).localtime = 0
		(*vertexList[a]).roletime = 0
		bol = bol && BFS(vertexList, a)
		if !bol {
			fmt.Println("-")
			return
		}
		//for _, x := range vertexList {
		//	fmt.Print((*x).num, "(",(*x).localtime, ") " )
		//}
	}
	//fmt.Println("result:")
	//for _, x := range vertexList {
	//	fmt.Print((*x).num, "(",(*x).roletime, ") " )
	//}
	for _, x := range vertexList {
		if (*x).roletime > 0 {
			fmt.Print((*x).num, " ")
			bol = false
		}
	}
	if bol{
		fmt.Println("-")
	}
}
