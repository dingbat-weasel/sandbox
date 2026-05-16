#lang htdp/bsl
(require 2htdp/image)
(require 2htdp/universe)




; properties of world and ufo
(define WIDTH 200)
(define HEIGHT 200)
(define V 4)
(define X_POS (/ WIDTH 2))

; graphical constants
(define MTSCN (empty-scene WIDTH HEIGHT))
(define ELEVATION 10)
(define GROUND-VENUS (rectangle WIDTH ELEVATION "solid" "gray"))
(define GROUND-EARTH (rectangle WIDTH ELEVATION "solid" "green"))
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
(define (venus t)
  (cond
    [(<= (distance t) (- UFO-CENTER-TO-TOP ELEVATION))
     (place-image UFO X_POS (distance t) VENUS)]
    [(>= (distance t) (- UFO-CENTER-TO-TOP ELEVATION))
     (place-image UFO X_POS (- UFO-CENTER-TO-TOP (/ ELEVATION 2)) VENUS)]))

(define (earth t)
  (cond
    [(<= (distance t) (- UFO-CENTER-TO-TOP ELEVATION))
     (place-image UFO X_POS (distance t) EARTH)]
    [(>= (distance t) (- UFO-CENTER-TO-TOP ELEVATION))
     (place-image UFO X_POS (- UFO-CENTER-TO-TOP 5) EARTH)]))
          
(define (distance t)
  (* V t))

(animate venus)