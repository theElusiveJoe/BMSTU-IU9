(define (signum x)
  (cond
    ((< x 0) -1)
    ((= x 0)  1) ; Ошибка здесь!
    (else     1)))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define-syntax test
  (syntax-rules ()
    ((_ expr expect)
     (list (quote expr) expect))))

(define (run-test xs) 
  (begin 
    ;(display (car xs))
    (let ((res (eval (car xs) (interaction-environment))))
      (if (equal? res (cadr xs))
          (newline)(display "OK \n")
          (begin
            (display " FAIL \nexpected: ")
            (display (cadr xs))
            (newline)
            (display "returned: ")
            (display res)
            (newline)
            #f)))))
          


(define (run-tests xs)
  (define (loop xs i)
    (if (null? xs)
        i
        (loop (cdr xs) (and i (car xs)))))
  (loop (map run-test xs)  #t))

(define the-tests
  (list (test (signum -2) -1)
        (test (signum  0)  0)
        (test (signum  2)  1)))


(run-tests the-tests)






