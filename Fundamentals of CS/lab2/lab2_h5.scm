(define (f x) (+ x 2))
(define (g x) (* x 3))
(define (h x) (- x))

(define (o . xs)
  (define (loop x xs)
    (if (null? xs)
        x
        (loop ((car xs) x) (cdr xs))))
  (lambda (x) (loop x (reverse xs))))

((o f g h) 1) ; -1
((o f g) 1) ; 5
((o h) 1) ; -1
((o) 1) ; 1