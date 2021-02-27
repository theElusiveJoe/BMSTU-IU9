(define (save-data data path)
  (call-with-output-file path (lambda (p)
                                (write data p))))

(define (load-data path)
  (call-with-input-file path (lambda (p)
                              (read p))))


(define (numofstrings path)
  (define (loop strings string)
    (let ((x (read-char)))
      ;(display string)
      ;(display '-)
      ;(display strings)
      ;(newline)
      (cond
        ((and (eof-object? x) (null? string)) strings)
        ((and (eof-object? x) (not (null? string))) (+ 1 strings))
        ((and (equal? x #\newline) (null? string)) (loop strings string))
        ((and (equal? x #\newline) (not (null? string))) (loop (+ 1 strings) '()))
        ((char-whitespace? x) (loop strings string))
        (else (loop strings (cons x string))))))
  (with-input-from-file path
    (lambda ()
      (loop 0 '()))))

(save-data (list 1 2 3 4) "1234.txt")
(load-data "1234.txt")
(apply * (load-data "1234.txt")) ;; теперь работает

