(define (string-trim-left st)
  (define (loop xs)
    (if (null? xs)
        (list -> string '())
        (if (char-whitespace? (car xs))
            (loop (cdr xs))
            (list->string xs))))
  (loop (string->list st)))

(string-trim-left  "\t\t\n  abc def")   ; "abc def"

(define (string-trim-right st)
  (define (loop xs)
    (if (null? xs)
        '()
        (if (char-whitespace? (car xs))
            (loop (cdr xs))
            xs)))
  (list->string(reverse(loop (reverse (string->list st))))))

(string-trim-right "abc def\t \n")     ; "abc def"

(define (string-trim st)
  (string-trim-left (string-trim-right st)))

(string-trim "\t abc def \n") ; "abc def"
(newline)

;=======================================

(define (string-prefix? a b)
  (define (loop xs xy)
    (or (null? xs) (and (not (null? xy)) (equal? (car xs) (car xy)) (loop (cdr xs) (cdr xy)))))
  (loop (string->list a) (string->list b)))

(string-prefix? "abc" "abcdef")  ; #t
(string-prefix? "bcd" "abcdef")  ; #f
(newline)

;=======================================

(define (string-suffix? a b)
  (define (loop xs xy)
    (or (null? xs) (and (not (null? xy)) (equal? (car xs) (car xy)) (loop (cdr xs) (cdr xy)))))
  (loop (reverse (string->list a)) (reverse (string->list b))))

(string-suffix? "def" "abcdef")  ; #t
(string-suffix? "bcd" "abcdef")  ; #f
(newline)

;=======================================

(define (help-infix xs xy)
  (or (null? xs) (and (not (null? xy)) (equal? (car xs) (car xy)) (help-infix (cdr xs) (cdr xy)))))

(define (string-infix? a b)
  (define (help-infix xs xy)
    (or (null? xs) (and (not (null? xy)) (equal? (car xs) (car xy)) (help-infix (cdr xs) (cdr xy)))))
  (define (loop xs xy)
    (and (not (null? xy)) (or (help-infix xs xy) (loop xs (cdr xy)))))
  (loop (string->list a) (string->list b)))
  
(string-infix? "def" "abcdefgh") ; #t
(string-infix? "abc" "abcdefgh") ; #t
(string-infix? "fgh" "abcdefgh") ; #t
(string-infix? "ijk" "abcdefgh") ; #f
(newline)

;=======================================

(define (string-split str sep) ; xs - исходная строка
  ; xy - сепаратор
  
  (define (cut-from-start xs xy); ok
    (if (null? xy)
        xs
        (cut-from-start (cdr xs) (cdr xy))))
  
  (define (starts-with? xs xy); ok
    (or (null? xy) (and (not (null? xs)) (equal? (car xy) (car xs)) (starts-with? (cdr xs) (cdr xy)))))
  
  (define (loop xs xy ourlist templist)
    (if (null? xs) ; если список кончился
        (if (null? templist)
            (reverse ourlist)   
            (reverse (cons (list->string templist) ourlist))) ; то выводим результат
        (if (starts-with? xs xy); если наткнулись на сепаратор
            (loop (cut-from-start xs xy) xy (cons (list->string templist) ourlist) '())
            ; то вырезаем его, а строку закидываем в список, строку обнуляем
            (loop (cdr xs) xy ourlist (reverse (cons (car xs) templist))))))
  ; или же ищем сепаратор дальше, а первый символ записываем во временную строку
  (loop (string->list str) (string->list sep) '() '()))
        
(string-split "x;y;z" ";")       ; ("x" "y" "z")
(string-split "xx-->yy-->" "-->") ; ("x" "y" "z")      














  
  





















