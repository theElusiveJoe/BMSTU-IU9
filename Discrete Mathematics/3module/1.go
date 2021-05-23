package main

import (
	"fmt"
	"os"
)

type vertex struct {
	num    int
	cannum int
	color int
}

type matrixelem struct {
	leadsto int
	out     string
}

var vertexlist []vertex
var matrix [][]matrixelem
var mp map[string]int

var cannum int
func DFS (num int){
	if vertexlist[num].color == 0{
		//fmt.Println("coloring vertex num ", vertexlist[num].num)
		vertexlist[num].color = 1
		vertexlist[num].cannum = cannum
		cannum++
		for i:= 0; i < m; i++{
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
	for i := 0; i < n; i++{
		for j:= 0; j < m; j++{
			fmt.Fscan(os.Stdin, &matrix[i][j].out)}
	}

	cannum = 0

	DFS(ss)

	//for _, x := range vertexlist{
	//	fmt.Println("num = ", x.num, " cannum = ", x.cannum, "color = ", x.color)
	//}

	// теперь надо перемешать матрицу
	// по-сути - поменялись только номера узлов(состояний)
	// те в самой матрице надо поменять значения leadsto
	// а также поменять строки местами(или выводить их в новом порядке)

	// создадим мапу из старых номеров в новые и наоборот
	m1 := make(map[int]int) // old -> new
	m2 := make(map[int]int) // new -> old
	for _, x := range vertexlist{
		m1[x.num] = x.cannum
		m2[x.cannum] = x.num
	}

	for i := 0; i < n; i++ { // строки - состояния
		for j := 0; j < m; j++ { // столбцы - входные сигналы
			matrix[i][j].leadsto = m1[matrix[i][j].leadsto]
		}
	}

	for _, x := range vertexlist{
		if x.cannum == -1{
			n--
		}
	}

	//вывод
	fmt.Println(n)
	fmt.Println(m)
	fmt.Println(0)

	for i := 0; i < n; i++ { // строки - состояния
		k := m2[i]
		if vertexlist[k].cannum != -1 {
			for j := 0; j < m; j++ { // столбцы - входные сигналы
				fmt.Print(matrix[k][j].leadsto, " ")
			}
			fmt.Println()
		}
	}

	for i := 0; i < n; i++ { // строки - состояния
		k := m2[i]
		if vertexlist[k].cannum != -1 {
			for j := 0; j < m; j++ { // столбцы - входные сигналы
				fmt.Print(matrix[k][j].out, " ")
			}
			fmt.Println()
		}
	}
}

