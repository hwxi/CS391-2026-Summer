##################################################################
#
# HX: let's use dataclasses
# HX: let's do type-checking
# Tue Jun  9 05:28:30 PM EDT 2026
#
##################################################################
type sint = int
type strn = str
##################################################################
from lambda3 import *
##################################################################
from abc import ABC
from enum import Enum
from dataclasses import dataclass
##################################################################
@dataclass
class treg(ABC):
    the_narg = 0
    the_ntmp = 100
    the_nfun = 100
    prfx: strn
    sffx: sint
    pass
def targ_new():
    treg.the_narg += 1
    return treg("arg", treg.the_narg)
def ttmp_new():
    treg.the_ntmp += 1
    return treg("tmp", treg.the_ntmp)
def tfun_new():
    treg.the_nfun += 1
    return treg("fun", treg.the_nfun)
##################################################################
# myarg0 = targ_new()
# mytmp1 = ttmp_new()
# mytmp2 = ttmp_new()
# myfun1 = tfun_new()
# myfun2 = tfun_new()
# print("myarg0 = " + repr(myarg0))
# print("mytmp1 = " + repr(mytmp1))
# print("mytmp2 = " + repr(mytmp2))
# print("myfun1 = " + repr(myfun1))
# print("myfun2 = " + repr(myfun2))
##################################################################
#
type dval = DVL000 \
    | DVLint | DVLbtf \
    | DVLstr | DVLreg \
#
# datatype dval =
# | DVint of sint | DVbtf of bool
# | DVstr of strn | DVreg of treg
#
@dataclass
class DVL000(ABC):
    pass
@dataclass
class DVLint(ABC):
    arg1: sint
    pass
@dataclass
class DVLbtf(ABC):
    arg1: bool
    pass
@dataclass
class DVLstr(ABC):
    arg1: strn
    pass
@dataclass
class DVLreg(ABC):
    arg1: treg
    pass
##################################################################
#
# datatype dins =
# | INSmov of (treg(*dst*), tval(*src*))
# | INSapp of (treg(*res*), treg(*fun*), treg(*arg*))
# | INSop1 of (treg(*res*), strn(*opr*), treg(*arg*))
# | INSop2 of (treg(*res*), strn(*opr*), treg(*ag1*), treg(*ag2*))
# | INSfun of (treg(*f00*), treg(*x01*), dcmp(*body*))
# | INSif0 of (treg(*res*), treg(*test*), dcmp(*then*), dcmp(*else*))
#
type dins = INS000 \
    | INSmov | INSapp \
    | INSop1 | INSop2 \
    | INSfun | INSif0
@dataclass
class INS000(ABC):
    pass
# | INSmov of (treg(*dst*), tval(*src*))
@dataclass
class INSmov(ABC):
    arg1: treg
    arg2: dval
    pass
# | INSapp of (treg(*res*), treg(*fun*), treg(*arg*))
@dataclass
class INSapp(ABC):
    arg1: treg
    arg2: treg
    arg3: treg
    pass
# | INSop1 of (treg(*res*), strn(*opr*), treg(*arg*))
@dataclass
class INSop1(ABC):
    arg1: treg
    arg2: strn
    arg3: treg
    pass
# | INSop2 of (treg(*res*), strn(*opr*), treg(*ag1*), treg(*ag2*))
@dataclass
class INSop2(ABC):
    arg1: treg
    arg2: strn
    arg3: treg
    arg4: treg
    pass
# | INSfun of (treg(*f00*), treg(*x01*), dcmp(*body*))
@dataclass
class INSfun(ABC):
    arg1: treg
    arg2: treg
    arg3: dcmp
    pass
# | INSif0 of (treg(*res*), treg(*test*), dcmp(*then*), dcmp(*else*))
@dataclass
class INSif0(ABC):
    arg1: treg
    arg2: treg
    arg3: dcmp
    arg4: dcmp
    pass
##################################################################
# datatype dcmp =
# | DCMP of (list(tins), treg(*res*))
@dataclass
class dcmp(ABC):
    dres: treg
    inss: list[dins]
##################################################################
type xtenv = CENV000 | CENVnil | CENVcons
@dataclass
class CENV000(ABC):
    pass    
@dataclass
class CENVnil(CENV000):
    pass    
@dataclass
class CENVcons(CENV000):
    arg1: dvar
    arg2: treg
    arg3: xtenv
    pass    
##################################################################

