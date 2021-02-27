;исполнялка
(define-syntax leval
  (syntax-rules ()
    ((_ xs) (eval xs (interaction-environment)))))

;определяет функцию-мейкер
(define-syntax define-maker
  (syntax-rules ()
    ((_ name (xs ...))
     (leval
      (list 'define
            (list (string->symbol (string-append "make-" (symbol->string 'name))) ;имя функции
                  (string->symbol (string-append "p_" (symbol->string 'xs))) ... ) ;параметры функции
            (list 'list ''name (list 'list ''xs (string->symbol(string-append "p_" (symbol->string 'xs))))
                  ...))))))

;предикат структуры
(define-syntax define-checker
  (syntax-rules ()
    ((_ name)
     (leval
      (list 'define
            (list (string->symbol (string-append (symbol->string 'name) "?"))
                  'param)
            '(and (list? param) (equal? (car param) 'name)))))))

;геттер
(define-syntax define-getter
  (syntax-rules ()
    ((_ name (subname))
     (leval
      (list 'define
            (list (string->symbol (string-append (symbol->string 'name) "-" (symbol->string 'subname)))
                  'param)
            '(cadr (assoc 'subname (cdr param)))))))) 

;геттеры
(define-syntax define-getters
  (syntax-rules ()
    ((_ name (xs))
     (define-getter name (xs)))
   ((_ name (x xs ...))
    (begin (define-getter name (x)) (define-getters name (xs ...))))))

;сеттер
(define-syntax define-setter
  (syntax-rules ()
    ((_ name (subname))
     (leval
      (list 'define
            (list (string->symbol (string-append "set-" (symbol->string 'name) "-" (symbol->string 'subname) "!"))
                  'param 'val)
            '(set-car! (cdr (assoc 'subname (cdr param))) val))))))

;сеттеры
(define-syntax define-setters
  (syntax-rules ()
    ((_ name (xs))
     (define-setter name (xs)))
   ((_ name (x xs ...))
    (begin (define-setter name (x)) (define-setters name (xs ...))))))

;дефайнит всю структуру
(define-syntax define-struct
  (syntax-rules ()
    ((_ name (xs ...))
     (begin
       (define-maker name (xs ...))
       (define-checker name)
       (define-getters name (xs ...))
       (define-setters name (xs ...))))))

(define-struct pos (row col)) ; Объявление типа pos
(define p (make-pos 1 2))     ; Создание значения типа pos

(pos? p)    ; #t

(pos-row p) ; 1
(pos-col p) ; 2

(set-pos-row! p 3) ; Изменение значения в поле row
(set-pos-col! p 4) ; Изменение значения в поле col

(pos-row p) ; 3
(pos-col p) ; 4



