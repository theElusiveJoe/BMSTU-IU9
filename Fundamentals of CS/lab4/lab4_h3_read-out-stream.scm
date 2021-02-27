(define (read-words path)
  (define (loop words word)
        (let ((x (read-char)))
          (cond
            ((eof-object? x) (reverse words))                             ;закончился
            ((char-alphabetic? x) (loop words (cons x word)))             ;новая буква
            ((and (char-whitespace? x) (null? word)) (loop words word))   ;очередной пробел - просто пропускаем
            (else (loop (cons (list->string (reverse word)) words) '())))))   ;слово закончилось
  
  (with-input-from-file path
    (lambda ()
      (loop '() '()))))

(read-words "doc2")
  













  


  
          