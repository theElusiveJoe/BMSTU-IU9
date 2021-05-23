package main

import (
	"fmt"
	"os"
)

type vertex struct {
	num    int
	cannum int
	color  int
}

type matrixelem struct {
	leadsto int
	out     string
}

var vertexlist []vertex
var matrix [][]matrixelem
var mp map[string]int

var cannum int

func DFS(num int) {
	if vertexlist[num].color == 0 {
		//fmt.Println("coloring vertex num ", vertexlist[num].num)
		vertexlist[num].color = 1
		vertexlist[num].cannum = cannum
		cannum++
		for i := 0; i < m; i++ {
			DFS(matrix[num][i].leadsto)
		}
	}
}

var n, m, ss int

func main() {
	fmt.Scan(&n, &m, &ss)
	vertexlist = make([]vertex, n)
	for i := 0; i < n; i++ {
		vertexlist[i].num = i
		vertexlist[i].cannum = -1
	}
	matrix = make([][]matrixelem, n) // n строк
	for i := 0; i < n; i++ {
		matrix[i] = make([]matrixelem, m) // m столбцов
	}

	// ввод матрицы перехода состояний
	for i := 0; i < n; i++ { // строки - состояния
		for j := 0; j < m; j++ { // столбцы - входные сигналы
			fmt.Scan(&matrix[i][j].leadsto)
		}
	}
	// воод матрицы выходных значений
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			fmt.Fscan(os.Stdin, &matrix[i][j].out)
		}
	}


	fmt.Println("digraph {")
	fmt.Println("rankdir = LR")
	fmt.Println("dummy [label = \"\", shape = none]")
	for i := 0; i < n; i++ {
		fmt.Printf("\t%d [shape = circle]\n", i)
	}
	fmt.Printf("\tdummy -> %d\n", ss)
	for i := 0; i < n; i++ { // строки - состояния
		for j := 0; j < m; j++ { // столбцы - входные сигналы
			fmt.Printf("\t%d->%d [label = \"%s(%s)\"]\n", i, matrix[i][j].leadsto, string(97+j), matrix[i][j].out)
		}
	}
	fmt.Println("}")

}

