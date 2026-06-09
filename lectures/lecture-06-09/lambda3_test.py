############################################################
from lambda3 import *
############################################################
TM_f = TMvar("f")
TM_i = TMvar("i")
TM_n = TMvar("n")
TM_x = TMvar("x")
TM_y = TMvar("y")
TM_z = TMvar("z")
############################################################
TM_I = TMlam("x", TM_x)
TM_K = TMlam("x", TMlam("y", TM_x))
TM_S = TMlam("x", TMlam("y", TMlam("z", TMapp(TMapp(TM_x, TM_z), TMapp(TM_y, TM_z)))))
############################################################
print("TM_f = " + repr(TM_f))
print("TM_I = " + repr(TM_I))
print("TM_K = " + repr(TM_K))
print("TM_S = " + repr(TM_S))
############################################################
DE_0 = DEint(0)
DE_1 = DEint(1)
DE_2 = DEint(2)
DE_f = DEvar("f")
DE_n = DEvar("n")
############################################################
dexp_fact_fix = \
DEfix("f", "n",
  DEif0(DEop2("<=", DE_n, DE_0), DE_1,
    DEop2("*", DE_n, DEapp(DE_f, DEop2("-", DE_n, DE_1)))))
_ = print("dexp_fact_fix = ", dexp_fact_fix)

_ = print("dexp_fact_fix(3) = ", dexp_eval000(DEapp(dexp_fact_fix, DEint(3))))
_ = print("dexp_fact_fix(10) = ", dexp_eval000(DEapp(dexp_fact_fix, DEint(10))))
############################################################
