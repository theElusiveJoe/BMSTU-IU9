;(load "trace and test.scm")

(define (interpret program stack)
  
  (define (skiptoelse i program enclosed)
    (cond
      ((and (= enclosed 0) (or (equal? (vector-ref program i) 'else) (equal? (vector-ref program i) 'endif))) ;нужный нам else
       (+ 1 i))
      ((equal? (vector-ref program i) 'if) ;вложенный if, который надо пропустить
       (skiptoelse (+ 1 i) program (+ enclosed 2)))
      ((and (or (equal? (vector-ref program i) 'else) (equal? (vector-ref program i) 'endif)) (not (= enclosed 0)));вложенный if закончился
       (skiptoelse (+ 1 i) program (- enclosed 1)))
      (else
       (skiptoelse (+ 1 i) program enclosed))))
  
  (define (skiptoendwhile i program enclosed)
    (cond
      ((and (= enclosed 0) (equal? (vector-ref program i) 'endwhile)) ;нужный нам endwhile
       (+ 1 i))
      ((equal? (vector-ref program i) 'while) ;вложенный while, который надо пропустить
       (skiptoendwhile (+ 1 i) program (+ enclosed 1)))
      ((and (equal? (vector-ref program i) 'endwhile) (not (= enclosed 0)));вложенный while закончился
       (skiptoendwhile (+ 1 i) program (- enclosed 1)))
      (else
       (skiptoendwhile (+ 1 i) program enclosed))))

  (define (forretstack i k retstack)
    (if (equal? k 1)
        retstack
        (forretstack i (- k 1) (cons 'for (cons i retstack)))))


  (define (ultimateskip i program a b c)
    (if (>= i (vector-length program))
        i
        (let ((x (vector-ref program i)))
          (cond
            ((or (equal? a -1) (equal? b -1) (equal? c -1)) i)
            ((eq? x 'while) (ultimateskip (+ 1 i) program (+ 1 a) b c))
            ((eq? x 'endwhile) (ultimateskip (+ 1 i) program (- a 1) b c))
            ((eq? x 'dowhile) (ultimateskip (+ 1 i) program a (+ 1 b) c))
            ((eq? x 'endodwhile) (ultimateskip (+ 1 i) program a (- b 1) c))
            ((eq? x 'for) (ultimateskip (+ 1 i) program a b (+ 1 c)))
            ((eq? x 'endfor) (ultimateskip (+ 1 i) program a b (- c 1)))
            (else (ultimateskip (+ 1 i) program a b c))))))

  (define (breakret retstack)
    (define (breakret2 retstack)
      (if (null? retstack)
          '()
          (if (equal? (car retstack) 'for)
              (breakret2 (cddr retstack))
              retstack)))
    (if (null? retstack)
        '()
        (if (equal? (car retstack) 'for)
            (breakret2 (cddr retstack))
            (cdr retstack))))

(define (skiptoendcase i program)
        (let ((x (vector-ref program i)))
          (if (equal? x 'endcase)
              (+ i 1)
              (skiptoendcase (+ i 1) program))))

  (define (skiptoendswitch i program)
        (let ((x (vector-ref program i)))
          (if (equal? x 'endswitch)
              (+ i 1)
              (skiptoendswitch (+ i 1) program))))
  
  (define (loop program i stack retstack dict)
    (if (>= i (vector-length program))
        stack
        (let ((x (vector-ref program i)))
          ;(display stack)
          ;(newline)
          (cond
            ((number? x) (loop program (+ 1 i) (cons x stack) retstack dict))
            ((equal? '+ x) (loop program (+ 1 i) (cons (+ (cadr stack) (car stack)) (cddr stack)) retstack dict))
            ((equal? '- x) (loop program (+ 1 i) (cons (- (cadr stack) (car stack)) (cddr stack)) retstack dict))
            ((equal? '* x) (loop program (+ 1 i) (cons (* (cadr stack) (car stack)) (cddr stack)) retstack dict))
            ((equal? '/ x) (loop program (+ 1 i) (cons (quotient (cadr stack) (car stack)) (cddr stack)) retstack dict))
            ((equal? 'mod x) (loop program (+ 1 i) (cons (remainder (cadr stack) (car stack)) (cddr stack)) retstack dict))
            ((equal? 'neg x) (loop program (+ 1 i) (cons (-(car stack)) (cdr stack)) retstack dict))
            ((equal? '= x) (loop program (+ 1 i) (cons (if (= (cadr stack) (car stack)) -1 0) (cddr stack)) retstack dict))
            ((equal? '> x) (loop program (+ 1 i) (cons (if (> (cadr stack) (car stack)) -1 0) (cddr stack)) retstack dict))
            ((equal? '< x) (loop program (+ 1 i) (cons (if (< (cadr stack) (car stack)) -1 0) (cddr stack)) retstack dict))
            ((equal? 'not x) (loop program (+ 1 i) (cons (if (zero? (car stack)) -1 0) (cdr stack)) retstack dict))
            ((equal? 'and x) (loop program (+ 1 i) (cons (if (or (zero? (cadr stack)) (zero? (car stack))) 0 -1) (cddr stack)) retstack dict))
            ((equal? 'or x) (loop program (+ 1 i) (cons (if (and (zero? (cadr stack)) (zero? (car stack))) 0 -1) (cddr stack)) retstack dict))
            ((equal? 'drop x) (loop program (+ 1 i) (cdr stack) retstack dict))
            ((equal? 'swap x) (loop program (+ 1 i) (append (list (cadr stack) (car stack)) (cddr stack)) retstack dict))
            ((equal? 'dup x) (loop program (+ 1 i) (cons (car stack) stack) retstack dict))
            ((equal? 'over x) (loop program (+ 1 i) (cons (cadr stack) stack) retstack dict))
            ((equal? 'rot x) (loop program (+ 1 i) (append (list (caddr stack) (cadr stack) (car stack)) (cdddr stack)) retstack dict))
            ((equal? 'depth x) (loop program (+ 1 i) (cons (length stack) stack) retstack dict))
            ((equal? 'if x) (if (not (zero? (car stack)))
                                (loop program (+ 1 i) (cdr stack) retstack dict) ; скипнем потом, когда встретим else
                                (loop program (skiptoelse (+ 1 i) program 0) (cdr stack) retstack dict))) ; скипаем до else
            ((equal? 'else x) (loop program (skiptoelse (+ 1 i) program 0) stack retstack dict)) ;скипаем до endif
            ((equal? 'endif x) (loop program (+ i 1) stack retstack dict))
            ((equal? 'define x) (loop program (skiptoend (+ i 1) program) stack retstack (cons (list (vector-ref program (+ 1 i)) (+ i 2)) dict)))
            ((equal? 'end x) (loop program (car retstack) stack (cdr retstack) dict))
            ((equal? 'exit x) (loop program (car retstack) stack (cdr retstack) dict)) 
            ((assoc x dict) (loop program (cadr (assoc x dict)) stack (cons (+ 1 i) retstack) dict))
            
            ;цикл с предусловием
            ((equal? 'while x) (if (not (zero? (car stack)))
                                   (loop program (+ i 1) (cdr stack) (cons i retstack) dict)
                                   (loop program (skiptoendwhile (+ i 1) program 0) (cdr stack) retstack dict)))
            ((equal? 'endwhile x) (loop program (car retstack) stack (cdr retstack) dict))
            ;цикл с постусловием
            ((equal? 'dowhile x) (loop program (+ i 1) stack (cons i retstack) dict))
            ((equal? 'enddowhile x) (if (not (zero? (car stack)))
                                        (loop program (car retstack) (cdr stack) (cdr retstack) dict)
                                        (loop program (+ i 1) (cdr stack) (cdr retstack) dict)))
            ;цикл с параметром
            ((equal? 'for x) (loop program (+ i 1) (cdr stack) (append (forretstack (+ i 1) (car stack) '()) retstack) dict))
            ((equal? 'endfor x) (if (and (not (null? retstack)) (eq? 'for (car retstack)))
                                    (loop program (car (cdr retstack)) stack (cddr retstack) dict)
                                    (loop program (+ i 1) stack retstack dict)))

            ;управление циклом (вложенные for не поддерживаются из-за особенности записи в retstack)
            ((equal? 'break x) (loop program (ultimateskip i program 0 0 0) stack (breakret retstack) dict))     
            ((equal? 'continue x) (if (null? retstack)
                                      (loop program (ultimateskip i program 0 0 0) stack '() dict)
                                      (if (eq? 'for (car retstack))
                                          (loop program (car (cdr retstack)) stack (cddr retstack) dict)
                                          (loop program (car retstack) stack (cdr retstack) dict))))

            ;switch-case
            ;считаем, что в конце каждого case по умолчанию стоит break (который в c++, например, надо ставить самому)
            ((equal? 'switch x) (loop program (+ 1 i) stack retstack dict))
            ((equal? 'case x) (if (equal? (car stack) (cadr stack)) ;на этот момент на стеке должно быть минимум 2 числа 
                                  (loop program (+ 1 i) (cddr stack) retstack dict)
                                  (loop program (skiptoendcase i program) (cdr stack) retstack dict)))
            ((equal? 'endcase x) (loop program (skiptoendswitch i program) stack retstack dict))
            ))))

  (loop program 0 stack '() '()))

;всего сдесь 5 пунктов из домашнего задания №5
;я уже сдал Вам 1 или 2 пункта, но в этом файле все вместе

(interpret  #(1
              if
              1 if 1 else 2 endif 
              else
              0 if 3 else 4 endif
              endif )  '())
(interpret  #(1
              if
              0 if 1 else 2 endif 
              else
              0 if 3 else 4 endif
              endif )  '())
(interpret  #(0
              if
              1 if 1 else 2 endif 
              else
              1 if 3 else 4 endif
              endif )  '())
(interpret  #(0
              if
              1 if 1 else 2 endif 
              else
              0 if 3 else 4 endif
              endif )  '())

;************************
(trace (interpret #(3 switch 1 case 111 endcase 2 case 222 endcase 3 case 333 endcase endswitch) '()))


(trace (interpret  #(1 while dup 1 - dup endwhile)  '(10)))
(trace (interpret  #(dowhile dup 1 - dup enddowhile)  '(10)))
(trace (interpret #(5 for dup 1 - endfor) '(10))) ; добавляет в стек именно 5 раз 

(trace (interpret #(1 while dup 1 - dup 3 < if drop break endif dup 1 - endwhile) '(10))) ;
(trace (interpret #(dowhile dup 1 - dup 5 < if drop break endif dup 1 - enddowhile) '(10))) ;
(trace (interpret #(10 for dup dup 7 < if drop drop break endif 1 - endfor) '(10))) ;

(trace (interpret #(10 for dup dup 7 < if 1 - drop continue endif 1 - endfor) '(10))) ;
(trace (interpret  #(1 while dup 1 - dup  continue 100500 endwhile)  '(10)))
(trace (interpret #(dowhile dup 1 -  dup -5 = if break endif continue 100500 enddowhile) '(10))) ;

