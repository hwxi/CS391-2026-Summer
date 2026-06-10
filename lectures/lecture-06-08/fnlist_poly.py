##################################################################
#
# HX-2026-06-08:
# Code for
# demonstrating polymorphic functional lists
#
##################################################################
from typing import \
    Generic, TypeVar, Callable
from dataclasses import dataclass
##################################################################
T = TypeVar("T")
X = TypeVar("X")
Y = TypeVar("Y")
##################################################################
@dataclass
class fnlist[T]:
    pass
@dataclass
class fnlist_nil(fnlist[T]):
    pass
@dataclass
class fnlist_cons(fnlist[T]):
    arg1: T
    arg2: fnlist[T]
    pass
##################################################################
def fnlist_hd(xs: fnlist[T]) -> T:
    assert isinstance(xs, fnlist_cons)
    return xs.arg1
def fnlist_tl(xs: fnlist[T]) -> fnlist[T]:
    assert isinstance(xs, fnlist_cons)
    return xs.arg2
##################################################################
def \
fnlist_forall\
(xs: fnlist[T], test: Callable[[T], bool]) -> bool:
    while isinstance(xs, fnlist_cons):
        x1 = xs.arg1
        if test(x1):
            xs = xs.arg2
            continue
        else:
            return False
    return True
##################################################################
def \
fnlist_foritm\
(xs: fnlist[T], work: Callable[[T], None]) -> None:
    while isinstance(xs, fnlist_cons):
        x1 = xs.arg1
        work(x1)
        xs = xs.arg2
    return None
##################################################################
def \
fnlist_range1(n: int) -> fnlist[int]:
    res: fnlist[int]
    res = fnlist_nil()
    for i in range(n):
        res = fnlist_cons(n-1-i, res)
    return res
##################################################################
def \
fnlist_reverse\
(xs: fnlist[T]) -> fnlist[T]:
    res: fnlist[T]
    res = fnlist_nil()
    while isinstance(xs, fnlist_cons):
        x0 = xs.arg1
        xs = xs.arg2
        res = fnlist_cons(x0, res)
    return res
##################################################################
#
def fnlist_map\
(xs: fnlist[X], \
 fopr: Callable[[X], Y]) -> fnlist[Y]:
    return fnlist_reverse(fnlist_maprev(xs, fopr))
#
def fnlist_maprev\
(xs: fnlist[X], \
 fopr: Callable[[X], Y]) -> fnlist[Y]:
    res: fnlist[Y]
    res = fnlist_nil()
    while isinstance(xs, fnlist_cons):
        x0 = xs.arg1
        xs = xs.arg2
        res = fnlist_cons(fopr(x0), res)
    return res
#
##################################################################
xs1 = fnlist_range1(10)
xs2 = fnlist_map(xs1, lambda x1: x1*x1)
fnlist_foritm(xs1, lambda x1: print(x1))
fnlist_foritm(xs2, lambda x1: print(x1))
##################################################################
