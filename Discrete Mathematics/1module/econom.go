package main

import (
	"fmt"
	"input"
)

var arr [][2]int
var stack []int

func addexpr(r int, str string) {
	l := stack[len(stack)-1]
	stack = stack[:len(stack)-1]
	for _, pair := range arr {
		if str[l:r] == str[pair[0]: pair[1]] {
			return
		}
	}
	p := [2]int{l,r}
	arr = append(arr, p)
}

func getexpr(str string) {
	for i, chr := range str {
		if chr == '(' {
			stack = append(stack, i)
		} else if chr == ')' {
			addexpr(i, str)
		}
	}
}

func main() {
	var str string
	str = input.Gets()
	getexpr(str)
	fmt.Println(len(arr))
}
