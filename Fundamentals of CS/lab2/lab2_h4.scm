(define (make-multi-vector sizes . fill)
  (let ((m (make-vector ( + 1 (apply * sizes)))))
    (if (not (null? fill))
        (vector-fill! m (car fill)))
    (vector-set! m 0 "ILOVEBOMONKA")
    m))

(define (multi-vector? m)
  (and (vector? m) (equal? (vector-ref m 0) "ILOVEBOMONKA")))

(define (multi-vector-ref m indices)
  (vector-ref m (apply * (map (lambda (x) (+ 1 x)) indices))))

(define (multi-vector-set! m indices x)
  (vector-set! m (apply * (map (lambda (x) (+ 1 x)) indices)) x))

(define m (make-multi-vector '(11 12 9 16)))
(multi-vector? m)
(multi-vector-set! m '(10 7 6 12) 'test)
(multi-vector-ref m '(10 7 6 12)) ; test

(define m (make-multi-vector '(3 5 7) -1))
(multi-vector-ref m '(0 0 0)) ; -1