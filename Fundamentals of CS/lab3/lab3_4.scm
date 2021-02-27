(load "trace and test.csm")

(define (factorize xs)
  (let* ((sign (car xs))
         (first (cadr xs)) (second (caddr xs))
         (ffoo (car first)) (sfoo (car second))
         (x (cadr first)) (y (cadr second))
         (fdegree (caddr first)) (sdegree (caddr second)))
    
    (begin
      ;(trace sign)     ;sign - знак
      ;(trace first)    ;first - первая скобка
      ;(trace second)   ;second - вторая
      ;(trace ffoo)     ;ffoo - expt?
      ;(trace sfoo)     ;sfoo - expt?
      ;(trace x) (trace y)   ;x y - очевидно
      ;(trace fdegree)  ;fdegree - степень x
      ;(trace sdegree)  ;sdegree - степень y
    
      (if (and  (equal? '- sign) (equal? fdegree 2) (equal? sdegree 2)) ;; a2-b2
          (list '* (list '- x y) (list '+ x y))
          (if (and (equal? '- sign) (equal? fdegree 3) (equal? sdegree 3)) ;; a3-b3
              (list '* (list '- x y)
                    (list '+ (list 'expt x 2)
                          (list '* x y)
                          (list 'expt y 2)))
              (if (and (equal? '+ sign) (equal? fdegree 3) (equal? sdegree 3)) ;; a3+b3
                  (list '* (list '+ x y)
                        (list '+ (list 'expt x 2)
                              (list '* -1 x y)
                              (list 'expt y 2)))
                  "я такое не умею("))))))

(define x1 '(- (expt x 2) (expt y 2)))
(define x2 '(- (expt x 3) (expt y 3)))
(define x3 '(+ (expt x 3) (expt y 3)))
(define x4 '(* (expt x 4) (expt y 3)))
(define x5 '(* (- x) (+ x y)))

(define the-tests
  (list (test (factorize x1) '(* (- x y) (+ x y)))
        (test (factorize x2)  '(* (- x y) (+ (expt x 2) (* x y) (expt y 2))))
        (test (factorize x3)  '(* (+ x y) (+ (expt x 2) (* -1 x y) (expt y 2))))))

(run-tests the-tests)







  
;(factorize '(- (expt (+ first 1) 2) (expt (- second 1) 2)))
; (* (- (+ first 1) (- second 1)) (+ (+ first 1) (- second 1)))
             
;(eval (list (list 'lambda 
;         '(x y) 
;        (factorize '(- (expt x 2) (expt y 2))))
;     1 2)
;   (interaction-environment))
; -3