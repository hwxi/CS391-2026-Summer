##################################################################
#
# HX: let's use dataclasses
# HX: let's do type-checking
# Tue Jun 15 08:08:43 AM EDT 2026
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
type styp = ST000
##################################################################
type dvar = strn
type dexp = DE000
##################################################################
@dataclass
class ST000(ABC):
    pass
##################################################################
@dataclass
class STbas(ST000):
    arg1: strn
    pass
##################################################################
@dataclass
class STfun(ST000):
    arg1: styp
    arg2: styp
    pass
@dataclass
class STtup(ST000):
    arg1: styp
    arg2: styp
    pass
##################################################################
@dataclass
class STlist(ST000):
    arg1: styp
    pass
@dataclass
class STstrm(ST000):
    arg1: styp
    pass
@dataclass
class STstcn(ST000):
    arg1: styp
    pass
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
@dataclass
class DElam1(DE000):
    arg1: dvar
    arg2: styp
    arg3: dexp
    pass
@dataclass
class DEfix1(DE000):
    arg1: dvar
    arg2: dvar
    arg3: styp # arg
    arg4: styp # res
    arg5: dexp
    pass
@dataclass
class DEanno(DE000):
    arg1: dexp
    arg2: styp
    pass
##################################################################
type xtctx = SCTX000
##################################################################
@dataclass
class SCTX000(ABC):
    pass    
@dataclass
class SCTXnil(SCTX000):
    pass    
@dataclass
class SCTXcons(SCTX000):
    arg1: dvar
    arg2: styp
    arg3: xtctx
    pass    
##################################################################

type stypopt = styp|None

##################################################################

STint = STbas("sint")
STbtf = STbas("bool")
STstr = STbas("strn")

##################################################################

def \
xtctx_search\
(xts: xtctx, dx0: dvar) -> styp:
    while True:
        if isinstance(xts, SCTXnil):
            return ST000()
        if isinstance(xts, SCTXcons):
            if dx0 == xts.arg1:
                return xts.arg2
            else:
                xts = xts.arg3; continue
        raise TypeError(xts) # HX-2026-06-02: should be deadcode!

##################################################################

# def dexp_eval000(dex: dexp):
#    return dexp_evalenv(dex, ENVnil())
def \
dexp_oftp000(dex: dexp) -> styp:
    return dexp_oftpctx(dex, SCTXnil())

# def \
# dexp_evalenv(dex: dexp, env0: xvenv) -> dval:
def \
dexp_oftpctx(dex: dexp, ctx0: xtctx) -> styp:
    if isinstance(dex, DEint):
        return STint
    if isinstance(dex, DEbtf):
        return STbtf
    if isinstance(dex, DEstr):
        return STstr
    if isinstance(dex, DEvar):
        return \
            xtctx_search(ctx0, dex.arg1)
    if isinstance(dex, DEapp):
        # DEapp(e1, e2)
        dex1 = dex.arg1
        dex2 = dex.arg2
        tex1 = dexp_oftpctx(dex1, ctx0)
        tex2 = dexp_oftpctx(dex2, ctx0)
        assert isinstance(tex1, STfun)
        assert (tex1.arg1 == tex2)
        return tex1.arg2
    if isinstance(dex, DEop2):
        opnm = dex.arg1
        dex1 = dex.arg2
        dex2 = dex.arg3
        tex1 = dexp_oftpctx(dex1, ctx0)
        tex2 = dexp_oftpctx(dex2, ctx0)
        return dop2_oftp(opnm, tex1, tex2)
    if isinstance(dex, DEif0):
        cond = dex.arg1
        tcnd = dexp_oftpctx(cond, ctx0)
        assert tcnd == STbtf
        tthn = dexp_oftpctx(dex.arg2, ctx0)
        tels = dexp_oftpctx(dex.arg3, ctx0)
        assert tthn == tels
        return tthn
    if isinstance(dex, DElam1):
        # DElam1(x1, T1, e2)
        xarg = dex.arg1
        targ = dex.arg2
        body = dex.arg3
        ctx1 = SCTXcons(xarg, targ, ctx0)
        tres = dexp_oftpctx(body, ctx1)
        return STfun(targ, tres)
    if isinstance(dex, DEfix1):
        # DEfix1(f0, x1, T1, T2, e2)
        farg = dex.arg1
        xarg = dex.arg2
        targ = dex.arg3
        tres = dex.arg4
        tfun = STfun(targ, tres)
        body = dex.arg5
        ctx1 = SCTXcons(farg, tfun, ctx0)
        ctx2 = SCTXcons(xarg, targ, ctx1)
        trs2 = dexp_oftpctx(body, ctx2)
        assert tres == trs2
        return tfun
    raise TypeError(dex) # HX-2026-06-15: dexp_oftpctx(...)

##################################################################

def dop2_oftp\
(opnm: strn, tex1: styp, tex2: styp) -> styp:
    # print("dop2_oftp: opnm = ", opnm)
    # print("dop2_oftp: tex1 = ", tex1)
    # print("dop2_oftp: tex2 = ", tex2)
    if (opnm == "+"):
        assert (tex1 == STint)
        assert (tex2 == STint)
        return STint
    if (opnm == "-"):
        assert (tex1 == STint)
        assert (tex2 == STint)
        return STint
    if (opnm == "*"):
        assert (tex1 == STint)
        assert (tex2 == STint)
        return STint
    if (opnm == "%"):
        assert (tex1 == STint)
        assert (tex2 == STint)
        return STint
    if (opnm == "/"):
        assert (tex1 == STint)
        assert (tex2 == STint)
        return STint
    if (opnm == "<"):
        assert (tex1 == STint)
        assert (tex2 == STint)
        return STbtf
    if (opnm == ">"):
        assert (tex1 == STint)
        assert (tex2 == STint)
        return STbtf
    if (opnm == "<="):
        assert (tex1 == STint)
        assert (tex2 == STint)
        return STbtf
    if (opnm == ">="):
        assert (tex1 == STint)
        assert (tex2 == STint)
        return STbtf
    if (opnm == "=="):
        assert (tex1 == STint)
        assert (tex2 == STint)
        return STbtf
    if (opnm == "!="):
        assert (tex1 == STint)
        assert (tex2 == STint)
        return STbtf
    raise TypeError(opnm) # HX-2026-06-09: dop2_oftp(...)

##################################################################
##################################################################
# end of [CS391-2026-Summer/lectures/lecture-06-09/lambda5.py]
##################################################################
##################################################################
