user_link_targets[0] = [
 ["(part._(.'(planet._scribble-emacs..scrbl._(neil._scribble-emacs..plt._1._3)).'._.'.Features.'))", "file:///home/abrahamx/.racket/planet/300/6.1/cache/neil/scribble-emacs.plt/1/3/doc/scribble-emacs/index.html#%28part._.Features%29"],
 ["(part._(.'(planet._scribble-emacs..scrbl._(neil._scribble-emacs..plt._1._3)).'._.'.History.'))", "file:///home/abrahamx/.racket/planet/300/6.1/cache/neil/scribble-emacs.plt/1/3/doc/scribble-emacs/index.html#%28part._.History%29"],
 ["(part._(.'(planet._scribble-emacs..scrbl._(neil._scribble-emacs..plt._1._3)).'._.'.Install.'))", "file:///home/abrahamx/.racket/planet/300/6.1/cache/neil/scribble-emacs.plt/1/3/doc/scribble-emacs/index.html#%28part._.Install%29"],
 ["(part._(.'(planet._scribble-emacs..scrbl._(neil._scribble-emacs..plt._1._3)).'._.'.Intro.'))", "file:///home/abrahamx/.racket/planet/300/6.1/cache/neil/scribble-emacs.plt/1/3/doc/scribble-emacs/index.html#%28part._.Intro%29"],
 ["(part._(.'(planet._scribble-emacs..scrbl._(neil._scribble-emacs..plt._1._3)).'._.'.Legal.'))", "file:///home/abrahamx/.racket/planet/300/6.1/cache/neil/scribble-emacs.plt/1/3/doc/scribble-emacs/index.html#%28part._.Legal%29"],
 ["(part._(.'(planet._scribble-emacs..scrbl._(neil._scribble-emacs..plt._1._3)).'._.'.Racket_.Scribble_.Emacs_.Mode.'))", "file:///home/abrahamx/.racket/planet/300/6.1/cache/neil/scribble-emacs.plt/1/3/doc/scribble-emacs/index.html"],
 ["(part._(.'(planet._scribble-emacs..scrbl._(neil._scribble-emacs..plt._1._3)).'._.'.Requirements.'))", "file:///home/abrahamx/.racket/planet/300/6.1/cache/neil/scribble-emacs.plt/1/3/doc/scribble-emacs/index.html#%28part._.Requirements%29"],
 ["(part._(.'(planet._scribble-emacs..scrbl._(neil._scribble-emacs..plt._1._3)).'._.'top.'))", "file:///home/abrahamx/.racket/planet/300/6.1/cache/neil/scribble-emacs.plt/1/3/doc/scribble-emacs/index.html"]];


function user_convert_all_links_0() {
   var elements = document.getElementsByClassName("Sq");
   for (var i = 0; i < elements.length; i++) {
     var elem = elements[i];
     var tag = elem.href.match(/tag=[^&]*/);
     
     if (tag) {
       var pos = user_bsearch(decodeURIComponent(tag[0].substring(4)),
                                   user_link_targets[0],
                                   0,
                                   user_link_targets[0].length);
       if (pos) {
         var p = user_link_targets[0][pos][1];
         if (user_link_target_prefix) {
           p = user_link_target_prefix + p;
         }
         elem.href = p;
       }
     }
  }
}
user_convert_all_links_0();
