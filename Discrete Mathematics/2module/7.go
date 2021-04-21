package main

import (
	"fmt"
)

type vertex struct {
	num, index, key, value int
	edges                  []edge
}

type edge struct {
	dest, len int
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
	for i > 0 && q.heap[(i-1)/2].key > q.heap[i].key {
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
		if l < n && q.heap[i].key > q.heap[l].key {
			i = l
		}
		if r < n && q.heap[i].key > q.heap[r].key {
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
	q.heap[index].key = len
	for i > 0 && q.heap[(i-1)/2].key > len {
		q.heap[(i-1)/2], q.heap[i] = q.heap[i], q.heap[(i-1)/2]
		q.heap[i].index = i
		i = (i - 1) / 2
	}
	q.heap[i].index = i
}

func MST_Prim(listIncidence []*vertex, n int) int {
	len := 0
	v := listIncidence[0]
	var q pqueue
	initi(&q, n - 1)
	for {
		v.index = -2
		for _, e := range v.edges {
			if listIncidence[e.dest].index == -1 {
				listIncidence[e.dest].key = e.len
				listIncidence[e.dest].value = v.num
				insert(&q, listIncidence[e.dest])
			} else {
				if listIncidence[e.dest].index != -2 && e.len <= listIncidence[e.dest].key {
					listIncidence[e.dest].value = v.num
					decreaseKey(&q, listIncidence[e.dest].index, e.len)
				}
			}
		}
		if qempty(&q) {
			return len
		}
		v = extractMin(&q)
		len += v.key
	}

}

func main() {
	var n, m, x, y, len int
	fmt.Scan(&n)
	// теперь буду хранить массив ссылок - так удобнее
	vertexList := make([]*vertex, n)
	for i := 0; i < n; i++ {
		var v vertex // создаем переменную
		v.num = i
		v.index = -1
		v.edges = make([]edge, 0)
		vertexList[i] = &v // и закидываем ссылку на неё в массив
	}
	fmt.Scan(&m)
	var t edge
	for i := 0; i < m; i++ {
		fmt.Scanf("%d %d %d", &x, &y, &len)
		t.len = len
		t.dest = x
		vertexList[y].edges = append(vertexList[y].edges, t)
		t.dest = y
		vertexList[x].edges = append(vertexList[x].edges, t)
	}

	fmt.Println(MST_Prim(vertexList, n))
}
