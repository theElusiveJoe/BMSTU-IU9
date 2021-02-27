(define-syntax trace
  (syntax-rules() ;; ключевые слова
    ((_ smth);; образец
     (begin ;; шаблон
       (let ((val smth))
         (display 'smth)
         (display " => ")
         (display val)
         (newline)
         smth)))))

(define-syntax test
  (syntax-rules ()
    ((_ expr expect)
     (list (quote expr) expect))))

(define (run-test xs) 
  (begin 
    (display (car xs))
    (let ((res (eval (car xs) (interaction-environment))))
    (if (equal? res (cadr xs))
        (display "OK \n")
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
