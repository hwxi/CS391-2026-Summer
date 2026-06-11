##################################################################
#
# HX: let's use dataclasses
# HX: let's do type-checking
# Tue Jun  9 08:08:43 AM EDT 2026
#
##################################################################
type nint = int
type sint = int
type strn = str
##################################################################
from abc import ABC
from enum import Enum
from dataclasses import dataclass
##################################################################
#
# HX-2026-06-09:
# For Church's pure lambda-calculus
#
type tvar = strn
type term = TM000
##################################################################
@dataclass
class TM000(ABC):
    pass
@dataclass
class TMvar(TM000):
    arg1: tvar
    pass
@dataclass
class TMlam(TM000):
    arg1: tvar
    arg2: term
    pass
@dataclass
class TMapp(TM000):
    arg1: term
    arg2: term
    pass
##################################################################
def \
term_subst0\
(tm0: term, tx0: tvar, sub: term) -> term:
    def subst0(tm0: term) -> term:
        return term_subst0(tm0, tx0, sub)
    if isinstance(tm0, TMvar):
        tx1 = tm0.arg1
        if tx0 == tx1:
            return sub
        else:
            return tm0
    if isinstance(tm0, TMlam):
        tx1 = tm0.arg1
        if tx0 == tx1:
            return tm0
        else:
            return TMlam(tx1, subst0(tm0.arg2))
    if isinstance(tm0, TMapp):
        return TMapp(subst0(tm0.arg1), subst0(tm0.arg2))
    raise TypeError(tm0) # HX-2026-06-09: should be deadcode!
##################################################################
##################################################################
type dvar = strn
type dexp = DE000
##################################################################
@dataclass
class DE000(ABC):
    pass
@dataclass
class DEint(DE000):
    arg1: sint
    pass
@dataclass
class DEbtf(DE000):
    arg1: bool
    pass
@dataclass
class DEstr(DE000):
    arg1: strn
    pass
@dataclass
class DEvar(DE000):
    arg1: dvar
    pass
@dataclass
class DElam(DE000):
    arg1: dvar
    arg2: dexp
    pass
@dataclass
class DEapp(DE000):
    arg1: dexp
    arg2: dexp
    pass
@dataclass
class DEop1(DE000):
    arg1: strn
    arg2: dexp
    pass
@dataclass
class DEop2(DE000):
    arg1: strn
    arg2: dexp
    arg3: dexp
    pass
@dataclass
class DEif0(DE000):
    arg1: dexp
    arg2: dexp
    arg3: dexp
    pass
@dataclass
class DEfst(DE000):
    arg1: dexp
    pass
@dataclass
class DEsnd(DE000):
    arg1: dexp
    pass
@dataclass
class DEtup(DE000):
    arg1: dexp
    arg2: dexp
    pass
@dataclass
class DEfix(DE000):
    arg1: dvar
    arg2: dvar
    arg3: dexp
    pass
@dataclass
class DElet(DE000):
    arg1: dvar
    arg2: dexp
    arg3: dexp
    pass
##################################################################
type dval = DV000
##################################################################
type xvenv = ENV000
##################################################################
@dataclass
class DV000(ABC):
    pass    
@dataclass
class DVint(DV000):
    arg1: sint
    pass
@dataclass
class DVbtf(DV000):
    arg1: bool
    pass
@dataclass
class DVstr(DV000):
    arg1: strn
    pass
@dataclass
class DVtup(DV000):
    arg1: dval
    arg2: dval
    pass
@dataclass
class DVlam(DV000):
    arg1: DElam
    arg2: xvenv
    pass
@dataclass
class DVfix(DV000):
    arg1: DEfix
    arg2: xvenv
    pass
##################################################################
@dataclass
class ENV000(ABC):
    pass    
@dataclass
class ENVnil(ENV000):
    pass    
@dataclass
class ENVcons(ENV000):
    arg1: dvar
    arg2: dval
    arg3: xvenv
    pass    
##################################################################
def \
xvenv_search\
(xvs: xvenv, dx0: dvar) -> dval:
    while True:
        if isinstance(xvs, ENVnil):
            return DV000()
        if isinstance(xvs, ENVcons):
            if dx0 == xvs.arg1:
                return xvs.arg2
            else:
                xvs = xvs.arg3; continue
        raise TypeError(xvs) # HX-2026-06-02: should be deadcode!    
##################################################################

def dexp_eval000(dex: dexp):
    return dexp_evalenv(dex, ENVnil())

def dop1_eval\
(opr: strn, dv1: dval) -> dval:
    if (opr == "-"):
        assert isinstance(dv1, DVint)
        return DVint(   -(dv1.arg1)   )
    if (opr == "print"):
        if isinstance(dv1, DVint):
            print(dv1.arg1, end='')
            return DVint(      0      )
        elif isinstance(dv1, DVbtf):
            print(dv1.arg1, end='')
            return DVint(      0      )
        elif isinstance(dv1, DVstr):
            print(dv1.arg1, end='')
            return DVint(      0      )
        elif isinstance(dv1, DVlam):
            print("DVlam(...)", end='')
            return DVint(      0      )
        elif isinstance(dv1, DVfix):
            print("DVfix(...)", end='')
            return DVint(      0      )
        else:
            print(dv1, end=''); return DVint(0)
    raise TypeError(opr) # HX-2026-06-09: dop1_eval(...)

