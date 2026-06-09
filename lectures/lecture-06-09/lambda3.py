############################################################
#
# HX: let's use dataclasses
# HX: let's do type-checking
# Tue Jun  9 08:08:43 AM EDT 2026
#
############################################################
type sint = int
type strn = str
############################################################
from abc import ABC
from enum import Enum
from dataclasses import dataclass
############################################################
#
# HX-2026-06-09:
# For Church's pure lambda-calculus
#
type tvar = strn
type term = TM000 \
    | TMvar | TMlam | TMapp \
############################################################
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
############################################################
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
############################################################
############################################################
type dvar = strn
type dexp = DE000 \
    | DEint | DEbtf | DEstr \
    | DEvar | DElam | DEapp \
    | DEop1 | DEop2 | DEif0 \
    | DEfst | DEsnd | DEtup | DEfix
############################################################
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
############################################################
type value = VAL000 \
    | VALint | VALbtf | VALstr \
    | VALtup | VALlam | VALfix \
############################################################
type xvenv = ENV000 | ENVnil | ENVcons
############################################################
@dataclass
class VAL000(ABC):
    pass    
@dataclass
class VALint(VAL000):
    arg1: sint
    pass
@dataclass
class VALbtf(VAL000):
    arg1: bool
    pass
@dataclass
class VALstr(VAL000):
    arg1: strn
    pass
@dataclass
class VALtup(VAL000):
    arg1: value
    arg2: value
    pass
@dataclass
class VALlam(VAL000):
    arg1: DElam
    arg2: xvenv
    pass
@dataclass
class VALfix(VAL000):
    arg1: DEfix
    arg2: xvenv
    pass
############################################################
@dataclass
class ENV000(ABC):
    pass    
@dataclass
class ENVnil(ABC):
    pass    
@dataclass
class ENVcons(ABC):
    arg1: dvar
    arg2: value
    arg3: xvenv
    pass    
############################################################
def \
xvenv_search\
(xvs: xvenv, dx0: dvar) -> value:
    while True:
        if isinstance(xvs, ENVnil):
            return VAL000()
        if isinstance(xvs, ENVcons):
            if dx0 == xvs.arg1:
                return xvs.arg2
            else:
                xvs = xvs.arg3; continue
        raise TypeError(xvs) # HX-2026-06-02: should be deadcode!    
############################################################

def dexp_eval000(dex: dexp):
    return dexp_evalenv(dex, ENVnil())

def dop2_eval\
(opr: strn, vl1: value, vl2: value) -> value:
    if (opr == "+"):
        assert isinstance(vl1, VALint)
        assert isinstance(vl2, VALint)
        return VALint(vl1.arg1 + vl2.arg1)
    if (opr == "-"):
        assert isinstance(vl1, VALint)
        assert isinstance(vl2, VALint)
        return VALint(vl1.arg1 - vl2.arg1)
    if (opr == "*"):
        assert isinstance(vl1, VALint)
        assert isinstance(vl2, VALint)
        return VALint(vl1.arg1 * vl2.arg1)
    if (opr == "%"):
        assert isinstance(vl1, VALint)
        assert isinstance(vl2, VALint)
        return VALint(vl1.arg1 % vl2.arg1)
    if (opr == "/"):
        assert isinstance(vl1, VALint)
        assert isinstance(vl2, VALint)
        return VALint(vl1.arg1 // vl2.arg1)
    if (opr == "<"):
        assert isinstance(vl1, VALint)
        assert isinstance(vl2, VALint)
        return VALbtf(vl1.arg1 < vl2.arg1)
    if (opr == ">"):
        assert isinstance(vl1, VALint)
        assert isinstance(vl2, VALint)
        return VALbtf(vl1.arg1 > vl2.arg1)
    if (opr == "<="):
        assert isinstance(vl1, VALint)
        assert isinstance(vl2, VALint)
        return VALbtf(vl1.arg1 <= vl2.arg1)
    if (opr == ">="):
        assert isinstance(vl1, VALint)
        assert isinstance(vl2, VALint)
        return VALbtf(vl1.arg1 >= vl2.arg1)
    if (opr == "=="):
        assert isinstance(vl1, VALint)
        assert isinstance(vl2, VALint)
        return VALbtf(vl1.arg1 == vl2.arg1)
    if (opr == "!="):
        assert isinstance(vl1, VALint)
        assert isinstance(vl2, VALint)
        return VALbtf(vl1.arg1 != vl2.arg1)
    raise TypeError(opr) # HX-2026-06-09: dop2_eval(...)

def dexp_evalenv(dex: dexp, env0: xvenv) -> value:
    if isinstance(dex, DEint):
        return VALint(dex.arg1)
    if isinstance(dex, DEbtf):
        return VALbtf(dex.arg1)
    if isinstance(dex, DEstr):
        return VALstr(dex.arg1)
    if isinstance(dex, DElam):
        return VALlam(dex, env0)
    if isinstance(dex, DEfix):
        return VALfix(dex, env0)
    if isinstance(dex, DEvar):
        return \
            xvenv_search(env0, dex.arg1)
    if isinstance(dex, DEapp):
        vl1 = dexp_evalenv(dex.arg1, env0)
        vl2 = dexp_evalenv(dex.arg2, env0)
        if isinstance(vl1, VALlam):
            vl1_dlam = vl1.arg1
            vl1_env0 = vl1.arg2
            vl1_dvar = vl1_dlam.arg1
            vl1_body = vl1_dlam.arg2
            vl1_env1 = \
                ENVcons(vl1_dvar, vl2, vl1_env0)
            return dexp_evalenv(vl1_body, vl1_env1)
        if isinstance(vl1, VALfix):
            vl1_dfix = vl1.arg1
            vl1_env0 = vl1.arg2
            vl1_dfun = vl1_dfix.arg1
            vl1_dvar = vl1_dfix.arg2
            vl1_body = vl1_dfix.arg3
            vl1_env1 = \
                ENVcons(vl1_dfun, vl1, vl1_env0)
            vl1_env2 = \
                ENVcons(vl1_dvar, vl2, vl1_env1)
            return dexp_evalenv(vl1_body, vl1_env2)
        raise TypeError(vl1) # HX-2026-06-09: non-function!
    if isinstance(dex, DEtup):
        vl1 = dexp_evalenv(dex.arg1, env0)
        vl2 = dexp_evalenv(dex.arg2, env0)
        return VALtup(vl1, vl2)
    if isinstance(dex, DEfst):
        tup = dexp_evalenv(dex.arg1, env0)
        if isinstance(tup, VALtup):
            return tup.arg1
        else:
            raise TypeError(tup)
    if isinstance(dex, DEsnd):
        tup = dexp_evalenv(dex.arg1, env0)
        if isinstance(tup, VALtup):
            return tup.arg2
        else:
            raise TypeError(tup)
    if isinstance(dex, DEop2):
        opr = dex.arg1
        vl1 = dexp_evalenv(dex.arg2, env0)
        vl2 = dexp_evalenv(dex.arg3, env0)
        return dop2_eval(opr, vl1, vl2)
    if isinstance(dex, DEif0):
        vl1 = dexp_evalenv(dex.arg1, env0)
        assert isinstance(vl1, VALbtf)
        if vl1.arg1:
            return dexp_evalenv(dex.arg2, env0)
        else:
            return dexp_evalenv(dex.arg3, env0)
    raise TypeError(dex) # HX-2026-06-09: dexp_evalenv(...)

############################################################
# end of [CS391-2026-Summer/lectures/lecture-06-09/lambda3.py]
############################################################
