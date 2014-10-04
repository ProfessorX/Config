(module random mzscheme
  ; SRFI 27
  (provide random-integer     
           random-real
           default-random-source)
  
  ; SRFI 27 like
  (provide random-source-make-normals       random-normal
           random-source-make-gaussians     random-gaussian
           random-source-make-exponentials  random-exponential
           random-source-make-gammas        random-gamma
           random-source-make-betas         random-beta
           random-source-make-chi-squares   random-chi-square    
           random-source-make-Fs            random-F
           random-source-make-ts            random-t

           random-source-make-geometrics    random-geometric
           random-source-make-binomials     random-binomial 
           random-source-make-poissons      random-poisson
           
           random-source-make-permutations  random-permutation  
           random-source-make-discretes)
  
  (require (lib "list.ss" "mzlib")
           (lib "math.ss" "mzlib"))
  
  
  (require (lib "27.ss" "srfi"))
  ; (require (lib "27-scheme.ss" "srfi"))   ; for now (use above)
  (require (lib "42.ss" "srfi"))

  ; From srfi-27
  
  ; random-integer : integer -> {0, ..., n-1}
  ;  (random-integer n) gives the next integer x in {0, ..., n-1} obtained from 
  ;  default-random-source. Subsequent results of this procedure appear to be 
  ;  independent uniformly distributed over the range {0, ..., n-1}. The argument n 
  ;  must be a positive integer, otherwise an error is signalled. 
  
  ; random-real : -> ]0;1[
  ;   Gives the next number 0 < x < 1 obtained from default-random-source. 
  ;   Subsequent results of this procedure appear to be independent uniformly distributed. 
  ;   The numerical type of the results and the quantization of the output range depend on 
  ;   the implementation; refer to random-source-make-reals for details. 
  
  ; default-random-source 
  ;   A random source from which random-integer and random-real have been derived using 
  ;   random-source-make-integers and random-source-make-reals. Note that an assignment to 
  ;   default-random-source does not change random or random-real; it is also strongly recommended 
  ;   not to assign a new value. 
  
  ;;; NORMAL DISTRIBUTION
  
  ; random-source-make-normals : source [unit] -> real
  ;   The call (random-source-make-normals s . unit) returns
  ;   a function (lambda (mu sigma) ...) that generates
  ;   normal N(mu, sigma)-distributed real numbers using the polar method.
  ;  [Code by: Sebastian Egner]

  ;                            1     /x         2
  ; Distribution:  F(x) = ---------  |    exp(-t / 2) dt   , mu=0, sigma=1
  ;                       sqrt(2pi)  /-infinity
  
  (define (random-source-make-normals s . unit)
    (let ((rand (if (empty? unit)
                    (random-source-make-reals s)
                    (random-source-make-reals s (first unit))))
          (next #f))
      (lambda (mu sigma)
        (if next
            (let ((result next))
              (set! next #f)
              (+ mu (* sigma result)))
            (let loop ()
              (let* ((v1 (- (* 2.0 (rand)) 1.0))
                     (v2 (- (* 2.0 (rand)) 1.0))
                     (s (+ (* v1 v1) (* v2 v2))))
                (if (>= s 1)
                    (loop)
                    (let ((scale (sqrt (/ (* -2.0 (log s)) s))))
                      (set! next (* scale v2))
                      (+ mu (* sigma scale v1))))))))))
  
  ; random-normal : mu sigma -> real
  ;   generates N(mu,sigma)-distributed numbers
  (define random-normal
    (random-source-make-normals default-random-source))
  
  ; random-source-make-gaussians :  -> real
  (define (random-source-make-gaussians s . unit)
    (let ([N (if (empty? unit)
                 (random-source-make-normals s)
                 (random-source-make-normals s unit))])
      (lambda ()
        (N 0.0 1.0))))
  
  ; random-gaussian :  -> real
  ;   generates N(0,1)-distributed numbers
  (define random-gaussian
    (random-source-make-gaussians default-random-source))
  
  
  ;;; EXPONENTIAL DISTRIBUTION
  
  ; The following code defines procedures to generate exponentially 
  ; Exp(mu)-distributed random numbers.
  ; Ref: Knuth's "The Art of Computer Programming", Vol. II, 2nd ed., Section 3.4.1.D. 

  ; Distribution:  F(x) = 1 - exp(-x/mu)   , mu is the mean
  
  (define (random-source-make-exponentials s . unit)
    (let ((U (apply random-source-make-reals s unit)))
      (lambda (mu)
        (- (* mu (log (U)))))))
  
  (define random-exponential
    (random-source-make-exponentials default-random-source))

  ;;; GAMMA DISTRIBUTION
  
  ; Distribution: The gamma distribition of order a>0
  
  ;               1       /x    a-1  -t
  ;     F(x) = ---------  |    t    e   dt,  x>=0
  ;            gamma(a)   /0

  ; Ref:  Knuth, Vol. II, 2nd ed., 
  ;       Section 3.4.1.E  and solution to exercise 3.4.1.16
  ; Note: Non-implemented improvements can be found in
  ;       "Numerical Recipes in C", section 7.3
  ;       <http://www.phys.uni.torun.pl/nrbook/c7-3.pdf>
  
  ; random-source-make-gammas : source [unit] -> ([1;inf[ -> real)
  ;  make function generating gamma(a) deviates given a in [1;inf[
  (define (random-source-make-gammas s . unit)
    (let* ([U (apply random-source-make-reals s unit)]
           [V U]
           ;[E (apply random-source-make-exponentials s unit)]
           )
      (lambda (a)
        (cond
          [(<= a 1.0)  (let ; G1 [Initialize] 
                           ([p (/ e (+ a e))])
                         ; G2 [Generate G deviate]
                         (let loop ()
                           (let-values ([(X q) (if (< (U) p)
                                                   (let ([X (expt (V) (/ 1.0 a))])
                                                     (values  X
                                                              (exp (- X))))
                                                   (let ([X (- 1.0 (log (V)))])
                                                     (values X 
                                                             (expt X (- a 1.0)))))])
                             ; G3 [Reject?]]
                             (if (>= (U) q)
                                 (loop)
                                 X))))]
          [(> a 1.0)   (let loop ()  ; A1 [Generate candidate]
                         (let* ([Y (tan (* pi (U)))]
                                [X (+ (* (sqrt (- (* 2.0 a) 1.0)) Y) a -1.0)])
                           ; A2 [Accept?]
                           (if (<= X 0.0)
                               (loop)
                               (if (> (V) (* (+ 1.0 (* Y Y)) 
                                             (real-part (exp (- (* (- a 1.0) 
                                                                   (log (/ X (- a 1.0))))
                                                                (* (sqrt (- (* 2.0 a) 1.0)) 
                                                                   Y))))))
                                   (loop)
                                   X))))]))))

  (define random-gamma
    (random-source-make-gammas default-random-source))

  ;;; BETA DISTRIBUTION
  
  ; Distribution:  Beta distribution with a>0 and b>0
  
  ;              gamma(a+b)     / x   a-1      b-1
  ;  F(x) =  -----------------  |    t    (1-t)     dt    , 0<= x <= 1
  ;          gamma(a) gamma(b)  / 0
  
  (define (random-source-make-betas s . unit)
    (let ([G (apply random-source-make-gammas s unit)])
      (lambda (a b)
        (let ([X1 (G a)]
              [X2 (G b)])
          (/ X1 (+ X1 X2))))))
  
  (define random-beta
    (random-source-make-betas default-random-source))

  ;;; CHI-SQUARE
  
  (define (random-source-make-chi-squares s . unit)
    (let ([G (apply random-source-make-gammas s unit)])
      (lambda (ny)
        (* 2.0 (G (/ ny 2.0))))))

  (define random-chi-square
    (random-source-make-chi-squares default-random-source))
  
  
  ;;; F-DISTRIBUTION
  
  ; The F-distribution (variance-ratio distribution) with
  ; ny1 and ny2 degrees of freedom:

  ;             ny1/2    ny2/2
  ;          ny1      ny2     gamma((ny1+ny2)/2)  / x   ny1/2-1           -ny1/2-ny2/2b-1
  ;  F(x) =  -----------------------------------  |    t        (ny2+ny1t)                dt    
  ;          gamma(ny1/2) gamma(ny2/2)            /0
  
  ; where x>=0.
                 
  (define (random-source-make-Fs s . unit)
    (let ([C (apply random-source-make-chi-squares s unit)])
      (lambda (ny1 ny2)
        (let ([Y1 (C ny1)]
              [Y2 (C ny2)])
          (/ (* Y1 ny2)
             (* Y2 ny1))))))

  (define random-F
    (random-source-make-Fs default-random-source))
  
  ;;; t-DISTRIBUTION

  ; The t-distribution with ny degrees of freedom
  
  ;          
  ;          gamma((ny+1)/2)           / x         2     -(ny+1)/2
  ;  F(x) =  -----------------------   |     (1 + t / ny)          dt    
  ;          sqrt(pi ny) gamma(ny/2)   /-inf
  
  (define (random-source-make-ts s . unit)
    (let ([N (apply random-source-make-normals s unit)]
          [C (apply random-source-make-chi-squares s unit)])
      (lambda (ny)
        (let ([Y1 (N 0.0 1.0)]
              [Y2 (C ny)])
          (/ Y1
             (sqrt (/ Y2 ny)))))))
  
  (define random-t
    (random-source-make-ts default-random-source))


  ;;; GEOMETRIC DISTRIBUTION

  ; A discrete distribution of one parameter p. 
  ; The probability function is
  
  ;                      n-1  
  ;      P(n) =   p (1-p)      ; where 0<p<1
  
  ; Mean:      my      =  1/p
  ; Variance:  sigma^2 =  (1-p)/p^2

  (define (random-source-make-geometrics s . unit)
    (let ([U (apply random-source-make-reals s unit)])
      (lambda (p)
        (ceiling (real-part (/ (log (U))
                               (log (- 1 p))))))))
  
  (define random-geometric
    (random-source-make-geometrics default-random-source))

  ;;; BINOMIAL DISTRIBUTION
  
  (define (random-source-make-binomials s)
    (let ([U    (random-source-make-reals s)]
          [Beta (random-source-make-betas s)])
      (letrec ([binom (lambda (t p)
                        (cond
                          ; small t
                          [(<= t 10)  (let loop ([N 0]
                                                [i 0])
                                        (cond
                                          [(= i t)   N]
                                          [(< (U) p) (loop (add1 N) (add1 i))]
                                          [else      (loop N (add1 i))]))]
                          ; large t
                          [else        (let* ([a (+ 1.0 (floor (/ t 2.0)))]
                                              [b (+ t 1.0 (- a))]
                                              [X (Beta a b)])
                                         (if (>= X p)
                                             (binom (- a 1) (/ p X))
                                             (+ a (binom (- b 1) (/ (- p X) (- 1 X))))))]))])
        binom)))
  
  (define random-binomial
    (random-source-make-binomials default-random-source))

  
  ;;; POISSON DISTRIBUTION
  
  ; The Poisson distribution with mean my.
  
  (define (random-source-make-poissons s)
    (let ([U    (random-source-make-reals s)]
          [G    (random-source-make-gammas s)]
          [B    (random-source-make-binomials s)])
      (letrec ([poisson (lambda (my)
                          (let ([treshold (exp (- my))]
                                [m (ceiling (* 7/8 my))])
                            (cond
                              ; small my
                              [(<= my 10) (let loop ([prod 1.0]
                                                     [m 0])
                                            (cond
                                              [(<= prod treshold)  (- m 1)]
                                              [else                (let ([X (U)])
                                                                     (loop (* prod X) (add1 m)))]))]
                              ; large my
                              [else        (let ([X (G m)])
                                             (if (< X my)
                                                 (+ m (poisson (- my X)))
                                                 (B (- m 1) (/ my X))))])))])
        poisson)))

    (define random-poisson
      (random-source-make-poissons default-random-source))

  
  ;;; PERMUTATIONS
  
  ; random-source-make-permutations : source -> (integer - > vector)
  ;  produces a function that given an integer n generates permutations
  ;  of the numbers 0,...,n-1  i.e. a vector of length n is returned
  ;  containing the numbers 0 to n-1 in some order.

  ; Ref: Knuth, "The Art of Computer Programming", Vol. II, 2nd ed., Algorithm P of Section 3.4.2. 
  ;      SRFI-27
  
  ; Code:  Sebastion Egner 

  (define (random-source-make-permutations s)
    (let ((rand (random-source-make-integers s)))
      (lambda (n)
        (let ((x (make-vector n 0)))
          (do ((i 0 (+ i 1)))
	    ((= i n))
            (vector-set! x i i))
          (do ((k n (- k 1)))
	    ((= k 1) x)
            (let* ((i (- k 1))
                   (j (rand k))
                   (xi (vector-ref x i))
                   (xj (vector-ref x j)))
              (vector-set! x i xj)
              (vector-set! x j xi)))))))
  
  (define random-permutation
    (random-source-make-permutations default-random-source))
  
  
  ; Random Source for Discrete Distribution 
  ; ======================================= 
  
  ; Sebastian.Egner@philips.com, 2-May-2003 
  ; in R5RS-Scheme using 
  ;   SRFI-23 (error), 
  ;   SRFI-27 (random sources), 
  ;   SRFI-42 (eager comprehensions) 
  
  ; (random-source-make-discretes s w) 
  ;    given a source s of random bits in the sense of SRFI-27 
  ;    and a vector w of n >= 1 non-negative real numbers, 
  ;    this procedure constructs and returns a procedure rand 
  ;    such that (rand) returns the next integer x in {0..n-1} 
  ;    from a pseudo random sequence with 
  ; 
  ;      Pr{x = k} = w[k] / Sum(w[i] : i) 
  ; 
  ;    for all k in {0..n-1}. 
  
  (define (random-source-make-discretes s w) 
    
    (define (check-weights w) 
      (if (not (and (vector? w) 
                    (>= (vector-length w) 1) 
                    (every?-ec (:vector wi w) 
                               (and (number? wi) (not (negative? wi)))))) 
          (error "bad vector of weights" w))) 
    
    (define (make-cutoff-alias w) 
      
      (define eps (expt 10 -6)) 
      
      (define n (vector-length w)) 
      (define cutoff (make-vector n 1)) 
      (define alias (make-vector n 0)) 
      
      (define avg-w (/ (sum-ec (:vector wi w) wi) n)) 
      (define b (vector-of-length-ec n (:vector wi w) (- wi avg-w))) 
      
      (let loop ((sum-abs-b (sum-ec (:vector bi b) (abs bi)))) 
        (if (< sum-abs-b eps) 
            (list cutoff alias) 
            (let ((imin 0) (bmin (vector-ref b 0)) 
                  (imax 0) (bmax (vector-ref b 0))) 
              (do-ec (:vector bi (index i) b) 
                     (begin 
                       (if (< bi bmin) 
                           (begin (set! imin i) (set! bmin bi))) 
                       (if (> bi bmax) 
                           (begin (set! imax i) (set! bmax bi))))) 
              (vector-set! cutoff imin (+ 1 (/ bmin avg-w))) 
              (vector-set! alias  imin imax) 
              (vector-set! b imin 0) 
              (vector-set! b imax (+ bmin bmax)) 
              (loop (+ sum-abs-b (- (abs bmin)) (- (abs bmax)) 
                       (+ (abs (vector-ref b imax))))))))) 
    
    (check-weights w) 
    
    (let* ((c-a (make-cutoff-alias w)) 
           (cutoff (car c-a)) 
           (alias (cadr c-a)) 
           (randi (random-source-make-integers s)) 
           (randu (random-source-make-reals s)) 
           (n (vector-length cutoff))) 
      (lambda () 
        (let ((i (randi n))) 
          (if (< (randu) (vector-ref cutoff i)) 
              i 
              (vector-ref alias i))))))
  
  )
