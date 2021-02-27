;<tokens> ::= <sign><fraction> | <fraction>
;<fraction> ::= <num><endoffraction>
;<endoffraction> ::= <num><endoffraction> | /<denominator>
;<denominator> ::= <num><endofdenominator>
;<endofdenominator> ::= <num><endofdenominator> | eof
;<num> ::= 1|2|3|4|5|6|7|8|9|0

(load "stream.scm")
(load "trace.scm")

(define (check-frac str)
  (let* ((EOF (integer->char 0))
         (stream (make-stream (string->list str) EOF)))             
    

    (define (tokens stream error)
      (cond ((or (equal? (peek stream) #\+) (equal? (peek stream) #\-))
             (next stream)
             (fraction stream error))
            (else (fraction stream error))))
    (define (fraction stream error)
      (cond ((char-numeric? (peek stream))
             (endoffraction stream error))
            (else
             (error #f))))
    (define (endoffraction stream error)
      (cond ((char-numeric? (peek stream))
             (next stream)
             (endoffraction stream error))
            ((equal? (peek stream) #\/) 
             (next stream)
             (denominator stream error))
            (else error)))
    (define (denominator stream error)
      (cond ((char-numeric? (peek stream))
             (next stream)
             (endofdenominator stream error))
            (else
             (error #f))))
    (define (endofdenominator stream error)
      (cond ((char-numeric? (peek stream))
             (next stream)
             (endofdenominator stream error))
            ((equal? EOF (peek stream))
             #t)
            (else
             (error #f))))
    (call-with-current-continuation
     (lambda (error)
       (define result (tokens stream error))
       (and (equal? (peek stream) EOF)
            result)))))    


(check-frac "110/111") ; #t
(check-frac "-4/3")    ; #t
(check-frac "+5/10")   ; #t
(check-frac "5.0/10")  ; #f
(check-frac "/")   ; #f
(check-frac "/1"); #f
(check-frac "-"); #f

(newline)


;***********************************
(define (scan-frac str)
  (and (check-frac str) (string->number str)))

(scan-frac "110/111")  ; 110/111
(scan-frac "-4/3")     ; -4/3
(scan-frac "+5/10")    ; 1/2
(scan-frac "5.0/10")   ; #f
(scan-frac "FF/10")    ; #f
(newline)












    

