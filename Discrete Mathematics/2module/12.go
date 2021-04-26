package main

import (
	"fmt"
)

type namestruct struct {
	x, y int
}

type vertex struct {
	name           namestruct
	index, dist, w int
	edges          []namestruct
}

type pqueue struct {
	heap  []*vertex
	count int
}

func initi(q *pqueue, n int) {
	q.heap = make([]*vertex, n)
	q.count = 0
}

func qempty(q *pqueue) bool {
	if (*q).count == 0 {
		return true
	}
	return false
}

func insert(q *pqueue, v *vertex) {
	i := q.count
	q.count++
	q.heap[i] = v
	for i > 0 && q.heap[(i-1)/2].dist > q.heap[i].dist {
		q.heap[i], q.heap[(i-1)/2] = q.heap[(i-1)/2], q.heap[i]
		q.heap[i].index = i
		i = (i - 1) / 2
	}
	(*q.heap[i]).index = i
	(*v).index = i
}

func heapify(q *pqueue, i, n int) {
	var l, j, r int
	for {
		l = 2*i + 1
		r = l + 1
		j = i
		if l < n && q.heap[i].dist > q.heap[l].dist {
			i = l
		}
		if r < n && q.heap[i].dist > q.heap[r].dist {
			i = r
		}
		if i == j {
			break
		}
		// так как в очереди хранятся ссылки на узлы,
		// то изменяя их здесь, мы изменяем их и в vertexList
		q.heap[i], q.heap[j] = q.heap[j], q.heap[i]
		(*q.heap[i]).index, (*q.heap[j]).index = i, j
	}
}

func extractMin(q *pqueue) *vertex {
	element := q.heap[0]
	q.count--
	if !qempty(q) {
		q.heap[0] = q.heap[q.count]
		q.heap[0].index = 0
		heapify(q, 0, q.count)
	}
	return element
}

func decreaseKey(q *pqueue, index, len int) {
	i := index
	q.heap[index].dist = len
	for i > 0 && q.heap[(i-1)/2].dist > len {
		q.heap[(i-1)/2], q.heap[i] = q.heap[i], q.heap[(i-1)/2]
		q.heap[i].index = i
		i = (i - 1) / 2
	}
	q.heap[i].index = i
}

func relax(u, v *vertex, w int) bool {
	changed := u.dist+w < v.dist
	if u.dist+w < v.dist {
		v.dist = u.dist + w
	}
	return changed
}

func Dijkstra(vertexlist *[][]vertex, n int) {
	var q pqueue
	initi(&q, n*n)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if i == 0 && j == 0 {
				(*vertexlist)[i][j].dist = (*vertexlist)[i][j].w
			} else {
				(*vertexlist)[i][j].dist = 150000
			}
			insert(&q, &(*vertexlist)[i][j])
		}
	}
	for !qempty(&q) {
		v := extractMin(&q)
		v.index = -1
		for _, u := range v.edges {
			if (*vertexlist)[u.x][u.y].index != -1 && relax(v, &(*vertexlist)[u.x][u.y], (*vertexlist)[u.x][u.y].w) {
				decreaseKey(&q, (*vertexlist)[u.x][u.y].index, (*vertexlist)[u.x][u.y].dist)
			}
		}
	}

	fmt.Println((*vertexlist)[n-1][n-1].dist)
}

func main() {
	//t := time.Now()
	var n int
	fmt.Scan(&n)
	if n == 1 {
		fmt.Scan(&n)
		fmt.Println(n)
		return
	}

	vertexlist := make([][]vertex, n)
	var w int
	for i := 0; i < n; i++ {
		vertexlist[i] = make([]vertex, n)
		for j := 0; j < n; j++ {
			vertexlist[i][j].edges = make([]namestruct, 0)
		}
	}

	var newname namestruct
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			newname.x = i
			newname.y = j
			vertexlist[i][j].name = newname
			fmt.Scan(&w)
			vertexlist[i][j].w = w
			if i > 0 {
				vertexlist[i-1][j].edges = append(vertexlist[i-1][j].edges, newname)
			}
			if i < n-1 {
				vertexlist[i+1][j].edges = append(vertexlist[i+1][j].edges, newname)
			}
			if j > 0 {
				vertexlist[i][j-1].edges = append(vertexlist[i][j-1].edges, newname)
			}
			if j < n-1 {
				vertexlist[i][j+1].edges = append(vertexlist[i][j+1].edges, newname)
			}
		}
	}

	Dijkstra(&vertexlist, n)
	//fmt.Println(t.Sub(time.Now()))
}
