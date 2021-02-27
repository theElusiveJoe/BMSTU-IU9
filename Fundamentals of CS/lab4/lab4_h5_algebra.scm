;исполнялка
(define-syntax leval
  (syntax-rules ()
    ((_ xs) (eval xs (interaction-environment)))))

(define-syntax define-type
  (syntax-rules ()
    ((_ name args ...)
     (leval '(define (name args ...) (list 'name args ...)))))) 

(define-syntax define-checker
  (syntax-rules ()
    ((_ commonname name ...)
     (leval
      (list 'define
            (list (string->symbol (string-append (symbol->string 'commonname) "?")) 'x)
            '(and (list? x) (member (car x) (list 'name ...))) #t)))))

(define-syntax define-data
  (syntax-rules ()
    ((_ commonname ((name args ...) ...))
     (begin
       (define-type name args ...) ...
       (newline)
       (define-checker commonname name ...)))))



; Определяем тип
;
(define-data figure ((square a)
                     (rectangle a b)
                     (triangle a b c)
                     (circle r)))

; Определяем значения типа

(define s (square 10))
(define r (rectangle 10 20))
(define t (triangle 10 20 30))
(define c (circle 10))

; Пусть определение алгебраического типа вводит
; не только конструкторы, но и предикат этого типа:
;
(and (figure? s)
     (figure? r)
     (figure? t)
     (figure? c)) ; #t





;***********************************
(define (create-let-list f pattern letlist)
  (if (null? pattern)
      letlist
      ;(triangle 10 20 30)    (triangle a b c) (+ a b c) 
      ;   1           12           3       34
      (let ((one (car f))
            (two (cdr f))
            (three (car pattern))
            (four (cdr pattern)))
        (if (symbol? one)
            (and (equal? one three)
                 (create-let-list two four letlist))
            (create-let-list two four (cons (list three one) letlist))))
      ))

(define (evaler letlist expr)
  (leval `(let ,letlist ,expr)))

(define (create-match f longlist)
  (let loop ((xs longlist))
    (and (not (null? xs))
         ;   ((square a)       (* 4 a))  ((rectangle a b)  (* 2 (+ a b)))   (* 2 pi r))))
         ;         1              3            1                  3
         (let* ((one (caar xs))
                (three (cadar xs))
                (letlist (create-let-list f one '())))
           (if letlist
               (evaler letlist three)
               (loop (cdr xs)))))))


     

(define-syntax match
  (syntax-rules ()
    ((_ f (pattern expr) ...) (create-match f '((pattern expr) ...)))))
;***********************************

(define pi (acos -1)) ; Для окружности
  
(define (perim f)
  (match f 
    ((square a)       (* 4 a))
    ((rectangle a b)  (* 2 (+ a b)))
    ((triangle a b c) (+ a b c))
    ((circle r)       (* 2 pi r))))
  
(perim s) ; 40
(perim r) ; 60
(perim t) ; 60