def dop2_eval\
(opr: strn, dv1: dval, dv2: dval) -> dval:
    if (opr == "+"):
        assert isinstance(dv1, DVint)
        assert isinstance(dv2, DVint)
        return DVint(dv1.arg1 + dv2.arg1)
    if (opr == "-"):
        assert isinstance(dv1, DVint)
        assert isinstance(dv2, DVint)
        return DVint(dv1.arg1 - dv2.arg1)
    if (opr == "*"):
        assert isinstance(dv1, DVint)
        assert isinstance(dv2, DVint)
        return DVint(dv1.arg1 * dv2.arg1)
    if (opr == "%"):
        assert isinstance(dv1, DVint)
        assert isinstance(dv2, DVint)
        return DVint(dv1.arg1 % dv2.arg1)
    if (opr == "/"):
        assert isinstance(dv1, DVint)
        assert isinstance(dv2, DVint)
        return DVint(dv1.arg1 // dv2.arg1)
    if (opr == "<"):
        assert isinstance(dv1, DVint)
        assert isinstance(dv2, DVint)
        return DVbtf(dv1.arg1 < dv2.arg1)
    if (opr == ">"):
        assert isinstance(dv1, DVint)
        assert isinstance(dv2, DVint)
        return DVbtf(dv1.arg1 > dv2.arg1)
    if (opr == "<="):
        assert isinstance(dv1, DVint)
        assert isinstance(dv2, DVint)
        return DVbtf(dv1.arg1 <= dv2.arg1)
    if (opr == ">="):
        assert isinstance(dv1, DVint)
        assert isinstance(dv2, DVint)
        return DVbtf(dv1.arg1 >= dv2.arg1)
    if (opr == "=="):
        assert isinstance(dv1, DVint)
        assert isinstance(dv2, DVint)
        return DVbtf(dv1.arg1 == dv2.arg1)
    if (opr == "!="):
        assert isinstance(dv1, DVint)
        assert isinstance(dv2, DVint)
        return DVbtf(dv1.arg1 != dv2.arg1)
    raise TypeError(opr) # HX-2026-06-09: dop2_eval(...)

def dexp_evalenv(dex: dexp, env0: xvenv) -> dval:
    if isinstance(dex, DEint):
        return DVint(dex.arg1)
    if isinstance(dex, DEbtf):
        return DVbtf(dex.arg1)
    if isinstance(dex, DEstr):
        return DVstr(dex.arg1)
    if isinstance(dex, DElam):
        return DVlam(dex, env0)
    if isinstance(dex, DEfix):
        return DVfix(dex, env0)
    if isinstance(dex, DEvar):
        return \
            xvenv_search(env0, dex.arg1)
    if isinstance(dex, DEapp):
        dv1 = dexp_evalenv(dex.arg1, env0)
        dv2 = dexp_evalenv(dex.arg2, env0)
        if isinstance(dv1, DVlam):
            dv1_dlam = dv1.arg1
            dv1_env0 = dv1.arg2
            dv1_dvar = dv1_dlam.arg1
            dv1_body = dv1_dlam.arg2
            dv1_env1 = \
                ENVcons(dv1_dvar, dv2, dv1_env0)
            return dexp_evalenv(dv1_body, dv1_env1)
        if isinstance(dv1, DVfix):
            dv1_dfix = dv1.arg1
            dv1_env0 = dv1.arg2
            dv1_dfun = dv1_dfix.arg1
            dv1_dvar = dv1_dfix.arg2
            dv1_body = dv1_dfix.arg3
            dv1_env1 = \
                ENVcons(dv1_dfun, dv1, dv1_env0)
            dv1_env2 = \
                ENVcons(dv1_dvar, dv2, dv1_env1)
            return dexp_evalenv(dv1_body, dv1_env2)
        raise TypeError(dv1) # HX-2026-06-09: non-function!
    if isinstance(dex, DEtup):
        dv1 = dexp_evalenv(dex.arg1, env0)
        dv2 = dexp_evalenv(dex.arg2, env0)
        return DVtup(dv1, dv2)
    if isinstance(dex, DEfst):
        tup = dexp_evalenv(dex.arg1, env0)
        if isinstance(tup, DVtup):
            return tup.arg1
        else:
            raise TypeError(tup)
    if isinstance(dex, DEsnd):
        tup = dexp_evalenv(dex.arg1, env0)
        if isinstance(tup, DVtup):
            return tup.arg2
        else:
            raise TypeError(tup)
    if isinstance(dex, DEop2):
        opr = dex.arg1
        dv1 = dexp_evalenv(dex.arg2, env0)
        dv2 = dexp_evalenv(dex.arg3, env0)
        return dop2_eval(opr, dv1, dv2)
    if isinstance(dex, DEif0):
        dv1 = dexp_evalenv(dex.arg1, env0)
        assert isinstance(dv1, DVbtf)
        if dv1.arg1:
            return dexp_evalenv(dex.arg2, env0)
        else:
            return dexp_evalenv(dex.arg3, env0)
    if isinstance(dex, DElet):
        # let x = de1 in de2
        dx0 = dex.arg1
        de1 = dex.arg2
        dv1 = dexp_evalenv(de1, env0)
        env1 = ENVcons(dx0, dv1, env0)
        return dexp_evalenv(dex.arg3, env1)
    raise TypeError(dex) # HX-2026-06-09: dexp_evalenv(...)

##################################################################
##################################################################
# end of [CS391-2026-Summer/lectures/lecture-06-09/lambda3.py]
##################################################################
##################################################################
