
(define (quadratic a b c)
  (cond
    ((and (= a 0)  (= b 0) (= c 0)) (display "unlimited number of roots"))
    ((and (= a 0)  (= b 0)) (display "no roots"))
    ((= a 0) (/ (- c) b))
    ((< (- (* b b) (* 4 a c)) 0) (list))
    (( = (- (* b b) (* 4 a c)) 0) (list (/ (- b) (* 2 a))))
    (else (list (/ (- (- b) (sqrt (- (* b b) (* 4 a c))))(* 2 a)) (/ (+ (- b) (sqrt (- (* b b) (* 4 a c))))(* 2 a))))))


(define (show a b c)
  (begin
    (write a) (display " ") (write b) (display " ") (write c) (display "  - ")
    (quadratic a b c)))

;(define (disc a b c)
; (- (* b b) (* 4 a c)))

(show 0 0 0) (newline); unlimited number of roots
(show 0 0 1) (newline); no roots
(show 0 1 5) ; -5
(show 2 1 5) ; void list ()
(show 1 -2 1) ; (1)
(show 1 5 -6) ; (-6 1)



