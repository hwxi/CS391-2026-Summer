# Assignment 4 for CS391X1, Summer I, 2026

## Total points: 100

In lectures/lecture-06-09, we covered the topic of
code emission. The following function is for compiling
a dynamic expression (dexp) into a dynamic computation
(which consists of a sequence of instructions plus a treg)

def dexp_comp000(dex: dexp) -> dcmp: ...

And the following one is for emitting a sequence of instructions
(where [nind] is an integer for the amount of indentation needed)

def dinslst_emit000(inss: list[dins], nind: sint): ...

Please see some related testing code in lambda4_test.py.

## Description of the task

The LAMBDA programming language now has the following
language constructs.

datatype dexp =
//
| DEint of sint
| DEbtf of bool
| DEstr of strn
//
| DEvar of dvar
| DElam of
( dvar, dexp(*body*))
| DEapp of
( dexp(*fun*), dexp(*arg*))
//
| DEopr of (strn, list(dexp))
//
| DEfst of (dexp)
| DEsnd of (dexp)
| DEtup of (dexp, dexp)
//
| DEif0 of
( dexp(*test*)
, dexp(*then*), dexp(*else*))
//
| DEfix of
( dvar(*fun*)
, dvar(*arg*), dexp(*body*))
//
| DElet of
( dvar(*x*)
, dexp(*def*), dexp(*scope*))
//
| DElist_nil of ()
| DElist_cons of (dexp, dexp)
//
| DElazy of dexp
| DEstcn_nil of ()
| DEstcn_cons of (dexp, dexp)
//
| DEarry_size$val of (dexp(*size*), dexp(*val*))
| DEarry_size$fun of (dexp(*size*), dexp(*fun*))

Your task is to extend lambda3.py and lambda4.py with code
that handles the following ones:
//
// For lists (50 points)
// You need the following operators:
// list_nilq, list_head, and list_tail
| DElist_nil of ()
| DElist_cons of (dexp, dexp)
//
// For streams (100 points)
// You need the following operators:
// stcn_nilq, stcn_head, and stcn_tail
| DElazy of dexp
| DEstcn_nil of ()
| DEstcn_cons of (dexp, dexp)
//
// For arrays (100 points)
// What operations do you need for supporting
// arrays?
| DEarry_size$val of (dexp(*size*), dexp(*val*))
| DEarry_size$fun of (dexp(*size*), dexp(*fun*))

I expect that you submission can compile successfully:
1: fact and fact2
2: 8-queen puzzle (assign03)
3: fnlist_tally/fnlist_range1 (Quiz03)

## Submission

You are expected to have all of your submitted code in one file of
the name `assign04.py`; this file should be stored in the directory
of the name `assigns/04/MySolution`. Please visit the following page
for information on creating a private repository of your own for this
class:

```
https://github.com/hwxi/CS391-2026-Summer/blob/main/README.md
```
