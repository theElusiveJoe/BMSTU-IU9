(define-syntax when
  (syntax-rules ()
    ((_ cond? x . xs)
     (if cond?
         (begin x . xs)))))

(define-syntax unless
  (syntax-rules ()
    ((_ cond? x . xs)
     (if (not cond?)
         (begin x . xs)))))

(define-syntax for
  (syntax-rules (as in)
    ((_ x in xs . ys) (for-each (lambda (x) (begin . ys)) xs))
    ((_ xs as x . ys) (for-each (lambda (x) (begin . ys)) xs))))

(define-syntax while
  (syntax-rules ()
    ((_ cond? . xs)
     (let end () (when cond? (begin . xs) (end))))))

(define-syntax repeat
  (syntax-rules (until)
    ((_ (exp . expr) until cond?)
     (let end ()
       (begin exp . expr)
       (if (not cond?) (end))))))

(define-syntax cout
  (syntax-rules (<< endl)
    ((_ << endl) (newline))
    ((_ << x) (display x))
    ((_ << endl . xs) (begin (newline) (cout . xs)))
    ((_ << x . xs) (begin (display x) (cout . xs)))))

(define x 1)
(when   (> x 0) (display "x > 0")  (newline))
(unless (= x 0) (display "x != 0") (newline))

(for i in '(1 2 3)
  (for j in '(4 5 6)
    (display (list i j))
    (newline)))

(for '(1 2 3) as i
  (for '(4 5 6) as j
    (display (list i j))
    (newline)))

(let ((p 0)
      (q 0))
  (while (< p 3)
         (set! q 0)
         (while (< q 3)
                (display (list p q))
                (newline)
                (set! q (+ q 1)))
         (set! p (+ p 1))))


(let ((i 0)
      (j 0))
  (repeat ((set! j 0)
           (repeat ((display (list i j))
                    (set! j (+ j 1)))
                   until (= j 3))
           (set! i (+ i 1))
           (newline))
          until (= i 3)))

(cout << "a = " << 1 << endl << "b = " << 2 << endl)
  
  