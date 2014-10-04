#lang scribble/manual
@; $Id: scribble-emacs.scrbl,v 1.29 2013-09-28 04:51:57 user Exp $
@; Note: Changes to version number must be reflected in "scribble.el" and
@; "info.rkt".
@title[#:version "0.3"]{Racket Scribble Emacs Mode}

@author{Neil Van Dyke}

License: @seclink["Legal" #:underline? #f]{LGPL 3} @hspace[1]
Web: @hyperlink["http://www.neilvandyke.org/scribble-emacs/" #:underline? #f]{http://www.neilvandyke.org/scribble-emacs/}

@index['("Scribble")]
@index['("Emacs")]
@index['("documentation" "writing")]

@section[#:tag "Intro"]{Introduction}

This package provides an
@hyperlink["http://www.gnu.org/software/emacs/"]{Emacs} editing mode for Racket
@seclink["top" #:doc '(lib "scribblings/scribble/scribble.scrbl")]{Scribble}.

@subsection[#:tag "Features"]{Features}

The current version of this package provides a few features:
it
@itemlist[

@item{Syntax coloring/fontification.  Currently supported syntax is
@racket[scribble/base], @racket[scribble/bnf], and some of
@racket[scribble/manual].  (Note: This feature is currenty implemented using
regular expressions derived from a detailed grammar of various Scribble
procedures and special syntax.  This might change in the future, since regular
expressions are not very appropriate.)}

@item{Syntax quick-reference help in the echo area, when clicking on a name in
at-sign syntax.  This is implemented using the encoded grammar and ElDoc.}

@item{Completion of Scribble functions, special syntax, and keywords, using
M-TAB.}

@item{Various hints to Emacs about the syntax of Scribble.}

@item{Menu-based navigation to particular section headings, using Imenu.}

]

Some additional features are planned.

@subsection[#:tag "Requirements"]{Requirements}

This package is being developed with GNU Emacs 23.2 on GNU/Linux.  There is an
intention to have it portable to GNU Emacs 23 and 22 on all popular host OS
platforms those Emacs versions support, so please let me know if you find
compatibility problems.

This package currently uses the ``DejaVu'' fonts explicitly.

@section[#:tag "Install"]{Installation}

This package is currently distributed through PLaneT.  There are two
alternatives for installation:

@itemlist[

@item{Evaluate the following Racket code to install the PLaneT package and to
modify your personal Emacs initialization file (usually @tt{~/.emacs}) to load
the @tt{scribble.el} file when you start Emacs.

@RACKETBLOCK[(require (planet neil/scribble-emacs:1:2/install-in-my-emacs))]

You can safely evaluate this code many times, such as to install new versions,
and the configuration in your Emacs initialization file will be updated
appropriately.}

@item{Evaluate the following Racket code to install the PLaneT package without
modifying your Emacs setup.

@RACKETBLOCK[(require (planet neil/scribble-emacs:1:2))]}

]

@section[#:tag "History"]{History}
      
@; Changes to PLaneT version should also be reflected in the two "require"
@; forms above.

@itemlist[
@item{Version 0.4 --- 2013-09-28 - PLaneT @tt{(1 3)}

    Added @tt{code} and @tt{codeblock}.  (Thanks to Rommel M. Martinez.)

}
@item{Version 0.3 --- 2011-01-10 - PLaneT @tt{(1 2)}

    Added M-TAB completion of Scribble functions, syntax, and keywords.

}
@item{Version 0.2 --- 2011-01-09 - PLaneT @tt{(1 1)}

    Documentation fix.

}
@item{Version 0.1 --- 2011-01-09 - PLaneT @tt{(1 0)}

    Initial release.

}
]

@section[#:tag "Legal"]{Legal}

@; Note: Changes to legal information must be reflected in "scribble.el".

@(require (only-in racket/base string))

Copyright @(string #\u00a9) 2011 Neil Van Dyke.  This program is Free
Software; you can redistribute it and/or modify it under the terms of the GNU
Lesser General Public License as published by the Free Software Foundation;
either version 3 of the License (LGPL 3), or (at your option) any later
version. This program is distributed in the hope that it will be useful, but
without any warranty; without even the implied warranty of merchantability or
fitness for a particular purpose.  See http://www.gnu.org/licenses/ for
details.  For other licenses and consulting, please contact the author.
