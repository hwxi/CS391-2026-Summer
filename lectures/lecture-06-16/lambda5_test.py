##################################################################
#
# HX: let's use dataclasses
# HX: let's do type-checking
# Tue Jun 16 05:36:49 PM EDT 2026
#
##################################################################
import sys
##################################################################
from lambda5 import *
##################################################################
sys.setrecursionlimit(10000)
##################################################################
STint = STbas("sint")
STbtf = STbas("bool")
STstr = STbas("strn")
STfun_i_i = STfun(STint, STint)
# STfun_i_i_i: Haskell Curry style
STfun_i_i_i = STfun(STint, STfun(STint, STint))
STfun_ixi_i = STfun(STtup(STint, STint), STint)
_ = print("STfun_i_i_i = " + repr(STfun_i_i_i))
_ = print("STfun_ixi_i = " + repr(STfun_ixi_i))
##################################################################
DE_0 = DEint(0)
DE_1 = DEint(1)
DE_2 = DEint(2)
DE_3 = DEint(3)
DE_f = DEvar("f")
DE_n = DEvar("n")
DE_x = DEvar("x")
##################################################################

dex01 = DElam1("x", STint, DE_0)
dex02 = DElam1("x", STint, DE_x)
dex03 = DEapp(dex01, DE_1)
dex04 = DEapp(dex02, DEbtf(True))
dex05 = DElam("x", DE_x)
dex06 = DEapp(dex05, DEbtf(True))
print("oftp(dex01) = ", dexp_oftp000(dex01))
print("oftp(dex02) = ", dexp_oftp000(dex02))
print("oftp(dex03) = ", dexp_oftp000(dex03))
# print("oftp(dex04) = ", dexp_oftp000(dex04))
print("oftp(dex05) = ", dexp_oftp000(dex05))
print("oftp(dex06) = ", dexp_oftp000(dex06))

##################################################################
dexp_fact_fix1 = \
DEfix1("f", "n", STint, STint,
  DEif0(DEop2("<=", DE_n, DE_0), DE_1,
    DEop2("*", DE_n, DEapp(DE_f, DEop2("-", DE_n, DE_1)))))
_ = print("dexp_fact_fix1 = ", dexp_fact_fix1)
_ = print("oftp(dexp_fact_fix1) = ", dexp_oftp000(dexp_fact_fix1))
##################################################################
##################################################################
# end of [CS391-2026-Summer/lectures/lecture-06-16/lambda5_test.py]
##################################################################
##################################################################
