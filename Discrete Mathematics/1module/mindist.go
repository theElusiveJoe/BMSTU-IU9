package main

import (
	"fmt"
	"input"
)


func searchfst(s *string, xch, ych rune) (int, rune) {
	for i, x:= range *s {
		if x == xch {
			return i, xch
		}
		if x == ych {
			return i, ych
		}
	}
	return 0, 0
}


func search_another_and_eval_distance(s *string, lchar, rchar rune, lpos int) int{
	var res, curlen int = 1000000, 0
	for i, x:= range *s {
		//fmt.Printf("\nlchar(%d)= %#U\ns[%d]= %#U\n%d %d\n",  lpos, lchar, i, s[i], curlen, res)
		if x == lchar {
			lpos = i
			curlen = 0
			//println("shift lchar")
		} else if x == rchar {
			//println("found pair!")
			if res > curlen {
				res = curlen
				if res == 0 {
					return 0
				}
			}
			curlen = 0
			lchar, rchar = rchar, lchar
			lpos = i
		} else {
			//println("go next")
			curlen++
		}

	}
	return res
}


func main(){
	var s, x, y string
	s = input.Gets()
	input.Scanf("%s %s", &x, &y)
	xch := ([]rune)(x)[0]
	//fmt.Println(xch)
	ych := ([]rune)(y)[0]
	//fmt.Println(ych)

	//for _, ch := range a{
	//	fmt.Printf("%#U ", ch)
	//}

	pos, current := searchfst(&s, xch, ych)
	//fmt.Printf("%#U  ---  %d", current, pos)
	if current == xch {
		fmt.Println(search_another_and_eval_distance(&s, xch, ych, pos))
	} else {
		fmt.Println(search_another_and_eval_distance(&s, ych, xch, pos))
	}
}