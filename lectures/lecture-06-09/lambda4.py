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
# datatype tcmp =
# | TCMP of (list(tins), treg(*res*))
@dataclass
class dcmp(ABC):
    dres: dval
    inss: list(tins)
##################################################################
# end of [CS391-2026-Summer/lectures/lecture-06-09/lambda4.py]
##################################################################
