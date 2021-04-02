package main

import "fmt"

func check(i int, nodes [][]int, colors *[]int) bool {

}

func checkColor()

func main() {
	var n int
	fmt.Scan(&n)

	nodes := make([][]int, n) // список несовместимых
	var str string
	for i := 0; i < n; i++ {
		nodes[i] = make([]int,0)
		for j := 0; j < n; j++ {
			fmt.Scan(&str)
			if str == "+" {
				nodes[i] = append(nodes[i], j)
			}
		}
	}

	colors = make([]int, n) // проверяем на двудольность
	for i , node := range nodes{
		if len(node) != 0{
			if colors[i] == 0{
				if !check(i, nodes, &colors){
					fmt.Println("No solution")
					return
				}
			}
		}
	}

	for i := 0; i < n; i++ {
		fmt.Println(i, nodes[i])
	}
}
