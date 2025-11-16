#lang sicp

(define (square x) (* x x))

(define (sum-of-squares x y)
  (+ (square x) (square y)))

; conditionals

(define (abs x)
  (cond ((> x 0) x)
        ((= x 0) 0)
        ((< x 0) (- x))))

(define (abs2 x)
  (cond ((< x 0) (- x))
        (else x)))

(define (abs3 x)
  (if (< x 0)
      (- x)
      x))

; cond expressions may be a sequence of expressions
; each exp is evaluated in sequence and the final is returned
; if requires only two cases in case analysis

; exercises

(define a 3)
(define b (+ a 1))
(* (cond ((> a b) a)
         ((< a b) b)
         (else -1))
   (+ a 1))

; translation (5+4+(2-(3-(6+(4/5)))))/(3*(6-2)*(2-7))
(/ (+ 5 4
      (- 2
         (- 3
            (+ 6
               (/ 4 5)))))
   (* 3
      (- 6 2)
      (- 2 7)))


; takes 3 num args, returns sum of squares of two larger numbers

(define (max2-sum-of-squares x y z)
  (define n1 (cond ((>= x (and y z)) x)
                   ((>= y (and x z)) y)
                   ((>= z (and x y)) z)))
  (define n2 (cond ((and (>= x y) (>= y z)) y)
                   ((and (>= x z) (>= z y)) z)
                   ((and (>= y x) (>= x z)) x)
                   ((and (>= y z) (>= z x)) z)
                   ((and (>= z x) (>= x y)) x)
                   ((and (>= z y) (>= y x)) y)))
  (display n1)
  (newline)
  (display n2)
  (newline)
  (display "Sum of squares: ")
  (+ (* n1 n1) (* n2 n2)))


(max2-sum-of-squares 1 2 3)



