(load "stream.scm")
(load "trace.scm")

;<fractions> ::= whitespace<fractions> | <fraction><fractions> | <sign><fraction><fractions> | <empty>
;<fraction> ::= <num><nums>/<num><nums>
;<sign> ::= + | - | <empty>
;<nums> ::= <num><nums> | <empty>
;<num> ::= 1|2|3|4|5|6|7|8|9|0

(define (scan-many-fracs str)
  (let* ((EOF (integer->char 0))
         (stream (make-stream (string->list str) EOF)))
     
    (define (fractions stream error)
      (cond ((char-whitespace? (peek stream))
             (next stream)
             (fractions stream error))
            ((equal? EOF (peek stream))
             '())
            ((member (peek stream) (list #\+ #\-))
             (cons (string->number (string-append (list->string (list (next stream))) (fraction stream error)))
                   (fractions stream error)))
            ((char-numeric? (peek stream))
             (cons (string->number (fraction stream error))
                   (fractions stream error)))
            (else
             (error #f))))

    (define (fraction stream error)
      (string-append (list->string (cons (next stream)
            (nums stream error)))
            (if (equal? (peek stream) #\/)
                (begin
                  (next stream)
                  "/")
                (error #f))
            (list->string (cons (if (char-numeric? (peek stream))
                (next stream)
                (error #f))
            (nums stream error)))))

  (define (nums stream error)
    (cond ((char-numeric? (peek stream))
           (cons (next stream) (nums stream error)))
          (else '())))
         
  (call-with-current-continuation
   (lambda (error)
     (define result (fractions stream error))
     (and
      (equal? (peek stream) EOF)
      result)))))
 
(scan-many-fracs
 "\t11/22 -1/3\n\n+10/8")  ; (1/2 1/3 5/4)
(scan-many-fracs
 "\t1/2 1/3\n\n2/-5")  ; #f

(scan-many-fracs "+5/10")   
(scan-many-fracs "5.0/10")  ; #f
(scan-many-fracs "/")   ; #f
(scan-many-fracs "/1"); #f
(scan-many-fracs "-"); #f