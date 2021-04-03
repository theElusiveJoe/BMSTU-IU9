package main

import "fmt"
import "sort"

var nodes [][]int
var colors []int

func cmpColor(i, col int) bool {// здесь col - цвет узла с номером i
	ans := true
	fmt.Println("node ", i)
	if colors[i] == 0 { // если узел еще не покрашен, красим
		colors[i] = col
		fmt.Println("coloring node ", i, "in", col)
	} else if colors[i] != col { // если ожидаемый цвет не совпадает с действительным
		fmt.Println("wrong color!")
		return false
	}
	fmt.Println()
	for _, x := range nodes[i] { // проверяем интендентные узлы
		if colors[x] == 0 { // если идет до некрешенного узла, то переходим в него
			fmt.Print(i, "-->")
			ans = ans && cmpColor(x, 3-col)
		} else if colors[x] == col { // если интендентный узел имеет тот же цвет
			fmt.Println("nodes conflict:", i, "and", x)
			return false
		}
	}

	return ans
}

func main() {
	var n int
	fmt.Scan(&n)

	nodes = make([][]int, n) // список несовместимых
	var str string
	for i := 0; i < n; i++ {
		nodes[i] = make([]int, 0)
		for j := 0; j < n; j++ {
			fmt.Scan(&str)
			if str == "+" {
				nodes[i] = append(nodes[i], j)
			}
		}
	}

	for i := 0; i < n; i++ {
		fmt.Print(i, ":")
		fmt.Println(nodes[i])
	}

	colors = make([]int, n)
	for i, node := range nodes {
		if len(node) != 0 && colors[i] == 0 && !cmpColor(i, 1) {
			fmt.Println("No solution")
			return
		}
	}

	//fmt.Println(colors, " - colors")

	whites := make([]int, 0)
	blues := make([]int, 0)
	reds := make([]int, 0)
	for i := 0; i < n; i++ {
		if colors[i] == 0 {
			whites = append(whites, i+1)
		} else if colors[i] == 1 {
			blues = append(blues, i+1)
		} else {
			reds = append(reds, i+1)
		}
	}

	fmt.Println(whites, " - whites")
	fmt.Println(blues, " - blues")
	fmt.Println(reds, " - reds")

	for i := 0; len(blues) < n/2 && i < n; i++ {
		blues = append(blues, whites[i])
	}
	for i := 0; len(reds) < n/2 && i < n; i++ {
		reds = append(reds, whites[i])
	}

	sort.Ints(blues)
	sort.Ints(reds)
	i, j := 0, 0
	for i < len(blues) && j < len(reds) {
		if blues[i] < reds[j] {
			for _, x := range blues {
				fmt.Print(x, " ")
			}
			return
		} else if blues[i] > reds[j] {
			for _, x := range reds {
				fmt.Print(x, " ")
			}
			return
		}
		i++
		j++
	}

	if i == len(blues) {
		for _, x := range blues {
			fmt.Print(x, " ")
		}
	} else {
		for _, x := range reds {
			fmt.Print(x, " ")
		}
	}

}
