package main

import (
	"fmt"
)

type state struct {
	q int
	y string
}

func printautomat(mooreleadsto [][]int, states []state, inalphabet []string) {
	fmt.Println("digraph {\n\trankdir = LR")
	for i, x := range states {
		fmt.Printf("\t%d [label = \"(%d,%s)\"]\n", i, x.q, x.y)
	}
	for i, _ := range mooreleadsto {
		for j, x := range mooreleadsto[i] {
			fmt.Printf("\t%d -> %d [label = \"%s\"]\n", i, x, inalphabet[j])
		}
	}
	fmt.Println("}")
}

func isin(st state, sts []state) int {
	for i, x := range sts {
		if x == st {
			return i
		}
	}
	return -1
}

func main() {
	var k1 int
	fmt.Scan(&k1)
	inalphabet := make([]string, k1)
	for i := 0; i < k1; i++ {
		fmt.Scan(&inalphabet[i])
	}
	var k2 int
	fmt.Scan(&k2)
	outalphabet := make([]string, k2)
	for i := 0; i < k2; i++ {
		fmt.Scan(&outalphabet[i])
	}

	var n int
	fmt.Scan(&n)
	leadsto := make([][]int, n)
	// ввод матрицы перехода состояний
	for i := 0; i < n; i++ { // строки - состояния
		leadsto[i] = make([]int, k1)
		for j := 0; j < k1; j++ { // столбцы - входные сигналы
			fmt.Scan(&leadsto[i][j])
		}
	}
	// воод матрицы выходных значений
	outs := make([][]string, n)
	for i := 0; i < n; i++ { // строки - состояния
		outs[i] = make([]string, k1)
		for j := 0; j < k1; j++ { // столбцы - входные сигналы
			fmt.Scan(&outs[i][j])
		}
	}

	states := make([]state, 0)
	var st state
	for i := 0; i < n; i++ {
		for j := 0; j < k1; j++ {
			st.q = leadsto[i][j]
			st.y = outs[i][j]
			// добавляем новые состояния
			if isin(st, states) == -1 {
				states = append(states, st)
			}
		}
	}

	mooreleadsto := make([][]int, len(states))
	for i := 0; i < len(states); i++ {
		mooreleadsto[i] = make([]int, k1)
		for j := 0; j < k1; j++ {
			//δ′(〈q,y〉,x)=〈δ(q,x),φ(q,x)〉
			st.q = leadsto[states[i].q][j]
			st.y = outs[states[i].q][j]
			mooreleadsto[i][j] = isin(st, states)
		}
	}

	printautomat(mooreleadsto, states, inalphabet)
}
