(load "stream.scm")
(load "trace.scm")
(load "h1_lexer.scm")

;Expr1   ::= Term1 Expr2 .
;Expr2   ::= AddOp Term1 Expr2 | .
;Term1    ::= Factor Term2 .
;Term2   ::= MulOp Factor Term2 | .
;Factor  ::= Power Factor2 .
;Factor2 ::= PowOp Power Factor2 | .
;Power   ::= value | "(" Expr1")" | unaryMinus Power .

(define (parse lst)
  (let* ((EOF (integer->char 0))
         (stream (make-stream lst EOF)))
  
    
    (define (expr stream error)
      (let loop ((t (term stream error)))
        (cond ((member (peek stream) '(+ -))
               (loop (list t (next stream) (term stream error))))
              (else t))))
  
    (define (term stream error)
      (let loop ((t (factor stream error)))
        (cond ((member (peek stream) '(* /))
               (loop (list t (next stream) (factor stream error))))
              (else t))))
    
    (define (factor stream error)
      (let loop ((t (power stream error)))
        (cond ((equal? (peek stream) '^)
               (loop (list t (next stream) (factor stream error))))
              (else t))))

    (define (power stream error)
      (cond ((equal? '- (peek stream))
             (list (next stream) (power stream error)))
            ((or (number? (peek stream)) (symbol? (peek stream)))
             (next stream))
            ((equal? "(" (peek stream))
             (next stream)
             (let ((t (expr stream error)))
               
               (if (and (equal? ")" (peek stream)) (next stream))
                   t
                   (error #f))))
            (else
             (error #f))))

    
    (call-with-current-continuation
     (lambda (error)
       (define result (expr stream error))
       (and (equal? (peek stream) EOF)
            result)))))

; Ассоциативность левая
;
(parse (tokenize "a / b / c / d"))
; (((a / b) / c) / d)

; Ассоциативность правая
;
(parse (tokenize "a^b^c^d"))
; (a ^ (b ^ (c ^ d)))

; Порядок вычислений задан скобками
;
(parse (tokenize "a/(b/c)"))
; (a / (b / c))

; Порядок вычислений определен только
; приоритетом операций
;

; ((a + (b / (c ^ 2))) - d)
;(parse (tokenize "(a + b/c)^2 - d"))

(define (tree->scheme xs)
  (if (and (pair? xs) (= (length xs) 3))
      (if (equal? (cadr xs) '^)
          (list 'expt (tree->scheme (car xs)) (tree->scheme (caddr xs)))
          (list (cadr xs) (tree->scheme (car xs)) (tree->scheme (caddr xs))))
      xs))

(tree->scheme (parse (tokenize "-a")))
 
(tree->scheme (parse (tokenize "a + - (b/c^2) - d")))
(tree->scheme (parse (tokenize "x^(a + 1)")))
; (expt x (+ a 1))

(eval (tree->scheme (parse (tokenize "2^2^2^2"))) (interaction-environment))
; 65536
