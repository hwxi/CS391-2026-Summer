############################################################
# datatype term =
# | TMvar of strn(*name*)
# | TMlam of (strn, term)
# | TMapp of (term, term)
############################################################
#
# HX-2026-05-20:
# These are really dataclasses
#
############################################################

class term:
    ctag = ""
    def __str__(self):
        return ("term(" + self.ctag + ")")
# end-of-class(term)

class term_var(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TMvar"
    def __str__(self):
        return ("TMvar(" + self.arg1 + ")")
# end-of-class(term_var(term))

class term_lam(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TMlam"
    def __str__(self):
        return ("TMlam(" + self.arg1 + "," + str(self.arg2) + ")")
# end-of-class(term_lam(term))

class term_app(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TMapp"
    def __str__(self):
        return ("TMapp(" + str(self.arg1) + "," + str(self.arg2) + ")")
# end-of-class(term_app(term))

var_x = term_var("x")
var_y = term_var("y")
var_z = term_var("z")
var_xyz = term_var("xyz")

_ = print("var_xyz =", var_xyz)

term_I = term_lam("x", var_x) # lambda x. x

_ = print("term_I =", term_I)

term_K = term_lam("x", term_lam("y", var_x)) # lambda x. lambda y. x

_ = print("term_K =", term_K)

term_K1 = term_lam("x", term_lam("y", var_y)) # lambda x. lambda y. y

_ = print("term_K1 =", term_K1)

term_S = term_lam("x", term_lam("y", term_lam("z", term_app(term_app(var_x, var_z), term_app(var_y, var_z))))) # lambda x. lambda y. lambda z. (x(z))(y(z))

_ = print("term_S =", term_S)

############################################################
# fun
# term_size
# (t0: term): sint =
# (
# case+ t0 of
# |
# TMvar(x0) => 1
# |
# TMlam(x0, t1) =>
# 1 + term_size(t1)
# |
# TMapp(t1, t2) =>
# (1+term_size(t1)+term_size(t2))
# )
############################################################

def term_size(t0):
    ctag = t0.ctag
    if (ctag == "TMvar"):
        return 1
    if (ctag == "TMlam"):
        return 1 + term_size(t0.arg2)
    if (ctag == "TMapp"):
        return 1 + term_size(t0.arg1) + term_size(t0.arg2)
    assert False, "term_size: DEADCODE!!!"

############################################################

_ = print("term_size(x) =", term_size(var_x))
_ = print("term_size(I) =", term_size(term_I))
_ = print("term_size(K) =", term_size(term_K))
_ = print("term_size(S) =", term_size(term_S))

############################################################

