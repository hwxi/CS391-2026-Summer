############################################################
# datatype term =
# | TMvar of strn(*name*) // name
# | TMlam of (strn, term) // abstraction
# | TMapp of (term, term) // application
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

############################################################

tvar_x = term_var("x")
tvar_y = term_var("y")
tvar_z = term_var("z")
tvar_f = term_var("f")
tvar_n = term_var("n")

term_I = term_lam("x", tvar_x) # lambda x. x

_ = print("term_I =", term_I)

term_K = term_lam("x", term_lam("y", tvar_x)) # lambda x. lambda y. x

_ = print("term_K =", term_K)

term_K1 = term_lam("x", term_lam("y", tvar_y)) # lambda x. lambda y. y

_ = print("term_K1 =", term_K1)

term_S = term_lam("x", term_lam("y", term_lam("z", term_app(term_app(tvar_x, tvar_z), term_app(tvar_y, tvar_z))))) # lambda x. lambda y. lambda z. (x(z))(y(z))

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

def term_size(tm0):
    ctag = tm0.ctag
    if (ctag == "TMvar"):
        return 1
    if (ctag == "TMlam"):
        return 1 + term_size(tm0.arg2)
    if (ctag == "TMapp"):
        return 1 + term_size(tm0.arg1) + term_size(tm0.arg2)
    # assert False, "term_size: DEADCODE!!!"
    raise TypeError(tm0) # HX-2026-05-20: should be deadcode!

############################################################

_ = print("term_size(x) =", term_size(tvar_x))
_ = print("term_size(I) =", term_size(term_I))
_ = print("term_size(K) =", term_size(term_K))
_ = print("term_size(S) =", term_size(term_S))

############################################################

def term_subst0(tm0, tx0, sub):
    def subst0(tm0):
        return term_subst0(tm0, tx0, sub)
    """
    term_subst0(tm0, tx0, sub) = tm0[tx0 -> sub]
    Please notice that 'sub' is ASSUMED to be a closed
    lambda-term. Hence, 'term_subst0' does not need to handling
    the issue of free variable capturing
    """
    ctag = tm0.ctag
    if (ctag == "TMvar"):
        tx1 = tm0.arg1
        if (tx0 == tx1):
            return sub
        else:
            return tm0
    if (ctag == "TMlam"):
        tx1 = tm0.arg1 # lambda-var
        tm1 = tm0.arg2 # lambda-body
        if (tx0 == tx1):
            return tm0 # no free 'tx1' in 'tm0'!!!
        else:
            return term_lam(tx1, subst0(tm1))
    if (ctag == "TMapp"):
        tm1 = tm0.arg1
        tm2 = tm0.arg2
        return term_app(subst0(tm1), subst0(tm2))
    # assert False, "term_subst0: DEADCODE!!!"
    raise TypeError(tm0) # HX-2026-05-20: should be deadcode!

_ = print("x[y -> I] =", term_subst0(tvar_x, "y", term_I))
_ = print("x[x -> I] =", term_subst0(tvar_x, "x", term_I))
_ = print("I[x -> I] =", term_subst0(term_I, "x", term_I))
_ = print("(x(y))[y -> I] =", term_subst0(term_app(tvar_x, tvar_y), "y", term_I))
_ = print("(y(x))[y -> I] =", term_subst0(term_app(tvar_x, tvar_y), "x", term_I))
_ = print("(lam x.y)[y -> I] =", term_subst0(term_lam("x", tvar_y), "y", term_I))

############################################################

def term_cbn_interp(tm0):
    """
    HX: Call-by-name interpreter
    """
    # print("term_cbn_interp: tm0 = ", tm0)
    ctag = tm0.ctag
    if (ctag == "TMvar"):
        return tm0
    if (ctag == "TMlam"):
        return tm0
    if (ctag == "TMapp"):
        # tm0 = TMapp(tm1, tm2)
        tm1 = tm0.arg1
        tm1 = term_cbn_interp(tm1)
        tm2 = tm0.arg2
        ctg1 = tm1.ctag
        if (ctg1 == "TMlam"):
            # tm1 = TMlam(tm1_x, tm1_t)
            # tm0 = TMapp(TMlam(tm1_x, tm1_t), tm2)
            tm1_x = tm1.arg1
            tm1_t = tm1.arg2
            tm0 = term_subst0(tm1_t, tm1_x, tm2)
            return term_cbn_interp(tm0)
        # print("TypeError: non-function!")
        raise TypeError(tm1) # HX: TypeError: non-function
    raise TypeError(tm0) # HX-2026-05-27: should be deadcode!

term_SKK = term_app(term_app(term_S, term_K), term_K)

_ = print("interp(SKKx) = ", term_cbn_interp(term_app(term_SKK, tvar_x)))

############################################################
############################################################
