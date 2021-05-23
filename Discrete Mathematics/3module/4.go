package main

import (
	"fmt"
	"reflect"
)

type state struct {
	num    int
	num2   int
	parent *state
	depth  int

	cannum int
	color  int
}

type automat struct {
	n, m, ss int
	leadsto  [][]int
	out      [][]string
	states   []state
}

func makeautomat(A *automat) {
	(*A).leadsto = make([][]int, (*A).n)
	(*A).out = make([][]string, (*A).n)
	(*A).states = make([]state, (*A).n)
	for i := 0; i < (*A).n; i++ {
		(*A).states[i].num = i
		(*A).leadsto[i] = make([]int, (*A).m)
		(*A).out[i] = make([]string, (*A).m)
	}
}

func printautomat(A automat) {
	fmt.Println("digraph {")
	fmt.Println("\trankdir = LR")
	fmt.Println("\tdummy [label = \"\", shape = none]")
	for i := 0; i < A.n; i++ {
		fmt.Printf("\t%d [shape = circle]\n", i)
	}
	fmt.Printf("\tdummy -> %d\n", A.ss)
	for i := 0; i < A.n; i++ { // строки - состояния
		for j := 0; j < A.m; j++ { // столбцы - входные сигналы
			fmt.Printf("\t%d -> %d [label = \"%s(%s)\"]\n", i, A.leadsto[i][j], string(97+j), A.out[i][j])
		}
	}
	fmt.Println("}")
}

func isin(st state, B automat) bool {
	for _, x := range B.states {
		if x == st {
			return true
		}
	}
	return false
}

func AufenkampHohn(A *automat) automat {
	m, pi := split1(A)

	var m2 int
	for {
		m2, pi = split(A, pi)
		if m == m2 {
			break
		}
		m = m2
	}

	var B automat
	makeautomat(&B)

	pi = normalize_nums(pi, &B)

	for _, q := range (*A).states {
		newstate := pi[q.num]
		if !isin(newstate, B) {
			B.n++
			B.states = append(B.states, newstate)
			lt, ou := make([]int, 0), make([]string, 0)
			for j := 0; j < (*A).m; j++ {
				lt = append(lt, pi[(*A).leadsto[q.num][j]].num2)
				ou = append(ou, (*A).out[q.num][j])
			}
			B.leadsto, B.out = append(B.leadsto, lt), append(B.out, ou)
		}
	}

	B.m = A.m
	for i, _ := range A.states {
		A.states[i].num = A.states[i].num2
	}

	return B
}

func find(a *state) *state {
	root := a
	for root.parent != root {
		root = root.parent
	}
	return root
}

func union(root1, root2 *state) {
	root1 = find(root1)
	root2 = find(root2)
	if root1.depth > root2.depth {
		root2.parent = root1
	} else if root1.depth < root2.depth {
		root1.parent = root2
	} else {
		root1.depth++
		root2.parent = root1
	}
}

func split1(A *automat) (int, []state) {
	m := len((*A).states)
	pi := make([]state, m)
	for i, _ := range (*A).states {
		(*A).states[i].parent = &(*A).states[i]
	}
	for i := 0; i < (*A).n; i++ {
		for j := i + 1; j < (*A).n; j++ {
			if find(&(*A).states[i]) != find(&(*A).states[j]) {
				eq := true
				for k := 0; k < (*A).m; k++ {
					if (*A).out[i][k] != (*A).out[j][k] {
						eq = false
						break
					}
				}
				if eq {
					union(&(*A).states[i], &(*A).states[j])
					m--
				}
			}
		}
	}

	for i := 0; i < (*A).n; i++ {
		pi[(*A).states[i].num] = *find(&(*A).states[i])
	}
	return m, pi
}

