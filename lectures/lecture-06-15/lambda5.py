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
class STbas(ST000):
    arg1: strn
    pass
class STxyz(ST000):
    arg1: styp
    pass
class STfun(ST000):
    arg1: styp
    arg2: styp
    pass
class STtup(ST000):
    arg1: styp
    arg2: styp
    pass
class STlist(ST000):
    arg1: styp
    pass
class STstrm(ST000):
    arg1: styp
    pass
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
    arg3: styp
    arg4: dexp
    arg5: styp
    pass
@dataclass
class DEanno(DE000):
    arg1: dexp
    arg2: styp
    pass
##################################################################
type xtenv = SCTX000
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
    arg2: treg
    arg3: xtenv
    pass    
##################################################################

def \
dexp_oftp000(dex: dexp): styp
    return dexp_oftpenv(dex, SCTXnil())

def \
dexp_oftpenv
(dex: dexp, sctx: xtctx): styp
    return dexp_oftpenv(dex, SCTXnil())

##################################################################
# end of [CS391-2026-Summer/lectures/lecture-06-09/lambda5.py]
##################################################################
##################################################################
