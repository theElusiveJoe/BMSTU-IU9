(define trib
  (let ((memo '()))
    (lambda (n)
      (if (assoc n memo)
          (cadr (assoc n memo))
          (let ((res (cond
                       ((or (= n 1) (= n 0)) 0)
                       ((= n 2) 1)
                     (else (+
                            (trib (- n 1))
                            (trib (- n 2))
                            (trib (- n 3)))))))
          (set! memo 
                (cons (list n res) memo))
          res)))))




(trib 10010)
(trib 10010)
