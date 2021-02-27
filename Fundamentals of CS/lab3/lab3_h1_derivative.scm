;(load "trace and test.csm")
;(load "simplify.csm")

(define (derivative xs)
  (define (der xs)
    (if (or (not (list? xs)) (= (length xs) 1)) ;; не выражение
        (if (list? xs)
            (cond ((equal? (car xs) 'x) 1)
                  ((equal? (car xs) '-x) -1)
                  (0))
            (if (or (equal? xs 'x))
                1
                0))
        ;; какое-то выражение
        (cond
          ;; (* a b)   ;; нет поддержки 'x*x'
          ((equal? (car xs) '*)
           (if (= (length xs) 3)
               (let ((b (cadr xs)) (c (caddr xs)))
                 (if (not (or (list? b) (list? c))) ;; вида expr * x 
                     (if (and (equal? b 'x) (equal? c 'x))
                         '(* 2 x)
                         (if (equal? 'x b)
                             c
                             b))
                     (list '+ (list '* b (der c)) (list '* (der b) c))))
               (let ((b (cadr xs)) (c (cons '* (cddr xs))))
                 (der (list '* b c))
                 )))

          ;;(+ a b)
          ((equal? (car xs) '+)
           (cons '+ (map der xs)))

          ;;(- a b)
          ((equal? (car xs) '-) 
           (cons '- (cons (der (cadr xs)) (map der (cddr xs)))))

          ;; (expt x n)
          ((equal? (car xs) 'expt) 
           (let ((b (cadr xs)) (c (caddr xs)))
             
             (if (equal? b 'e)
                 (if (list? c)
                     (list '* (der c) xs)
                     xs)
                 (cond
                   ((and (equal? b 'x) (number? c))  ; x^c
                    (list '* c (list 'expt b (- c 1))))
                   ((and (list? b) (number? c))  ; e^c
                    (list '* c (list 'expt b (- c 1)) (der b)))
                   ((and (number? b) (equal? c 'x))  ; c^x
                    (list '* (list 'log c) xs))
                   ((and (list? b) (equal? c 'x))  ; e^x
                    (list '* (list 'log c) xs))
                   ((and (number? b) (list? c))  ; c^e
                    (list '* xs (der c) (list 'log c)))
                   ((list '+ (list '* c (list 'expt b (list '- c 1)) (der b)) ; e^e x^e
                          (list '* (list 'expt b c) (der c) (list 'log b)))))))) 

          ;; (a/b)
          ((equal? (car xs) '/)
           (let ((b (cadr xs)) (c (caddr xs)))
             (der (list '* b (list 'expt c -1)))))

          ;;(log n)
          ((equal? (car xs) 'log)
           (let ((b (cadr xs)))
             (if (list? b)
                 (list '*  (der b) (list 'expt b -1))
                 (list 'expt b -1))))
          
          ;;(sin x)
          ((equal? (car xs) 'sin)
           (let ((b (cadr xs)))
             (if (list? b)
                 (list '*  (der b) (list 'cos b))
                 (list 'cos b))))

          ;;(cos x)
          ((equal? (car xs) 'cos)
           (let ((b (cadr xs)))
             (if (list? b)
                 (list '*  (der b) (list '- (list 'sin b)))
                 (list '- (list 'sin b)))))
          )))
  (der xs))


(define x1 '(2))
(define x2 '(x))
(define x3 '(-x))
(define x4 '(* 1 x))
(define x5 '(* -1 x))
(define x6 '(* -4 x))
(define x7 '(* 10 x))
(define x8 '(- (* 2 x) 3))
(define x9 '(expt x 10))
(define x10 '(* 2 (expt x 5)))
(define x11 '(expt x -2))
(define x12 '(expt 5 x))
(define x13 '(cos x))
(define x14 '(sin x))
(define x15 '(expt 2 x))
(define x16 '(* 2 (expt 2 (* 2 x))))
(define x17 '(log x))
(define x18 '(* 3 (log x)))
(define x19 '(+ (expt x 3) (expt x 2)))
(define x20 '(- (* 2 (expt x 3)) (* 2 (expt x 2))))
(define x21 '(/ 3 x))
(define x22 '(/ 3 (* 2 (expt x 2))))
(define x23 '(* 2 (expt e x) (sin x) (cos x)))
(define x24 '(sin (* 2 x)))
(define x25 '(cos (* 2 (expt x 2))))
(define x26 '(sin (log (expt x 2))))
(define x27 '(+ (sin (* 2 x)) (cos(* 2 (expt x 2)))))
(define x28 '(* (sin (* 2 x)) (cos(* 2 (expt x 2)))))


(define the-tests
  (list
   (test (derivative x1) 0)
   (test (derivative x3) -1)
   (test (derivative x4) 1)
   (test (derivative x8) '(- 2 0))
   (test (derivative x25) '(* (+ (* 2 (* 2 (expt x 1))) (* 0 (expt x 2))) (- (sin (* 2 (expt x 2))))))
   (test (derivative x26) '(* (* (* 2 (expt x 1)) (expt (expt x 2) -1)) (cos (log (expt x 2)))))
   (test (derivative x27) '(+ 0 (* 2 (cos (* 2 x))) (* (+ (* 2 (* 2 (expt x 1))) (* 0 (expt x 2))) (- (sin (* 2 (expt x 2)))))))))

(run-tests the-tests)

(define (check xs)
  (if (null? xs)
      (display 'done)
      (begin
        (let* (
               (a (caar xs))
               (b (eval a (interaction-environment)))
               (c (eval (list (list 'lambda '(x) b) 0.9) (interaction-environment)))
               (d (cadr(car xs)))
               (e (eval (list (list 'lambda '(x) d) 0.9) (interaction-environment))))
          (if (> (abs(- c e)) 0.001)
              (begin
                (display "wrong in ")
                (display (cadr(caar xs)))
                (newline)))
          (check (cdr xs))))
      ))

(check the-tests)
























