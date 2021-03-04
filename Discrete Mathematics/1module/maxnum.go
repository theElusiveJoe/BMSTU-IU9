package main

import "fmt"

func getbiggestdigit(x int) int{
	for x >= 10 {
		x/=10
	}
	return x
}


func digitalicy(x int) int {

	i := 1
	for x > 0 {
		i*=10
		x/=10
	}
	return i
}


func cmp(a, b int) int{
	if a == 0{
		return -1
	}
	if b == 0{
		return 1
	}
	return (a*digitalicy(b)+b)-(b*digitalicy(a)+a)
}


func insort(s []int){
	len := len(s)
	for i :=1; i < len; i++ {
		j := i
		for j > 0 {
			if cmp(s[j-1], s[j]) <= 0 {
				s[j-1], s[j] = s[j], s[j-1]
			}
			j--
		}
	}
}


func main() {
	var n, t int
	fmt.Scan(&n)

	var s []int
	for i:= 0; i < n; i++ {
		fmt.Scan(&t)
		s = append(s, t)
	}
	insort(s)
	for i := range s{
		fmt.Print(s[i])
	}

}