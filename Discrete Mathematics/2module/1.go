package main

import "fmt"
import "math"

var nodes []int

func getNodes(x int) {
	nodes = append(nodes, x)
	//y := x
	sx := int(math.Round(math.Sqrt(float64(x))))
	for i := 2; i <= sx; i++ {
		if x%i == 0 {
			var inNodes bool
			for _, y := range nodes {
				if y == x/i {
					inNodes = true
					break
				}
			}
			if !inNodes {
				nodes = append(nodes, x/i)
				if i*i != x {
					nodes = append(nodes, i)
				}
			}
		}
	}
	if x != 1 {
		nodes = append(nodes, 1)
	}
	for _, y := range nodes {
		fmt.Println(y)
	}
}

func getEdges() {
	for _, x := range nodes { // от какого узла исходит
		y := x // делаем его копию
		sx := int(math.Round(math.Sqrt(float64(x))))
		for i := 2; i <= sx; i++ {
			if y%i == 0 {
				fmt.Println(x, "--", x/i)
				for y >= i && y%i == 0 {
					y /= i
				}
			}
		}
		if y != 1 && y != x{
			fmt.Println( x, "--", x/y)
		}
		if y == x && x != 1 {
			fmt.Println(x, "--", 1)
		}
	}
}

func main() {
	var x int
	fmt.Scan(&x)
	fmt.Println("graph {")
	getNodes(x)
	getEdges()
	fmt.Println("}")
}
