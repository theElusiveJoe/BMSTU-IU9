(define p #f)

(define (use-assertions)
   (call-with-current-continuation
          (lambda (exit)
            (set! p (lambda (x)
                      (display "FAILED: ")
                      (display x)
                      (exit))))))

(define-syntax assert
  (syntax-rules ()
    ((_ expr) (if (not expr)
                  (p 'expr)))))


(use-assertions) ; Инициализация вашего каркаса перед использованием

; Определение процедуры, требующей верификации переданного ей значения:

(define (1/x x)
  (assert (not (zero? x))) ; Утверждение: x ДОЛЖЕН БЫТЬ > 0
  (/ 1 x))

; Применение процедуры с утверждением:

(map 1/x '(1 2 3 4 5)) ; ВЕРНЕТ список значений в программу

(map 1/x '(-2 -1 0 1 2)) ; ВЫВЕДЕТ в консоль сообщение и завершит работу программы