(load "trace and test.csm")

(define (ref xx pos num)
  (define (looplist xs ys n pos)
    (if (= pos 0)
        (append (reverse (cons n xs)) ys)
        (looplist (cons (car ys) xs) (cdr ys) n (- pos 1))))

  
  (if (list? xx)
      (and (not (< pos 0))
           (not  (> pos (length xx)))
           (looplist '() xx num pos))

      (if (vector? xx)
          (and (not (< pos 0))
               (not  (> pos (vector-length xx)))
               (list->vector (looplist '() (vector->list xx) num pos)))
          
          (if (string? xx)
              (begin
                (and (char? num)
                     (and (not (< pos 0))
                          (not (> pos (string-length xx)))
                          (list->string (looplist '() (string->list xx) num pos)))))))))


(ref '(1 2 3) 1 0)   ; (1 0 2 3)
(ref #(1 2 3) 1 0)   ; #(1 0 2 3)
(ref #(1 2 3) 1 #\0) ; #(1 #\0 2 3)
(ref "123" 1 #\0)    ; "1023"
(ref "123" 1 0)      ; #f
(ref "123" 3 #\4)    ; "1234"
(ref "123" 5 #\4)    ; #f
(ref '(a b c) 3)
(test (ref '(1 2 3) 1 0) '(1 0 2 3))