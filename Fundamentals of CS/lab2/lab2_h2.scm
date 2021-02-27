(define (my-element? x xs)
  (and (not (null? xs)) (or (equal? x (car xs)) (my-element? x (cdr xs)))))

(define (list->set xs)
  (define (loop xnews xs)
    (if (null? xs)
        xnews
        (if (my-element? (car xs) xnews)
            (loop xnews (cdr xs))
            (loop (cons (car xs) xnews) (cdr xs)))))
  (loop '() xs))

(list->set '(1 1 2 3)) ; (3 2 1)
(newline)

;===================================

(define (set? xs)
  (or (null? xs) (and (not (my-element? (car xs) (cdr xs)))(set? (cdr xs)))))

(set? '(1 2 3))                              ; #t
(set? '(1 2 3 3))                            ; #f
(set? '())                                   ; #t
(newline)

;===================================

(define (union xs ys)
  (if (null? xs)
      ys
      (if (my-element? (car xs) ys)
          (union (cdr xs) ys)
          (union (cdr xs) (cons (car xs) ys)))))

(union '(1 2 3) '(2 3 4))                    ; (4 3 2 1)
(newline)

;===================================

(define (intersection xs ys)
  (define (loop xs ys xnews)
    (if (null? xs)
        xnews
        (if (my-element? (car xs) ys)
            (loop (cdr xs) ys (cons (car xs) xnews))
            (loop (cdr xs) ys xnews))))
  (loop xs ys '()))
            
(intersection '(1 2 3) '(2 3 4))             ; (2 3)
(newline)

;===================================

(define (difference xs ys)
  (define (loop xs ys xnews)
    (if (null? xs)
        xnews
        (if (my-element? (car xs) ys)
            (loop (cdr xs) ys xnews)
            (loop (cdr xs) ys (cons (car xs) xnews)))))
  (loop xs ys '()))
            

(difference '(1 2 3 4 5) '(2 3))             ; (1 4 5)
(newline)

;===================================

(define (symmetric-difference xs ys)
  (append (difference xs ys) (difference ys xs)))

(symmetric-difference '(1 2 3 4) '(3 4 5 6)) ; (6 5 2 1)
(newline)

;===================================

(define (set-eq? xs ys)
  (and (null? (symmetric-difference xs ys)) #t))

(set-eq? '(1 2 3) '(3 2 1))                  ; #t
(set-eq? '(1 2) '(1 3))                      ; #f















    