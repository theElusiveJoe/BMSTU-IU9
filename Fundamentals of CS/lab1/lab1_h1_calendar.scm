(define (day-of-week d m y)
  (if(< m 3)
     (remainder (+ 1 (remainder(+ d 3 (- y 1) (quotient (- y 1) 4) (-(quotient (- y 1) 100)) (quotient (- y 1) 400) (quotient(+ (* 31 m) 10) 12)) 7) ) 7)
     (remainder (+ 1 (remainder(+ d y (quotient y 4) (-(quotient y 100)) (quotient y 400) (quotient(+ (* 31 m) 10) 12)) 7) )   7)))



(day-of-week 1 1 2020) ; 3
(day-of-week 1 10 1950) ; 0
(day-of-week 1 1 1700) ; 5

;некоторый нормальный язык: w:= 1 + [d + y + y/4 – y/100 + y/400 + (31m+10)/12] mod 7;
;ским: (+ 1 (remainder(+ d y (quotient y 4) (-(quotient y 100)) (quotient y 400) (quotient(+ (* 31 m) 10) 12)) 7)

