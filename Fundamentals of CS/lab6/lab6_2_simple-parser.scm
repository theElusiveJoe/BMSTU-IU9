; <Program>  ::= <Articles> <Body> .
; <Articles> ::= <Article> <Articles> | .
; <Article>  ::= define word <Body> end .
; <Body>     ::= if <Body> endif <Body> | integer <Body> | word <Body> | .

(load "stream.scm")
(load "trace.scm")


(define (parse xv)
  (let* ((EOF (integer->char 0))
         (stream (make-stream (vector->list xv) EOF)))

    (define (program stream error)
      (cond ((equal? EOF (peek stream))
             (error #f))
            (else
             (list(articles stream error) (body stream error)))))

    (define (articles stream error)
      (cond ((equal? (peek stream) 'define)
             (next stream)  ;съели define  
             (cons (article stream error) (articles stream error)))
            (else
             '())))
             
    (define (article stream error)
      (cond ((word? (peek stream))
             (cons (next stream) ; cъели word
                   (cons (body stream error) ; съели body
                         (if (equal? 'end (peek stream))
                             (begin
                               (next stream) ; съели end
                               '())
                             (error #f)))))
            (else
             (error #f))))

    (define (body stream error)
      (cond ((equal? 'if (peek stream))
             (next stream)
             (cons (cons 'if
                         (cons (body stream error)
                               (if (and (equal? 'endif (peek stream)) (next stream))
                                   '()
                                   (error #f))))
                   (body stream error)))
            ((number? (peek stream))
             (cons (next stream) (body stream error)))
            ((word? (peek stream))
             (cons (next stream) (body stream error)))
            (else
             '())))
            
    (define (word? x)
      (and (not (member x '(define end if endif))) (symbol? x)))

    (call-with-current-continuation
     (lambda (error)
       (define result (program stream error))
       (and (equal? (peek stream) EOF)
            result)))))
    
        

  


  
(parse #(1 2 +)) ; (() (1 2 +))
(newline)
(parse #(x dup 0 swap if drop -1 endif))
; (() (x dup 0 swap (if (drop -1))))
(newline)
(parse #( define -- 1 - end
           define =0? dup 0 = end
           define =1? dup 1 = end
           define factorial
           =0? if drop 1 exit endif
           =1? if drop 1 exit endif
           dup --
           factorial
           *
           end
           0 factorial
           1 factorial
           2 factorial
           3 factorial
           4 factorial ))

(parse #(define word w1 w2 w3)) ; #f
(parse #(define if end endif))
(parse #(if define end endif))
(parse #(define x if end endif))
(parse #(define if endif end))
(parse #(define 1 end))
(parse #(if define x end endif))
(parse #(define x endif end))
(parse #(endif if))
(parse #(define endif x y z end))
(parse #(if if if if endif endif endif endif))


(newline)
(parse #(define abs 
          dup 0 < 
          if neg endif 
          end 
          9 abs 
          -9 abs))
(newline)
(parse #(define =0? dup 0 = end
          define <0? dup 0 < end
          define signum
          =0? if exit endif
          <0? if drop -1 exit endif
          drop
          1
          end
          0 signum
          -5 signum
          10 signum))
















