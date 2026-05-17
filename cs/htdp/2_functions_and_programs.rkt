;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname 2_functions_and_programs) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp")) #f)))
(require 2htdp/image)

(define (f x) 1)
(define (d x y) (+ 1 1))
(define (h x y z) (+ (* 2 2) 3))
(define (ff a)
  (* a 10))

; exercise 11
(define (distance x y)
  (sqrt (+ (expt x 2) (expt y 2))))

; exercise 12
(define (cvolume a)
  (expt a 3))
(define (csurface a)
  (* 6 (expt a 2)))

; exercise 13
(define (string-first str)
  (string-ith str 0))

; exercise 14
(define (string-last str)
  (string-ith str (- (string-length str) 1)))

; exercise 15
(define (==> sunny friday)
  (or (not sunny) friday))

; exercise 16
(define (image-area img)
  (* (image-height img) (image-width img)))

; exercise 17
(define (image-classify img)
  (cond
    [(> (image-height img) (image-width img)) "tall"]
    [(< (image-height img) (image-width img)) "wide"]
    [(= (image-height img) (image-width img)) "square"]))


; exercise 18
(define (string-join str1 str2)
  (string-append str1 "_" str2))

; exercise 19
(define (string-insert str i)
  (string