def \
xtenv_search\
(xts: xtenv, dx0: dvar) -> treg:
    while True:
        if isinstance(xts, CENVnil):
            raise ValueError()
        if isinstance(xts, CENVcons):
            if dx0 == xts.arg1:
                return xts.arg2
            else:
                xts = xts.arg3; continue
        raise TypeError(xts) # HX-2026-06-09: should be deadcode!    

##################################################################

def \
dexp_comp000(dex: dexp) -> dcmp:
    return dexp_compenv(dex, CENVnil())

def \
dexp_compenv\
(dex: dexp, cenv: xtenv) -> dcmp:
    dvl0: dval
    ins0: dins
    if isinstance(dex, DEint):
        ttmp = ttmp_new()
        dvl0 = DVLint(dex.arg1)
        ins0 = INSmov(ttmp, dvl0)
        return dcmp(ttmp, [ins0])
    if isinstance(dex, DEbtf):
        ttmp = ttmp_new()
        dvl0 = DVLbtf(dex.arg1)
        ins0 = INSmov(ttmp, dvl0)
        return dcmp(ttmp, [ins0])
    if isinstance(dex, DEstr):
        ttmp = ttmp_new()
        dvl0 = DVLstr(dex.arg1)
        ins0 = INSmov(ttmp, dvl0)
        return dcmp(ttmp, [ins0])
    if isinstance(dex, DElam):
        dx0 = dex.arg1
        tfun = tfun_new()
        targ = targ_new()
        cenv = CENVcons(dx0, targ, cenv)
        cmp1 = dexp_compenv(dex.arg2, cenv)
        ins0 = INSfun(tfun, targ, cmp1)
        return dcmp(dres=tfun, inss=[ins0])
    if isinstance(dex, DEfix):
        df0 = dex.arg1
        dx0 = dex.arg2
        tfun = tfun_new()
        targ = targ_new()
        cenv = CENVcons(df0, tfun, cenv)
        cenv = CENVcons(dx0, targ, cenv)
        cmp1 = dexp_compenv(dex.arg3, cenv)
        ins0 = INSfun(tfun, targ, cmp1)
        return dcmp(dres=tfun, inss=[ins0])
    if isinstance(dex, DEapp):
        cmp1 = dexp_compenv(dex.arg1, cenv)
        cmp2 = dexp_compenv(dex.arg2, cenv)
        tmp1 = cmp1.dres
        ins1 = cmp1.inss
        tmp2 = cmp2.dres
        ins2 = cmp2.inss
        ttmp = ttmp_new()
        ins0 = INSapp(ttmp, tmp1, tmp2)
        inss = ins1 + ins2 + [ins0]
        return dcmp(dres=ttmp, inss=inss)
    if isinstance(dex, DEif0):
        cmp1 = dexp_compenv(dex.arg1, cenv) # test
        cmp2 = dexp_compenv(dex.arg2, cenv) # then
        cmp3 = dexp_compenv(dex.arg3, cenv) # else
        tmp1 = cmp1.dres
        ins1 = cmp1.inss
        ttmp = ttmp_new()
        ins0 = INSif0(ttmp, tmp1, cmp2, cmp3)
        inss = ins1 + [ins0]
        return dcmp(dres=ttmp, inss=inss)
    if isinstance(dex, DEop1):
        pnm = dex.arg1
        ag1 = dex.arg2
        cmp1 = dexp_compenv(ag1, cenv)
        tmp1 = cmp1.dres
        ins1 = cmp1.inss
        ttmp = ttmp_new()
        ins0 = INSop1(ttmp, pnm, tmp1)
        inss = ins1 + ins2 + [ins0]
        return dcmp(dres=ttmp, inss=inss)
    if isinstance(dex, DEop2):
        pnm = dex.arg1
        ag1 = dex.arg2
        ag2 = dex.arg3
        cmp1 = dexp_compenv(ag1, cenv)
        cmp2 = dexp_compenv(ag2, cenv)
        tmp1 = cmp1.dres
        ins1 = cmp1.inss
        tmp2 = cmp2.dres
        ins2 = cmp2.inss
        ttmp = ttmp_new()
        ins0 = INSop2(ttmp, pnm, tmp1, tmp2)
        inss = ins1 + ins2 + [ins0]
        return dcmp(dres=ttmp, inss=inss)
    raise ValueError("dexp_compenv: " + repr(dex))

##################################################################
# end of [CS391-2026-Summer/lectures/lecture-06-09/lambda4.py]
##################################################################
