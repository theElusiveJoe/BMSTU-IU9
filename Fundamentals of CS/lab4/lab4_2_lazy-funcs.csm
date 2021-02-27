(define-syntax lazy-cons
  (syntax-rules ()
    ((_ a b) (cons a (delay b)))))

(define (lazy-car xp)
  (car xp))

(define (lazy-cdr xp)
  (force (cdr xp)))

;(define p (lazy-cons 1 (/ 1 0)))
;(lazy-car p)
;(lazy-cdr p)

(define (lazy-head xs k)
  (define (loop xs k xy)
    (if (= k 0)
      (reverse xy)
      (loop (lazy-cdr xs) (- k 1) (cons (lazy-car xs) xy))))
  (loop xs k '()))

(define (lazy-ref xs k)
    (if (= k 1)
      (lazy-car xs)
      (lazy-ref (lazy-cdr xs) (- k 1))))

(define (naturals start)
  (lazy-cons start (naturals (+ 1 start))))

(define (lazy-factorial)
  (define (loop x prod)
    (lazy-cons (* x prod) (loop (+ x 1) (* x prod))))
  (loop 1 1))

(lazy-head (naturals 10) 12) ;(10 11 12 13 14 15 16 17 18 19 20 21)
(lazy-ref (naturals 10) 12)

(lazy-ref (lazy-factorial) 10)
