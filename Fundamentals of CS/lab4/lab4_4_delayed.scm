(define-syntax my-if
  (syntax-rules ()
    ((_ cond? then else)
     (force (or (and cond? (delay then)) (delay else))))))



(my-if #t 1 (/ 1 0)) ; 1
(my-if #f (/ 1 0) 1) ; 1

(my-if #t #f (/ 1 0)) ;тоже работает