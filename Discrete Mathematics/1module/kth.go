package main

import (
	"fmt"
	"math"
)


func main() {

	var n int
	fmt.Scan(&n)
	n++ // для удобства нумеруем с 1

	numlen := 1		// 1,2,3 - 1	10,11,12 - 2 ...
	tenpownumlen := 1
	grouplen := 9	// 1...9 - 9	10...99 - 180 ...
	startnum := 1	// 1..9 - 1		10...99 - 10
	// 123456789 		} - group
	// 10111213141516171819 }
	// ...				    } - group
	//90919293949596979899  }

	//fmt.Println("\n", numlen,": len ", grouplen, "starts with ", startnum)
	for n >= startnum+grouplen {
		tenpownumlen *= 10
		startnum+=grouplen
		grouplen/=numlen
		numlen++
		grouplen*=numlen
		grouplen*=10
		//fmt.Println(numlen,": grouplen:", grouplen, "starts with:", startnum)
	}

	n--			//потому что нумеровали с 1
	startnum--

	charingroup := n - startnum
	//fmt.Println("char in group = ", charingroup)

	numberingroup := charingroup / numlen
	//fmt.Println("number in group = ", numberingroup)

	thenumber := tenpownumlen + numberingroup
	//fmt.Println("the number is ", thenumber)

	// нумерация разрядов справа<-налево
	//  начиная с единицы
	digit := numlen - charingroup%numlen
	//fmt.Println("digit -", digit)

	cyclen := int(math.Pow10(digit))
	//fmt.Println("cyclen =", cyclen)

	ans := 1
	if digit == numlen {
		ans = thenumber / (cyclen/10)
	} else {
		ans = (numberingroup % cyclen) / (cyclen / 10)
	}

	fmt.Print(ans)

}