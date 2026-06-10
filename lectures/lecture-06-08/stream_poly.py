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
type strm[T] = \
Callable[[], stcn[T]]
@dataclass
class stcn[T]:
    pass
@dataclass
class stcn_nil(stcn[T]):
    pass
@dataclass
class stcn_cons(stcn[T]):
    arg1: T
    arg2: strm[T]
##################################################################
# all the ints starting from [n0]
def ints_from(n0: int) -> strm[int]:
    return lambda: stcn_cons(n0, ints_from(n0+1))
##################################################################
def strm_filter\
(fxs: strm[T], test: Callable[[T], bool]) -> strm[T]:
    def helper(fxs: strm[T]) -> stcn[T]:
        while(True):
            cxs = fxs()
            if isinstance(cxs, stcn_cons):
                cx1 = cxs.arg1
                fxs = cxs.arg2
                if test(cx1):
                    return stcn_cons(cx1, lambda: helper(fxs))
                else:
                    continue
            else:
                return stcn_nil()
    return lambda: helper(fxs)
##################################################################
def sieve(fxs: strm[int]) -> strm[int]:
    def helper(fxs: strm[int]) -> stcn[int]:
        cxs = fxs()
        assert isinstance(cxs, stcn_cons)
        cx1 = cxs.arg1
        return stcn_cons(cxs.arg1, sieve(strm_filter(cxs.arg2, lambda cx2: cx2 % cx1 != 0)))
    return lambda: helper(fxs)
##################################################################
def thePrimes_print(n: int) -> None:
    i = 0
    fxs = sieve(ints_from(2))
    while i <= n:
        i += 1
        cxs = fxs()
        assert isinstance(cxs, stcn_cons)
        cx1 = cxs.arg1
        fxs = cxs.arg2
        print("prime("+str(i)+") = " + str(cx1))
    return None
thePrimes_print(100)
##################################################################
