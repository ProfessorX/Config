#lang scribble/doc
@; This is a comment.
@(require scribble/manual)
@title{My Example Document}

@author{Jane Smith}

@section[#:tag "intro"]{First Section}

There is @bold{boldface} and @emph{emphasized} and @tt{typewriter} text.  Blah
blah.  The @@ sign.  @PLaneT Blah blah blah.  And @hyperlink{Some Hyperlink}.

@subsection[#:tag "intrigue"]{A Subsection}

@subsubsection[#:tag "intrigue"]{A Sub-Subsection}

@sub*section[#:tag "intrigue"]{A Sub-Something-Section}

@section[#:tag "bnf"]{BNF}

This example was taken from Scribble documentation.

@(let ([open @litchar{(}]
       [close @litchar{)}])
   @BNF[(list @nonterm{expr}
              @nonterm{id}
              @BNF-seq[open @kleeneplus[@nonterm{expr}] close]
              @BNF-seq[open @litchar{lambda}
                       open @kleenestar[@nonterm{id}] close
                       @nonterm{expr} close]
              @nonterm{val})
        (list @nonterm{val}
              @BNF-alt[@nonterm{number} @nonterm{primop}])
        (list @nonterm{id}
              @elem{any name except for @litchar{lambda}})])
