package main

import "fmt"

type node struct {
	num, colored, color int
	friends             []int
}

type group struct {
	nodes, edges, color int
}

var nodes []node
var g, gmax group
var groupColor int

func createGroup(x int) {
	nodes[x].colored = 1
	nodes[x].color = groupColor
	g.nodes++
	g.edges += len(nodes[x].friends)
	g.color = groupColor
	for _, y := range nodes[x].friends {
		if nodes[y].colored == 0 {
			createGroup(y)
		}
	}
}

func main() {
	var m, n, x, y int
	fmt.Scan(&n)
	fmt.Scan(&m)

	nodes = make([]node, n)
	for _, x := range nodes {
		x.friends = make([]int, 0)
	}

	for i := 0; i < m; i++ { // ввод графа
		fmt.Scan(&x)
		fmt.Scan(&y)
		nodes[x].friends = append(nodes[x].friends, y)
		if y != x {
			nodes[y].friends = append(nodes[y].friends, x)
		}
	}

	groupColor = 0

	for i, _ := range nodes {
		g.nodes, g.edges = 0, 0
		if nodes[i].colored == 0 {
			createGroup(i)
		}
		if g.nodes > gmax.nodes || (g.nodes == gmax.nodes && g.edges > gmax.edges) {
			gmax = g
		}
		groupColor++
	}

	fmt.Println("graph {")
	for i, x := range nodes{
		fmt.Print(i)
		if x.color == gmax.color{
			fmt.Print("[color = red]")
		}
		fmt.Println()
	}
	for i:= 0; i < n; i++{
		for _, y := range nodes[i].friends{
			if i <= y{
				fmt.Print(i, "--", y)
				if nodes[i].color == gmax.color{
					fmt.Print("[color = red]")
				}
				fmt.Println()
			}
		}
	}
	fmt.Println("}")
}
