##################################################################
#
# HX-2026-06-08:
# Code for
# demonstrating functional lists
#
##################################################################

class fnlist:
    ctag = ""
class fnlist_nil(fnlist):
    ctag = "nil"
    def __init__(self):
        return None
class fnlist_cons(fnlist):
    ctag = "cons"
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

def fnlist_nilq(xs):
    return (xs.ctag == "nil")
def fnlist_head(xs):
    assert (xs.ctag == "cons")
    return xs.arg1
def fnlist_tail(xs):
    assert (xs.ctag == "cons")
    return xs.arg2

def fnlist_print(xs):
    nx = 0
    sep = "; "
    print("[",end='')
    while(xs.ctag == "cons"):
        if (nx > 0):
            print(sep,end='')        
        print(xs.arg1,end='')
        nx = nx + 1; xs = xs.arg2
    print("]", end='')
# end-of-[fnlist_print]

def fnlist_forall(xs, test):
    while(xs.ctag == "cons"):
        x0 = xs.arg1
        xs = xs.arg2
        if test(x0):
            continue
        else:
            return False
    return True

def fnlist_foreach(xs, work):
    while(xs.ctag == "cons"):
        x0 = xs.arg1
        xs = xs.arg2
        work(x0)
    return None

def fnlist_range1(n):
    res = fnlist_nil()
    for i in range(n):
        res = fnlist_cons(n-1-i, res)
    return res

def fnlist_reverse(xs):
    return fnlist_maprev(xs, lambda x: x)
    
def fnlist_maprev(xs, fopr):
    res = fnlist_nil()
    while(xs.ctag == "cons"):
        x0 = xs.arg1
        xs = xs.arg2
        res = fnlist_cons(fopr(x0), res)
    return res

def fnlist_map(xs, fopr):
    return fnlist_reverse(fnlist_maprev(xs, fopr))

xs1 = fnlist_range1(10)
xs2 = fnlist_map(xs1, lambda x: x * x)
# xs2 = fnlist_maprev(xs1, lambda x: x * x)
___ = print("xs1:"); fnlist_print(xs1); print()
___ = print("xs2:"); fnlist_print(xs2); print()