func split(A *automat, pi []state) (int, []state) {
	m := len((*A).states)
	for i, _ := range (*A).states {
		(*A).states[i].depth = 0
		(*A).states[i].parent = &(*A).states[i]
	}
	for i := 0; i < (*A).n; i++ {
		for j := i + 1; j < (*A).n; j++ {
			if find(&(*A).states[i]) != find(&(*A).states[j]) && pi[(*A).states[i].num] == pi[(*A).states[j].num] {
				eq := true
				for k := 0; k < (*A).m; k++ {
					if pi[(*A).leadsto[i][k]] != pi[(*A).leadsto[j][k]] {
						eq = false
						break
					}
				}
				if eq {
					union(&(*A).states[i], &(*A).states[j])
					m--
				}
			}
		}
	}
	for i := 0; i < (*A).n; i++ {
		pi[(*A).states[i].num] = *find(&(*A).states[i])
	}

	return m, pi
}

func normalize_nums(pi []state, A *automat) []state {
	m := make(map[int]int, 0)
	c := 0
	for i, q := range pi {
		_, ok := m[q.num]
		if !ok {
			m[q.num] = c
			c++
		}
		pi[i].num2 = m[q.num]
	}

	return pi
}

func cannon(A *automat) automat {
	cannum = 0
	(*A).states = make([]state, (*A).n)
	for i := 0; i < (*A).n; i++ {
		(*A).states[i].num = i
		(*A).states[i].color = 0
		(*A).states[i].cannum = -1
	}
	DFS(A, (*A).ss)
	m1 := make(map[int]int) // old -> new
	m2 := make(map[int]int) // new -> old
	for _, x := range (*A).states {
		m1[x.num] = x.cannum
		m2[x.cannum] = x.num
	}

	for i := 0; i < (*A).n; i++ {
		for j := 0; j < (*A).m; j++ {
			(*A).leadsto[i][j] = m1[(*A).leadsto[i][j]]
		}
	}
	for _, x := range (*A).states {
		if x.cannum == -1 {
			(*A).n--
		}
	}

	var B automat
	makeautomat(&B)
	B.n, B.m = (*A).n, (*A).m

	for i := 0; i < (*A).n; i++ {
		k := m2[i]
		if (*A).states[k].cannum != -1 {
			B.leadsto = append(B.leadsto, (*A).leadsto[k])
			B.out = append(B.out, (*A).out[k])
			B.states = append(B.states, (*A).states[k])
		}
	}

	for i, _ := range B.states {
		B.states[i].num = B.states[i].cannum
	}

	return B
}

var cannum int

func DFS(A *automat, num int) {
	if (*A).states[num].color == 0 {
		(*A).states[num].color = 1
		(*A).states[num].cannum = cannum
		cannum++
		for i := 0; i < A.m; i++ {
			DFS(A, A.leadsto[num][i])
		}
	}
}

func main() {
	var A automat
	fmt.Scan(&A.n, &A.m, &A.ss)
	makeautomat(&A)
	// ввод матрицы перехода состояний
	for i := 0; i < A.n; i++ { // строки - состояния
		for j := 0; j < A.m; j++ { // столбцы - входные сигналы
			fmt.Scan(&A.leadsto[i][j])
		}
	}
	// воод матрицы выходных значений
	for i := 0; i < A.n; i++ { // строки - состояния
		for j := 0; j < A.m; j++ { // столбцы - входные сигналы
			fmt.Scan(&A.out[i][j])
		}
	}

	var B automat
	fmt.Scan(&B.n, &B.m, &B.ss)
	makeautomat(&B)
	// ввод матрицы перехода состояний
	for i := 0; i < B.n; i++ { // строки - состояния
		for j := 0; j < B.m; j++ { // столбцы - входные сигналы
			fmt.Scan(&B.leadsto[i][j])
		}
	}
	// воод матрицы выходных значений
	for i := 0; i < B.n; i++ { // строки - состояния
		for j := 0; j < B.m; j++ { // столбцы - входные сигналы
			fmt.Scan(&B.out[i][j])
		}
	}

	if A.m != B.m{
		fmt.Println("NOT EQUAL")
		return
	}
	A = cannon(&A)
	A = AufenkampHohn(&A)
	A = cannon(&A)
	B = cannon(&B)
	B = AufenkampHohn(&B)
	B = cannon(&B)

	if !reflect.DeepEqual(A, B){
		fmt.Println("NOT EQUAL")
		return
	}

	fmt.Println("EQUAL")
}
