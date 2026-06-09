##################################################################
#
# HX-2026-06-08:
# Code for
# demonstrating lazy-evaluation
#
##################################################################

class stcn:
    ctag = ""
# end-of-class(strcon)

class stcn_nil(stcn):
    ctag = "nil"
    def __init__(self):
        return None
class stcn_cons(stcn):
    ctag = "cons"
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

# all the ints starting from [n0]
def ints_from(n0):
    return lambda: stcn_cons(n0, ints_from(n0+1))

# f_theNums = ints_from(0)
# c_theNums = f_theNums( )
# _ = print("n1 = ", c_theNums.arg1)
# f_theNums = c_theNums.arg2
# c_theNums = f_theNums( )
# _ = print("n2 = ", c_theNums.arg1)
# f_theNums = c_theNums.arg2
# c_theNums = f_theNums( )
# _ = print("n3 = ", c_theNums.arg1)

def strm_filter(fxs, test):
    def helper(fxs):
        while(True):
            cxs = fxs()
            if cxs.ctag == "nil":
                return stcn_nil()
            else:
                cx1 = cxs.arg1
                fxs = cxs.arg2
                if test(cx1):
                    return stcn_cons(cx1, lambda: helper(fxs))
                else:
                    continue
            # end-of-(if(cxs.ctag==0)-then-else)
    return lambda: helper(fxs)

def sieve(fxs):
    def helper(fxs):
        cxs = fxs()
        cx1 = cxs.arg1
        return stcn_cons(cxs.arg1, sieve(strm_filter(cxs.arg2, lambda cx2: cx2 % cx1 != 0)))
    return lambda: helper(fxs)

thePrimes = sieve(ints_from(2))

f_theNums = thePrimes
c_theNums = f_theNums( )
_ = print("p1(2) = ", c_theNums.arg1)
f_theNums = c_theNums.arg2
c_theNums = f_theNums( )
_ = print("p2(3) = ", c_theNums.arg1)
f_theNums = c_theNums.arg2
c_theNums = f_theNums( )
_ = print("p3(5) = ", c_theNums.arg1)
f_theNums = c_theNums.arg2
c_theNums = f_theNums( )
_ = print("p4(7) = ", c_theNums.arg1)
f_theNums = c_theNums.arg2
c_theNums = f_theNums( )
_ = print("p5(11) = ", c_theNums.arg1)
f_theNums = c_theNums.arg2
c_theNums = f_theNums( )
_ = print("p6(13) = ", c_theNums.arg1)
f_theNums = c_theNums.arg2
c_theNums = f_theNums( )
_ = print("p7(17) = ", c_theNums.arg1)

##################################################################
## end of [stream.py]
##################################################################
