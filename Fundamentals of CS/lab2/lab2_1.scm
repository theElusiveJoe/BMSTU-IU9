(define (count x xs)
  (define (loop x xs i)
    (if (null? xs)
        i
        (if (equal? (car xs) x)
            (loop x (cdr xs) (+ i 1))
            (loop x (cdr xs) i))))
  (loop x xs 0))

(count 'a '(a b c a))  ; 2
(count 'b '(a c d))    ; 0
(count 'a '())         ; 0