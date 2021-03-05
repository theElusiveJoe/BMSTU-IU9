package main

import "fmt"
import "math/big"

func multmatrix(a, b [4]big.Int) [4]big.Int {
	x := big.NewInt(0)
	var res [4]big.Int
	for i := 0; i < 2; i++ {
		for j := 0; j < 2; j++ {
			for k := 0; k < 2; k++ {
				x.Mul(&a[i*2+k], &b[k*2+j])
				res[i*2+j].Add(x, &res[i*2+j])
			}
		}
	}
	return res
}

func main() {
		var n int
		fmt.Scan(&n)
		n--
		pow := [4]big.Int{*big.NewInt(1), *big.NewInt(1), *big.NewInt(1), *big.NewInt(0)}
		res := [4]big.Int{*big.NewInt(1), *big.NewInt(0), *big.NewInt(0), *big.NewInt(1)}
		for n > 0 {
			if n&1 == 1 {
				res = multmatrix(res, pow)
			}
			pow = multmatrix(pow, pow)

			n/=2
		}
		x := big.NewInt(0)
		fmt.Println(x.Add(&res[2], &res[3]))

}
