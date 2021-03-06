package main

import "fmt"

var aarr = make([]int, 0)

func swap(i, j int) {
	aarr[i], aarr[j] = aarr[j], aarr[i]
}

func less(i, j int) bool {
	return aarr[i] < aarr[j]
}

func partition(l, r int,
	less func(i, j int) bool, ) int {
	i, j := l, l
	for j < r {
		if less(j, r) {
			swap(j, i)
			i++
		}
		j++
	}
	swap(i, r)
	return i
}

func qsortrec(l, r int,
	less func(i, j int) bool,
	swap func(i, j int)) {
	if l < r {
		q := partition(l, r, less)
		qsortrec(l, q-1, less, swap)
		qsortrec(q+1, r, less, swap)
	}
}

func qsort(n int,
	less func(i, j int) bool,
	swap func(i, j int)) {
	qsortrec(0, n-1, less, swap)
}

func main() {
	var n, x int
	fmt.Scan(&n)

	for i := 0; i < n; i++ {
		fmt.Scan(&x)
		aarr = append(aarr, x)
	}

	qsort(n, less, swap)

	for i := 0; i < n; i++ {
		fmt.Print(aarr[i], " ")
	}
}
