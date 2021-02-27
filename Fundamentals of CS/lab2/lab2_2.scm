(define (delete f xs)
  (if (null? xs)
      '()
      (if (f (car xs))
          (delete f (cdr xs))
          (cons (car xs) (delete f (cdr xs))))))
          






(delete even? '(0 1 2 3)) ; (1 3)
(delete even? '(0 2 4 6)) ; ()
(delete even? '(1 3 5 7)) ; (1 3 5 7)
(delete even? '())        ; ()