package main

import (
	"fmt"
	//"github.com/skorobogatov/input"
	"input"
	"math"
	"sort"
)

type atraction struct {
	x, y int
	connected *atraction
	generation int
}

type road struct {
	len int
	a1, a2 *atraction
}

func find(a *atraction) *atraction {
	root := a
	for root.connected != nil {
		root = root.connected
	}
	return root
}

func union(root1, root2 *atraction)  {
	if root1.generation > root2.generation {
		root2.connected = root1
	} else if root1.generation < root2.generation{
		root1.connected = root2
	} else {
		root1.generation++
		root2.connected = root1
	}


}

func spanningTree(roads *[]road, n int) float64 {
	var len float64
	i := 0
	var a1,a2 *atraction
	var a3,a4 *atraction
	for _, r := range (*roads){
		a1, a2 = r.a1, r.a2
		a3, a4 = find(a1), find(a2)
		if a3!=a4{
			len +=math.Sqrt(float64(r.len))
			i++
			if i== n-1{
				return len
			}
			union(a3,a4)
		}
	}
	return len
}

func main() {
	var n int
	input.Scanf("%d",&n)
	roadsNum := (n*(n-1))/2
	atractions := make([]atraction, n)
	roads := make([]road, roadsNum)
	var x, y int
	var a atraction
	for i :=0; i < n;i++{
		input.Scanf("%d %d",&x, &y)
		a.x, a.y = x, y
		atractions[i] = a
	}
	var r road
	rcount := 0
	for i := 0; i < n; i++ { // создадим массив из всех возможных дорожек
		for j := i + 1; j < n; j++ {
			r.a1 = &atractions[i]
			r.a2 = &atractions[j]
			r.len = (atractions[i].x-atractions[j].x)*(atractions[i].x-atractions[j].x) + (atractions[i].y-atractions[j].y)*(atractions[i].y-atractions[j].y)
			if r.len < 80 && n > 100{
				roads[rcount] = r
				rcount++
			}
		}
	}
	roads = roads[:rcount]
	// и отсортируем его
	sort.Slice(roads,  func(i, j int) bool {return roads[i].len < roads[j].len})
	fmt.Printf("%.2f\n",spanningTree(&roads, n))
}
