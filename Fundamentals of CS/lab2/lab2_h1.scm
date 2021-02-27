(define (my-range a b d)
  (if (< a b)
      (cons a (my-range (+ a d) b d))
      '()))

(my-range 0 11 3)
(newline)
;=========================

(define (my-flatten xs)
  (cond
    ((null? xs)
     '())
    ((pair? xs)
     (append (my-flatten (car xs)) (my-flatten (cdr xs))))
    (else
     (list xs))))

(my-flatten '((1) 2 (3 (4 5)) 6))
(newline)

;==========================

(define (my-element? x xs)
  (and (not (null? xs)) (or (equal? x (car xs)) (my-element? x (cdr xs)))))

(my-element? 1 '(3 2 1)) ; #t
(my-element? 4 '(3 2 1)) ; #f
(newline)

;==========================

(define (my-filter pred? xs)
  (define (loop xnews xs)
    (if (null? xs)
        xnews
        (if (pred? (car xs))
            (loop (cons (car xs) xnews) (cdr xs))
            (loop xnews (cdr xs)))))
  (reverse (loop '() xs)))

(my-filter odd? (my-range 0 10 1)) ; (1 3 5 7 9)
(my-filter (lambda (x) (= (remainder x 3) 0)) (my-range 0 13 1)) ; (0 3 6 9 12)
(newline)

;==========================

(define (my-fold-left op xs)
  (define (loop x xs)
    (if (null? xs)
        x
        (loop (op x (car xs)) (cdr xs))))
  (if (null? xs)
      '()
      (loop (car xs) (cdr xs))))
              
(my-fold-left  quotient '(16 2 2 2 2)) ; 1

(define (my-fold-right op xs)
      (my-fold-left op (reverse xs)))

(my-fold-right expt '(2 3 4)) ; 4096












