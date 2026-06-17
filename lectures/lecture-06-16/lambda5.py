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
type stypopt = styp|None
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
class STxyz(ST000):
    uniq = 1
    arg1: sint
    arg2: stypopt
def STxyz_new():
    uniq = STxyz.uniq
    STxyz.uniq = uniq + 1
    return STxyz(uniq, None)
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
        raise TypeError(xts) # HX-2026-06-16: should be deadcode!

##################################################################

def styp_eval(tex: styp) -> styp:
    if isinstance(tex, STxyz):
        if tex.arg2 is None:
            return tex
        else:
            return styp_eval(tex.arg2)
    return tex

def \
styp_funiz(tex: styp) -> bool:
    tex = styp_eval(tex)
    if isinstance(tex, STfun):
        return True
    if isinstance(tex, STxyz):
        targ = STxyz_new()
        tres = STxyz_new()
        STxyz.arg2 = STfun(targ, tres)
        return True
    return False

def \
styp_tupiz(tex: styp) -> bool:
    tex = styp_eval(tex)
    if isinstance(tex, STtup):
        return True
    if isinstance(tex, STxyz):
        targ = STxyz_new()
        tres = STxyz_new()
        STxyz.arg2 = STtup(targ, tres)
        return True
    return False

def \
styp_check\
(tex1: STxyz, tex2: styp) -> bool:
    if isinstance(tex2, STbas):
        return False
    if isinstance(tex2, STxyz):
        # HX: tex1 and tex2 have the same stamp?
        return tex1.arg1 == tex2.arg1
    if isinstance(tex2, STfun):
        return styp_check(tex1, tex2.arg1) or styp_check(tex1, tex2.arg2)
    if isinstance(tex2, STtup):
        return styp_check(tex1, tex2.arg1) or styp_check(tex1, tex2.arg2)
    raise TypeError(tex2) # HX-2026-06-16: should be deadcode!

def \
styp_unify(tex1: styp, tex2: styp) -> bool:
    tex1 = styp_eval(tex1)
    tex2 = styp_eval(tex2)
    if isinstance(tex1, STxyz):
        if styp_check(tex1, tex2):
            if isinstance(tex2, STxyz):
                return True
            else:
                return False
        tex1.arg2 = tex2; return True
    if isinstance(tex2, STxyz):
        if styp_check(tex2, tex1):
            return False
        tex2.arg2 = tex1; return True
    if isinstance(tex1, STbas):
       if isinstance(tex2, STbas):
           return tex1.arg1 == tex2.arg1
       else:
           return False
    if isinstance(tex1, STfun):
       if isinstance(tex2, STfun):
           return styp_unify(tex1.arg1, tex2.arg1) and styp_unify(tex1.arg2, tex1.arg2)
       else:
           return False
    if isinstance(tex1, STtup):
       if isinstance(tex2, STtup):
           return styp_unify(tex1.arg1, tex2.arg1) and styp_unify(tex1.arg2, tex1.arg2)
       else:
           return False
    raise TypeError(tex1) # HX-2026-06-16: should be deadcode!

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
    if isinstance(dex, DElam):
        # DElam(x1, e2)
        xarg = dex.arg1
        body = dex.arg2
        targ = STxyz_new()
        ctx1 = SCTXcons(xarg, targ, ctx0)
        tres = dexp_oftpctx(body, ctx1)
        return STfun(targ, tres)
    if isinstance(dex, DEfix):
        # DElam(x1, e2)
        farg = dex.arg1
        xarg = dex.arg2
        body = dex.arg3
        targ = STxyz_new()
        tres = STxyz_new()
        tfun = STfun(targ, tres)
        ctx1 = SCTXcons(farg, tfun, ctx0)
        ctx2 = SCTXcons(xarg, targ, ctx1)
        trs2 = dexp_oftpctx(body, ctx2)
        assert styp_unify(tres, trs2)
        return tfun
    if isinstance(dex, DEapp):
        # DEapp(e1, e2)
        dex1 = dex.arg1
        dex2 = dex.arg2
        tex1 = dexp_oftpctx(dex1, ctx0)
        tex2 = dexp_oftpctx(dex2, ctx0)
        assert styp_funiz(tex1)
        assert isinstance(tex1, STfun)
        # print("dexp_oftpctx: DEapp: tex1 = ", tex1)
        # print("dexp_oftpctx: DEapp: tex2 = ", tex2)
        assert styp_unify(tex1.arg1, tex2)
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
        assert styp_unify(tcnd, STbtf)
        tthn = dexp_oftpctx(dex.arg2, ctx0)
        tels = dexp_oftpctx(dex.arg3, ctx0)
        assert styp_unify(tthn, tels)
        return tthn
    if isinstance(dex, DEtup):
        # DEtup(e1, e2)
        dex1 = dex.arg1
        dex2 = dex.arg2
        tex1 = dexp_oftpctx(dex1, ctx0)
        tex2 = dexp_oftpctx(dex2, ctx0)
        return STtup(tex1, tex2)
    if isinstance(dex, DEfst):
        # DEfst(e1, e2)
        dex1 = dex.arg1
        tex1 = dexp_oftpctx(dex1, ctx0)
        assert styp_tupiz(tex1)
        assert isinstance(tex1, STtup)
        return tex1.arg1
    if isinstance(dex, DEsnd):
        # DEfst(e1, e2)
        dex1 = dex.arg1
        tex1 = dexp_oftpctx(dex1, ctx0)
        assert styp_tupiz(tex1)
        assert isinstance(tex1, STtup)
        return tex1.arg2
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
        assert styp_unify(tres, trs2)
        return tfun
    raise TypeError(dex) # HX-2026-06-16: dexp_oftpctx(...)

##################################################################

def dop2_oftp\
(opnm: strn, tex1: styp, tex2: styp) -> styp:
    # print("dop2_oftp: opnm = ", opnm)
    # print("dop2_oftp: tex1 = ", tex1)
    # print("dop2_oftp: tex2 = ", tex2)
    if (opnm == "+"):
        assert styp_unify(tex1, STint)
        assert styp_unify(tex2, STint)
        return STint
    if (opnm == "-"):
        assert styp_unify(tex1, STint)
        assert styp_unify(tex2, STint)
        return STint
    if (opnm == "*"):
        assert styp_unify(tex1, STint)
        assert styp_unify(tex2, STint)
        return STint
    if (opnm == "%"):
        assert styp_unify(tex1, STint)
        assert styp_unify(tex2, STint)
        return STint
    if (opnm == "/"):
        assert styp_unify(tex1, STint)
        assert styp_unify(tex2, STint)
        return STint
    if (opnm == "<"):
        assert styp_unify(tex1, STint)
        assert styp_unify(tex2, STint)
        return STbtf
    if (opnm == ">"):
        assert styp_unify(tex1, STint)
        assert styp_unify(tex2, STint)
        return STbtf
    if (opnm == "<="):
        assert styp_unify(tex1, STint)
        assert styp_unify(tex2, STint)
        return STbtf
    if (opnm == ">="):
        assert styp_unify(tex1, STint)
        assert styp_unify(tex2, STint)
        return STbtf
    if (opnm == "=="):
        assert styp_unify(tex1, STint)
        assert styp_unify(tex2, STint)
        return STbtf
    if (opnm == "!="):
        assert styp_unify(tex1, STint)
        assert styp_unify(tex2, STint)
        return STbtf
    raise TypeError(opnm) # HX-2026-06-16: dop2_oftp(...)

##################################################################
##################################################################
# end of [CS391-2026-Summer/lectures/lecture-06-16/lambda5.py]
##################################################################
##################################################################
