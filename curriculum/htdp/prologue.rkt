;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname prologue) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "htdp")) #f)))
(require 2htdp/universe)

; constants
(define WIDTH 200)
(define HEIGHT 200)
(define MTSCN (empty-scene WIDTH HEIGHT))
(define GROUND-VENUS (rectangle WIDTH 10 "solid" "gray"))
(define GROUND-EARTH (rectangle WIDTH 10 "solid" "green"))
(define EARTH (place-image GROUND-EARTH
                           (/ WIDTH 2) HEIGHT
                           (place-image (rectangle WIDTH HEIGHT "solid" "lightblue") (/ WIDTH 2) (/ HEIGHT 2) MTSCN)))
(define VENUS (place-image GROUND-VENUS
                           (/ WIDTH 2) HEIGHT
                           (place-image (rectangle WIDTH HEIGHT "solid" "orange") (/ WIDTH 2) (/ HEIGHT 2) MTSCN)))
(define UFO (overlay (circle 10 "solid" "green")
                     (rectangle 40 4 "solid" "green")))
(define UFO-CENTER-TO-TOP
  (- HEIGHT (/ (image-height UFO) 2)))
  
; functions
(define (venus h)
  (cond
    [(<= h (- UFO-CENTER-TO-TOP 10))
     (place-image UFO (/ WIDTH 2) h VENUS)]
    [(>= h (- UFO-CENTER-TO-TOP 10))
     (place-image UFO (/ WIDTH 2) (- UFO-CENTER-TO-TOP 5) VENUS)]))

(define (earth h)
  (cond
    [(<= h (- UFO-CENTER-TO-TOP 10))
     (place-image UFO (/ WIDTH 2) h EARTH)]
    [(>= h (- UFO-CENTER-TO-TOP 10))
     (place-image UFO (/ WIDTH 2) (- UFO-CENTER-TO-TOP 5) EARTH)]))
          

(animate venus)