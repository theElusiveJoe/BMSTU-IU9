;;;; 1

(define (my-gcd a b)
  (if (= b 0)
      (abs a)
      (my-gcd b (remainder a b))))

(my-gcd 10 5) ; 5 everywhere
(my-gcd 5 10) 
(my-gcd 10 -5) 
(my-gcd -5 10)
(my-gcd -5 -10)

;;2
(define (my-lcm a b)
  (/ (abs (* a b))(my-gcd a b)))

(my-lcm -9 13) ; 117
(my-lcm 12 18) ; 36


;;3
(define (prime? a)
  (and (not ( = (abs a) 1)) (prime2 (abs a) 2)))

(define (prime2 a b)
  (or (not (> a (* 2 b))) (and (not (= (remainder a b) 0)) (prime2 a (+ b 1)))))
  

(prime? -25)
(prime? 1)
(prime? -13)