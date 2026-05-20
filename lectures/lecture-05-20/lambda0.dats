(* ****** ****** *)
(* ****** ****** *)
//
// HX-2026-05-20:
// This is like declaring a class
// and also have some constructors
//
// Concrete syntax for source code
// Parser for parsing source code into abstract syntax tree
//
datatype term = // for abstract syntax tree (AST)
// These are for pure lambda-terms
| TMvar of strn // for contructing a variable/name
| TMlam of (strn(*name*), term(*body*)) // for constructing an abstraction
| TMapp of (term(*function*), term(*argument*)) // for constructing an application
//
(*
| TMint of sint
| TMbtf of bool
| TMstr of strn
*)
//
(* ****** ****** *)
(* ****** ****** *)
  
fun
term_print
(t0: term): void =
(
case+ t0 of
//
|
TMvar(x0) =>
prints("TMvar(", x0, ")")
//
|
TMlam(x0, t1) =>
prints("TMlam(", x0, ";", t1, ")")
//
|
TMapp(t1, t2) =>
prints("TMapp(", t1, ";", t2, ")")
//
) where
{
  #impltmp
  g_print<term> = term_print
}(*where*)//end-of-[term_print(t0)]

(* ****** ****** *)
//
fun
term_size
(t0: term): sint =
(
case+ t0 of
|
TMvar(x0) => 1
|
TMlam(x0, t1) =>
1 + term_size(t1)
|
TMapp(t1, t2) =>
(1+term_size(t1)+term_size(t2))
)
//
(* ****** ****** *)
//
(*
HX-2026-05-20:
term_subst
(t0, x0, u0) = t0[x0->u0]
*)
#extern
fun
term_subst
( t0: term
, x0: strn, u0: term): term
//
#implfun
term_subst
(t0, x0, u0) =
(
case+ t0 of
|TMvar(x1) =>
 if x0 = x1 then u0 else t0
|TMlam(x1, t1) =>
 if x0 = x1
 then t0 else TMlam(x1, term_subst(t1, x0, u0))
|TMapp(t1, t2) =>
 TMapp(term_subst(t1, x0, u0), term_subst(t2, x0, u0))
)(*case+*)//end-of-[term_subst(t0,x0,u0)]
//
(* ****** ****** *)
(* ****** ****** *)
//
(***********************************************************************)
(* end of [CS391-2026-Summer/lectures/lecture-05-20/lambda0.dats] *)
(***********************************************************************)
