(define (any? f xs)
  (and (not (null? xs)) (or (f (car xs)) (any? f (cdr xs)))))

(define (all? f xs)
  (or (null? xs) (and (not (null? xs)) (and (f (car xs)) (all? f (cdr xs))))))


(any? odd? '(1 3 5 7)) ; #t
(any? odd? '(0 1 2 3)) ; #t
(any? odd? '(0 2 4 6)) ; #f
(any? odd? '())        ; #f
(display "+++++++") (newline)
(all? odd? '(1 3 5 7)) ; #t
(all? odd? '(0 1 2 3)) ; #f
(all? odd? '(0 2 4 6)) ; #f
(all? odd? '())        ; #t  Это - особенность, реализуйте её