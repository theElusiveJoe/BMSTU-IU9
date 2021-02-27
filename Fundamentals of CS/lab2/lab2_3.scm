(define (iterate f x n)
  (if (= n 0)
      '()
      (cons x (iterate f (f x) (- n 1)))))

(iterate (lambda (x) (* 2 x)) 1 6) ; (1 2 4 8 16 32)
(iterate (lambda (x) (* 2 x)) 1 1) ; (1)
(iterate (lambda (x) (* 2 x)) 1 0) ; ()
