(load "stream.scm")
(load "trace.scm")


;<axiom> ::= <expr>                                                                          
;<expr> ::= <symbol><expr> | ")"<expr> | "("<expr> | <number><expr> | <space><expr> | <var><expr> | <empty>         
;                                                                                            
;<symbol> ::= "(" | ")" | + | - | * | | / | ^                                                
;                                                                                            
;<number> ::= <digit><fpart>                                                                 
;<fpart> ::= <digit><fpart> | .<digit><spart> | e<digit><tpatr>| E<digit><tpatr> | <empty>   
;<spart> ::= <digit><spart> | e<digit><tpart> |E<digit><tpart> | <empty>                     
;<tpart> ::= <digit><tpart> | <empty>                                                        
;<digit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9                                           
;                                                                                            
;<space> ::=

;<var> ::= <letter><var> | <empty>                                                           
;<letter> ::= a | A | b | B | c  | C ... z | Z                                               
;                                                                                            
;<empty> ::=                                                                                 


(define (tokenize str)
  (let* ((EOF (integer->char 0))
         (stream (make-stream (string->list str) EOF)))
    
    (define (expr stream error)
        (cond ((symbol? (peek stream))
              ; (display 1);; + - * / ^
               (cons (string->symbol (list->string (list (next stream)))) (expr stream error)))
              ((equal? (peek stream) #\))
               (next stream)
               (cons ")" (expr stream error)))
              ((equal? (peek stream) #\()
               (next stream)
               (cons "(" (expr stream error)))
              ((char-numeric? (peek stream)) ; 0 1 2 3 ...
               ;(display 2)
               (cons (number stream error) (expr stream error)))
              ((char-whitespace? (peek stream))
               ;(display 3)
               (next stream)
               (expr stream error))
              ((char-alphabetic? (peek stream)) ; a b ...
               ;(display 4)
               (cons (var stream error) (expr stream error)))
              ((equal? EOF (peek stream))
               ;(display 5)
               '())
              (else error)))
    
    (define (symbol? x)
      (member x '( #\+ #\- #\/ #\* #\^)))

    (define (number stream error)
      (string->number
       (list->string
        (cons (next stream) (fpart stream error)))))
    
      (define (fpart stream error)
      (define (loop stream error)
        (cond ((char-numeric? (peek stream))
               (cons (next stream) (loop stream error)))
              ((equal? (peek stream) #\.)
               (if (and (next stream) (char-numeric? (peek stream)))
                   (cons #\. (cons (next stream) (spart stream error)))
                   (begin
                     (display 1)
                     (error #f))))
              ((equal? (peek stream) #\e)
               (if (and (next stream) (char-numeric? (peek stream)))
                   (cons #\e (cons (next stream) (tpart stream error)))
                   (error #f)))
              ((equal? (peek stream) #\E)
               (if (and (next stream) (char-numeric? (peek stream)))
                   (cons #\E (cons (next stream) (tpart stream error)))
                   (error #f)))
              (else
               '())))
      (loop stream error))

    (define (spart stream error)
      (define (loop stream error)
        (cond ((char-numeric? (peek stream))
               (cons (next stream) (loop stream error)))
              ((equal? (peek stream) #\e)
               (if (and (next stream) (char-numeric? (peek stream)))
                   (cons #\e (cons (next stream) (tpart stream error)))
                    (error #f)))
              ((equal? (peek stream) #\E)
               (if (and (next stream) (char-numeric? (peek stream)))
                   (cons #\E (cons (next stream) (tpart stream error)))
                    (error #f)))
              (else '())))
      (loop stream error))

    (define (tpart stream error)
      (define (loop stream error)
        (cond ((char-numeric? (peek stream))
               (cons (next stream) (loop stream error)))
              (else '())))
      (loop stream error))
    
    (define (var stream error)
      (define (loop stream error)
        (cond ((char-alphabetic? (peek stream))
               (cons (next stream) (loop stream error)))
              (else '())))
      (string->symbol (list->string (loop stream error))))
    
    (call-with-current-continuation
     (lambda (error)
       (define result (expr stream error))
       (and (equal? (peek stream) EOF)
            result)))))

;(tokenize "1e1")
; (1)

;(tokenize "-1")
; (- 1)

;(tokenize "-a + b * x^2 + dy")
; (- a + b * x^ 2 + dy)

;(tokenize "(a - 1)/(b + 1)")
; ("(" a - 1 ")" / "(" b + 1 ")")


