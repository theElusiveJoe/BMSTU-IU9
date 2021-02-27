(define-syntax my-let
  (syntax-rules ()
    ((_ ((name val) ...) expr1 . expr2)
     ((lambda (name ...) expr1 . expr2)
      val ...))))

(define-syntax my-let*
  (syntax-rules ()
    ((_ () expr1 . expr2)
     (my-let () expr1 . expr2))
    
    ((_ (с (var2 val2) ...) expr1 . expr2)
     (my-let ((var1 val1))
             (my-let* ((var2 val2) ...)
                      expr1 . expr2)))))

(my-let ((x 2) (y 3))
        (+ x y))

(my-let* ((x 2) (y (+ 2 x)) (z (+ 2 y)))