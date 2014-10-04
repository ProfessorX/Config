#lang racket/base
;; Copyright Neil Van Dyke -- see file "scribble.el".
;; $Id: scribble-emacs-dotemacs.rkt,v 1.10 2011/01/13 22:04:32 neilpair Exp $

(require racket/date
         (only-in racket/file make-temporary-file)
         (only-in racket/path normalize-path)
         (only-in mzlib/etc   this-expression-source-directory))

(define (find-dotemacs)
  (let ((home-path (find-system-path 'home-dir)))
    (let loop ((subs '((".emacs")
                       (".emacs.el")
                       (".emacs.d" "init.el")
                       ("_emacs")
                       ("_emacs.el"))))
      (if (null? subs)
          (error 'find-dotemacs
                 "Could not find Emacs init file under home: ~S"
                 home-path)
          (let ((path (apply build-path home-path (car subs))))
            (if (file-exists? path)
                path
                (loop (cdr subs))))))))

(define (get-emacs-require-filename)
  ;; Note: We return it without the ".el" suffix, to leave open the possibility
  ;; of later doing a byte-compile at package install time.  One of the
  ;; problems with byte-compile, however, is that we might get a ".elc" that at
  ;; some later point doesn't work with their current Emacs.
  ;;
  ;; TODO: Possibly document that power-users can byte-compile it in their
  ;; PLaneT directory...
  (let* ((el-path     (build-path (this-expression-source-directory)
                                  "scribble.el"))
         (el-filename (path->string el-path)))
    (if (file-exists? el-path)
        (regexp-replace #rx"\\.el$" el-filename "")
        (error 'get-emacs-require-filename
               "File does not exist: ~S"
               el-filename))))

(define begin-cookie-string ";;BEGIN-RACKET-SCRIBBLE-EMACS-INSTALL")
(define end-cookie-string   ";;END-RACKET-SCRIBBLE-EMACS-INSTALL")

(define (cookie-string->rx str)
  (regexp (string-append "^[ \t]*" (regexp-quote str) "[ \t]*\r?$")))

(define begin-cookie-rx (cookie-string->rx begin-cookie-string))
(define end-cookie-rx   (cookie-string->rx end-cookie-string))

(define (current-timestamp-string)
  (apply (lambda (whole date time)
           (string-append date "T" time "Z"))
         (regexp-match #rx"^([0-9]+-..-..) (..:..:..)$"
                       (parameterize ((date-display-format 'iso-8601))
                         (date->string (seconds->date (current-seconds) #f)
                                       #t)))))

(define (write-dotemacs-block require-filename port)
  ;; TODO: Worry about newline conventions, for the benefit of MS Windows.
  ;;
  ;; TODO: We are using the Racket writer to write out an Emacs Lisp string
  ;; literal.  In unusual situations of non-printable-ASCII characters in
  ;; filenames, this will fail.  We could write an Emacs Lisp-compatible string
  ;; writer.
  (let ((timestamp (current-timestamp-string)))
    (display    begin-cookie-string       port)
    (write-char #\newline                 port)
    (display    ";; Updated: "            port)
    (display    timestamp                 port)
    (write-char #\newline                 port)
    (display    "(condition-case err\n"   port)
    (display    "    (require 'scribble " port)
    (write      require-filename          port)
    (display    ")\n"                     port)
    (display "  (error (message \"Could not load Scribble Emacs: %s\" err)))\n" port)
    (display    end-cookie-string         port)
    (write-char #\newline                 port)))

(define (filter-dotemacs require-filename in out)
  ;; TODO: We could instead just do the entire thing with a regexp-replace.
  (let loop-find-block-begin ()
    (let ((line (read-line in 'any)))
      (cond ((eof-object? line)
             (log-info "Adding new Scribble Emacs install block.")
             (display "\n\n" out)
             (write-dotemacs-block require-filename out))
            ((regexp-match? begin-cookie-rx line)
             (log-info "Updating existing Scribble Emacs install block.")
             (write-dotemacs-block require-filename out)
             (let loop-find-block-end ()
               (let ((line (read-line in 'any)))
                 (cond
                  ((eof-object? line)
                   (error
                    'filter-dotemacs
                    "Could not find end cookie for Scribble Emacs install block."))
                  ((regexp-match end-cookie-rx line)
                   (let loop-to-eof ()
                     (let ((line (read-line in 'any)))
                       (if (eof-object? line)
                           (void)
                           (begin (display    line      out)
                                  (write-char #\newline out)
                                  (loop-to-eof))))))
                  (else (loop-find-block-end))))))
            (else (display line out)
                  (write-char #\newline out)
                  (loop-find-block-begin))))))

(define parent-path
  (let ((same-path (build-path 'same)))
    (lambda (path)
      (let-values (((base name dir?)
                    (split-path path)))
        (cond ((path? base)         base)
              ((eq? 'relative base) same-path)
              (else                 (error 'parent-path
                                           "Cannot get parent path of ~S"
                                           path)))))))

(define (update-dotemacs (dotemacs-path (find-dotemacs)))
  (let* ((dotemacs-path    (normalize-path (expand-user-path dotemacs-path)))
         (filter-out-path  (make-temporary-file "tmp-~a.el"
                                                #f
                                                (parent-path dotemacs-path)))
         (require-filename (get-emacs-require-filename)))
    (log-info (format "Installing Scribble Emacs into ~S..."
                      (path->string dotemacs-path)))
    (call-with-input-file dotemacs-path
      (lambda (in)
        (call-with-output-file filter-out-path
          (lambda (out)
            (filter-dotemacs require-filename in out)
            (let ((backup-path (path-add-suffix dotemacs-path ".bak")))
              (rename-file-or-directory dotemacs-path   backup-path   #t)
              (rename-file-or-directory filter-out-path dotemacs-path #f)
              (log-info (format "Installed Scribble Emacs into ~S."
                                (path->string dotemacs-path)))))
          #:mode   'text
          #:exists 'truncate))
      #:mode 'text)))

(provide update-dotemacs)
