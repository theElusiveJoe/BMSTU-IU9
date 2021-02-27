(define-syntax trace
  (syntax-rules() ;; ключевые слова
    ((_ smth);; образец
     (begin ;; шаблон
       (display 'smth)
         (display " => ")
       (let ((val smth))
         
          (write val)
          (newline)
          val)))))

  (define (zip . xss)
    (if (or (null? xss)
            (null? (trace (car xss)))) 
        '()
        (cons (map car xss)
              (apply zip (map cdr (trace xss))))))

  (zip '(1 2 3) '(one two three))

  (define counter
  (let ((c 0))
    (lambda ()
      (set! c (+ 1 c))
      c)))

(trace (counter))
(trace (/ 1 0))