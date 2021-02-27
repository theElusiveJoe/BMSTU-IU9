(define memorized-factorial
  (let ((memo '()))
        (lambda (x)
          (if (assoc x memo)
              (cadr (assoc x memo))
              (let ((res (cond
                           ((= x 1) 1)
                           (else (* x (memorized-factorial (- x 1)))))))
                (set! memo
                      (cons (list x res) memo))
                res)))))

(begin
  (display (memorized-factorial 8)) (newline)
  (display (memorized-factorial 550000)) (newline))