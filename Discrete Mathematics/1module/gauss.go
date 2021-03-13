package main

import (
	"fmt"
)

type frac struct {
	num, den int
}

func addFrac(a, b frac) frac {
	var c frac
	c.num = a.num*b.den + b.num*a.den
	c.den = a.den * b.den
	c = beautify(c)
	return c
} // a + b

func abs(x int) int {
	if x > 0 {
		return x
	} else {
		return -x
	}
}

func subtractFrac(a, b frac) frac {
	var c frac
	c.num = a.num*b.den - b.num*a.den
	c.den = a.den * b.den
	c = beautify(c)
	return c
} // a - b

func subtractLine(a *[][]frac, n, line1, line2 int) { // k = k - l
	for j := 0; j < n+1; j++ {
		(*a)[line1][j] = subtractFrac((*a)[line1][j], (*a)[line2][j])
	}
}

func beautify(f frac) frac {
	if f.num == 0 {
		f.den = 1
		return f
	}

	a, b := abs(f.num), abs(f.den)
	for a != 0 && b != 0 {
		if a > b {
			a %= b
		} else {
			b %= a
		}
	}
	f.num, f.den = f.num/(a+b), f.den/(a+b)
	if f.den < 0 {
		f.num, f.den = f.num*(-1), f.den*(-1)
	}
	return f
}

func beautifyMatrix(a *[][]frac) {
	for _, line := range *a {
		for _, elem := range line {
			elem = beautify(elem)
		}
	}
}

func makeOnes(a *[][]frac, lineNum, n int) {
	for i := lineNum; i < n; i++ {
		if (*a)[i][lineNum].num != 0 {
			num := (*a)[i][lineNum].num
			den := (*a)[i][lineNum].den
			for j := lineNum; j < n+1; j++ {
				if (*a)[i][j].num != 0 {
					(*a)[i][j].den *= num
					(*a)[i][j].num *= den
				}
			}
		}
	}
}

func setOneOnTop(a *[][]frac, lineNum, n int) {
	if (*a)[lineNum][lineNum].num != 0 {
		return
	}
	for i := lineNum + 1; i < n; i++ {
		if (*a)[i][lineNum].num != 0 {
			swapLines(a, lineNum, i)
			return
		}
	}

	return
}

func swapLines(a *[][]frac, k, l int) {
	(*a)[k], (*a)[l] = (*a)[l], (*a)[k]
}

func columnToZero(a *[][]frac, lineNum, n int) {
	for i := lineNum + 1; i < n; i++ {
		if (*a)[i][lineNum].num != 0 {
			subtractLine(a, n, i, lineNum)

		}
	}
}

func toStairType(a *[][]frac, n int) {
	for i := 0; i < n-1; i++ {
		makeOnes(a, i, n)
		setOneOnTop(a, i, n)
		columnToZero(a, i, n)
		beautifyMatrix(a)
	}
}

func rank(a *[][]frac, n int) frac {
	var f frac
	f.num, f.den = 1, 1
	for i := 0; i < n; i++ {
		if (*a)[i][i].num == 0 {
			return (*a)[i][i]
		}
	}
	return f
}

func printMatrix(a [][]frac, n int) {
	fmt.Println()
	for i := 0; i < n; i++ {
		for j := 0; j < n+1; j++ {
			fmt.Print(a[i][j].num, "/", a[i][j].den, " ")
		}
		fmt.Println()
	}
}

func main() {
	var n, x int
	var f frac
	f.den = 1
	fmt.Scan(&n)
	a := make([][]frac, n)
	for i := 0; i < n; i++ {
		for j := 0; j < n+1; j++ {
			fmt.Scan(&x)
			f.num = x
			a[i] = append(a[i], f)
		}
	}

	toStairType(&a, n)

	if rank(&a, n).num == 0 {
		fmt.Println("No solution")
		return
	}

	res := make([]frac, n)        // вектор-столбец - результат
	for i := n - 1; i >= 0; i-- { // считаю результат снизу вверх
		// в результат записываю свободный член
		res[i].num = a[i][n].num
		res[i].den = a[i][n].den
		for j := n - 1; j >= i+1; j-- {
			// в f записываю уже известный икс
			f.num = res[j].num
			f.den = res[j].den
			// помножаю на коэффициент при известном икс
			f.num *= a[i][j].num
			f.den *= a[i][j].den
			//вычитаю из результата
			res[i] = subtractFrac(res[i], f)
		}
		res[i].num *= a[i][i].den
		res[i].den *= a[i][i].num
		res[i] = beautify(res[i])
	}

	for _, fr := range res {
		fmt.Print(fr.num, "/", fr.den, " ")
	}
}
