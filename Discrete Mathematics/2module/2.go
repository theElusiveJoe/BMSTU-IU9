package main

import (
	"fmt"
)

var nodes [][]int
var variantsOfGroup [][]int
var g1 []int
var g2 []int
var n int

func makeVariants(groupNums []int, a, b, c, manNum int) {
	// a,b,c - счетчики того, сколько в человек могут входить в любую, только в первую, точлько во вторую группы
	if manNum == n {
		variantsOfGroup = append(variantsOfGroup, groupNums)
		g1 = append(g1, a)
		g2 = append(g2, b)
		return
	}

	var i int
	for i = 0; i < n; i++ { // находим такой минимальный i, что manNum и i не совместимы
		if nodes[manNum][i] == 1 {
			break
		}
	}
	if i == n { // если совместим со всеми 
		groupNums[manNum] = 0
		makeVariants(groupNums, a+1, b, c, manNum+1)
	} else {
		//создаем 2 последуюущих варианта
		group1 := make([]int, 0)
		group2 := make([]int, 0)
		for _, x := range groupNums {
			group1, group2 = append(group1, x), append(group2, x)
		}
		// они отличаются тем, что в одном из них manNum включен в первую групп, а в другом - во вторую
		group1[manNum], group2[manNum] = 1, 2
		f1, f2 := true, true

		for ; i < n && (f1 || f2); i++ {
			// в этом цикле добавляем в group1 и group2 те, которые можем
			// до тех пор, пока не встретим тот, который нельзя добавить
			if nodes[manNum][i] == 1 { // если i и manNum несовместимы
				if groupNums[i] == 0 { // если iй еще не распределили, то записываем в обе
					group1[i] = 2
					group2[i] = 1
				}
				if groupNums[i] == 1 { // если в первой группе
					f1 = false
				}
				if groupNums[i] == 2 { // если во второй группе
					f2 = false
				}
			}
		}

		if f1 {
			makeVariants(group1, a, b+1, c, manNum+1)
		}
		if f2 {
			makeVariants(group2, a, b, c+1, manNum+1)
		}
	}
}

func main() {
	fmt.Scan(&n)
	nodes = make([][]int, n)
	base := make([]int, n) // список кто-где
	var str string
	for i := 0; i < n; i++ {
		nodes[i] = make([]int, 0)
		for j := 0; j < n; j++ {
			fmt.Scan(&str)
			if str == "+" {
				nodes[i] = append(nodes[i], 1)
			} else {
				nodes[i] = append(nodes[i], 0)
			}
		}
	}

	makeVariants(base, 0, 0, 0, 0)

	if len(variantsOfGroup) == 0 {
		// если мы ни разу не дошли до конца, значит не смогли распределить на 2 группы
		// значит нет решения
		fmt.Printf("No solution")
	} else {
		for i, _ := range variantsOfGroup{
			g1[i] = n/2 - g2[i]
		}
		variants := make([][]int, len(variantsOfGroup))
		for i := 0; i < n; i++ { // рассматриваем конкретного человека
			for j, x := range variantsOfGroup{ // смотрим его принадлежность в разных вариантах групп
				if x[i] == 0 && g1[j] > 0 {
					x[i] = 1
					g1[j]--
				}
				if x[i] == 0 && g1[j] == 0 {
					x[i] = 2
				}
				variants[j] = append(variants[j], x[i])
			}
		}
		ans := variants[0]
		for _, x := range variantsOfGroup {
			if len(x) <= len(ans) {
				for i, _ := range x {
					if ans[i] > x[i] {
						copy(ans, x)
						break
					} else if ans[i] < x[i] {
						break
					}
				}
			}
		}

		for i, x := range ans {
			if x == 1 {
				fmt.Print(i+1, " ")
			}
		}
	}
}
