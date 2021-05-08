package main

import (
	"fmt"
	"sort"
)

type stack struct {
	top  int
	data []*vertex
}

func push(s *stack, vertex *vertex) {
	s.data[s.top] = vertex
	s.top++
}

func pop(s *stack) *vertex {
	s.top--
	return s.data[s.top]
}

type vertex struct {
	dead      bool
	time      int
	command   string
	operand   int
	parent    *vertex
	ancestor  *vertex
	idom      *vertex
	sdom      *vertex
	label     *vertex
	leadsto   []*vertex
	comesfrom []*vertex
	bucket    []*vertex
}

var vertexList []*vertex
var t = 1

func FindMin(v *vertex, s *stack) *vertex {
	if v.ancestor == nil {
		return v
	}

	s.top = 0
	var u = v
	for u.ancestor.ancestor != nil {
		push(s, u)
		u = u.ancestor
	}
	for s.top > 0 {
		v = pop(s)
		if v.ancestor.label.sdom.time < v.label.sdom.time {
			v.label = v.ancestor.label
		}
		v.ancestor = u.ancestor
	}

	return v.label
}

func Dominators(n int){
	var s stack
	s.data = make([]*vertex, n)
	sort.Slice(vertexList, func(i, j int) bool { return vertexList[i].time > vertexList[j].time })

	for _, w := range vertexList {
		if w.time == 1 {
			continue
		}
		for _, v := range w.comesfrom {
			u := FindMin(v, &s)
			if u.sdom.time < w.sdom.time {
				w.sdom = u.sdom
			}
		}
		w.ancestor = w.parent
		w.sdom.bucket = append(w.sdom.bucket, w)
		for _, v := range w.parent.bucket {
			u := FindMin(v, &s)
			if u.sdom == v.sdom {
				v.idom = v.sdom
			} else {
				v.idom = u
			}
		}
		w.parent.bucket = make([]*vertex, 0)
	}

	for _, w := range vertexList {
		if w.time == 1 {
			continue
		}
		if w.idom != w.sdom {
			w.idom = w.idom.idom
		}
	}

	vertexList[len(vertexList)-1].idom = nil
}

func DFS(v *vertex) {
	v.dead = false
	v.time = t
	t++
	for e, _ := range v.leadsto {
		if v.leadsto[e].dead {
			v.leadsto[e].parent = v
			DFS(v.leadsto[e])
		}
	}
}

func main() {
	var n, mark, operand int
	var str string
	fmt.Scan(&n)
	vertexList = make([]*vertex, 0)
	m := make(map[int]int)
	for i := 0; i < n; i++ {
		var v vertex
		v.dead = true
		v.comesfrom = make([]*vertex, 0)
		v.leadsto = make([]*vertex, 0)
		v.bucket = make([]*vertex, 0)
		v.sdom = &v
		v.label = &v
		vertexList = append(vertexList, &v)
	}

	for i, _ := range vertexList {
		fmt.Scanf("%d %s %d\n", &mark, &str, &operand)
		vertexList[i].command = str
		if str != "ACTION" {
			vertexList[i].operand = operand
		}
		m[mark] = i
	}

	for i, x := range vertexList {
		if x.command == "ACTION" {
			if i < n-1 {
				vertexList[i].leadsto = append(vertexList[i].leadsto, vertexList[i+1])
				vertexList[i+1].comesfrom = append(vertexList[i+1].comesfrom, vertexList[i])
			}
		} else if x.command == "JUMP" {
			operand = m[vertexList[i].operand]
			vertexList[i].leadsto = append(vertexList[i].leadsto, vertexList[operand])
			vertexList[operand].comesfrom = append(vertexList[operand].comesfrom, vertexList[i])
		} else {
			operand = m[vertexList[i].operand]
			vertexList[i].leadsto = append(vertexList[i].leadsto, vertexList[operand])
			vertexList[operand].comesfrom = append(vertexList[operand].comesfrom, vertexList[i])
			if i < n-1 {
				vertexList[i].leadsto = append(vertexList[i].leadsto, vertexList[i+1])
				vertexList[i+1].comesfrom = append(vertexList[i+1].comesfrom, vertexList[i])
			}
		}
	}

	DFS(vertexList[0])

	// отвязываем и удаляем мертвые
	for i := 0; i < len(vertexList); i++ {
		if !vertexList[i].dead {
			for j := 0; j < len(vertexList[i].comesfrom); j++ {
				if vertexList[i].comesfrom[j].dead {
					vertexList[i].comesfrom[j] = vertexList[i].comesfrom[len(vertexList[i].comesfrom)-1]
					vertexList[i].comesfrom = vertexList[i].comesfrom[:len(vertexList[i].comesfrom)-1]
					j--
				}
			}
		}
	}
	for i := 0; i < len(vertexList); i++ {
		if vertexList[i].dead {
			// меняем с последней и удаляем
			vertexList[i] = vertexList[len(vertexList)-1]
			vertexList[len(vertexList)-1] = nil
			vertexList = vertexList[:len(vertexList)-1]
			i--
			n--
		}
	}

	Dominators(n)

	var ans int
	for _, v := range vertexList {
		for _, e := range v.comesfrom {
			for e != v && e != nil {
				e = e.idom
			}
			if e == v {
				ans++
				break
			}
		}
	}

	fmt.Println(ans)
}
