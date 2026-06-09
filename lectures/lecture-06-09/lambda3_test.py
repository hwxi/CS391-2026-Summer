##################################################################
#
# HX: let's use dataclasses
# HX: let's do type-checking
# Tue Jun  9 08:08:43 AM EDT 2026
#
##################################################################
import sys
sys.setrecursionlimit(10000)
##################################################################
from lambda3 import *
##################################################################
TM_f = TMvar("f")
TM_i = TMvar("i")
TM_n = TMvar("n")
TM_x = TMvar("x")
TM_y = TMvar("y")
TM_z = TMvar("z")
##################################################################
TM_I = TMlam("x", TM_x)
TM_K = TMlam("x", TMlam("y", TM_x))
TM_S = TMlam("x", TMlam("y", TMlam("z", TMapp(TMapp(TM_x, TM_z), TMapp(TM_y, TM_z)))))
##################################################################
print("TM_f = " + repr(TM_f))
print("TM_I = " + repr(TM_I))
print("TM_K = " + repr(TM_K))
print("TM_S = " + repr(TM_S))
##################################################################
DE_0 = DEint(0)
DE_1 = DEint(1)
DE_2 = DEint(2)
DE_3 = DEint(3)
DE_f = DEvar("f")
DE_n = DEvar("n")
DE_x = DEvar("x")
##################################################################
# let x = 2+3 in x*x
dexp_let1 = DElet("x", DEop2("+", DE_2, DE_3), DEop2("*", DE_x, DE_x))
_ = print("dexp_let1 = ", dexp_let1)
_ = print("dexp_let1 = ", dexp_eval000(dexp_let1))
##################################################################
dexp_fact_fix = \
DEfix("f", "n",
  DEif0(DEop2("<=", DE_n, DE_0), DE_1,
    DEop2("*", DE_n, DEapp(DE_f, DEop2("-", DE_n, DE_1)))))
_ = print("dexp_fact_fix = ", dexp_fact_fix)
_ = print("dexp_fact_fix(3) = ", dexp_eval000(DEapp(dexp_fact_fix, DEint(3))))
_ = print("dexp_fact_fix(5) = ", dexp_eval000(DEapp(dexp_fact_fix, DEint(5))))
_ = print("dexp_fact_fix(10) = ", dexp_eval000(DEapp(dexp_fact_fix, DEint(10))))
##################################################################
# end of [CS391-2026-Summer/lectures/lecture-06-09/lambda3_test.py]
##################################################################
