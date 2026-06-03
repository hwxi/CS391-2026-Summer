############################################################
# HX-2026-06-02:
# This is the LAMBDA language so far:
#
# datatype term =
#######
# Primitive data
# | TMint of sint
# | TMbtf of bool
#######
# Pure part of LC
# | TMvar of strn(*name*) // name
# | TMlam of (strn, term) // abstraction
# | TMapp of (term, term) // application
#######
# Primitive operations
# | TMop2 of (strn(*name*), term(*arg1*), term(*arg2))
#######
# For if-then-else experssions
# | TMifb of (term(*cond*), term(*then*), term(*else*))
#######
# For recursion via fixed-point
# | TMfix of (strn(*f*), strn(*x*), term) // fixed-point
#######
# For pairs
# | TMprj1 of (term) // 1st projection
# | TMprj2 of (term) // 2nd projection
# | TMpair of (term(*1st*), term(*snd*))
#######
#
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

class term_int(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TMint"
    def __str__(self):
        return ("TMint(" + str(self.arg1) + ")")
# end-of-class(term_int(term))

class term_btf(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TMbtf"
    def __str__(self):
        return ("TMbtf(" + str(self.arg1) + ")")
# end-of-class(term_btf(term))

class term_var(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TMvar"
    def __str__(self):
        return ("TMvar(" + str(self.arg1) + ")")
# end-of-class(term_var(term))

class term_lam(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TMlam"
    def __str__(self):
        return ("TMlam(" + self.arg1 + "," + str(self.arg2) + ")")
# end-of-class(term_lam(term))

class term_fix(term):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "TMfix"
    def __str__(self):
        return ("TMfix(" + self.arg1 + "," + self.arg2 + "," + str(self.arg3) + ")")
# end-of-class(term_fix(term))

class term_app(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TMapp"
    def __str__(self):
        return ("TMapp(" + str(self.arg1) + "," + str(self.arg2) + ")")
# end-of-class(term_app(term))

class term_op2(term):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "TMop2"
    def __str__(self):
        return ("TMop2(" + str(self.arg1) + "," + str(self.arg2) + "," + str(self.arg3) + ")")
# end-of-class(term_op2(term))

class term_ifb(term):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "TMifb"
    def __str__(self):
        return ("TMifb(" + str(self.arg1) + "," + str(self.arg2) + "," + str(self.arg3) + ")")
# end-of-class(term_ifb(term))

############################################################

tint_0 = term_int(0)
tint_1 = term_int(1)
tint_2 = term_int(2)
_ = print("tint_2 =", tint_2)

tbtf_t = term_btf(True)
tbtf_f = term_btf(False)
_ = print("tbtf_t =", tbtf_t)

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

term_add12 = term_op2("+", tint_1, tint_2)
term_sub12 = term_op2("-", tint_1, tint_2)
term_mul12 = term_op2("*", tint_1, tint_2)

_ = print("term_mul12 =", term_mul12)

term_cond1 = term_ifb(tbtf_t, tint_1, tint_2)
term_cond2 = term_ifb(tbtf_f, tint_1, tint_2)

_ = print("term_cond1 =", term_cond1)
_ = print("term_cond2 =", term_cond2)

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
    if (ctag == "TMint"):
        return 1
    if (ctag == "TMbtf"):
        return 1
    if (ctag == "TMvar"):
        return 1
    if (ctag == "TMlam"):
        return 1 + term_size(tm0.arg2)
    if (ctag == "TMfix"):
        return 1 + term_size(tm0.arg3)
    if (ctag == "TMapp"):
        return 1 + term_size(tm0.arg1) + term_size(tm0.arg2)
    if (ctag == "TMop2"):
        return 1 + term_size(tm0.arg1) + term_size(tm0.arg2)
    if (ctag == "TMifb"):
        return 1 + term_size(tm0.arg1) + term_size(tm0.arg2) + term_size(tm0.arg3)
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
    if (ctag == "TMint"):
        return tm0
    if (ctag == "TMbtf"):
        return tm0
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
    if (ctag == "TMfix"):
        tf1 = tm0.arg1 # fixpnt-fun
        tx1 = tm0.arg2 # fixpnt-arg
        tm1 = tm0.arg3 # fixpnt-body
        if (tx0 == tf1):
            return tm0 # no free 'tx0' in 'tm0'!!!
        if (tx0 == tx1):
            return tm0 # no free 'tx0' in 'tm0'!!!
        else:
            return term_fix(tf1, tx1, subst0(tm1))
    if (ctag == "TMapp"):
        tm1 = tm0.arg1
        tm2 = tm0.arg2
        return term_app(subst0(tm1), subst0(tm2))
    if (ctag == "TMop2"):
        nm1 = tm0.arg1
        tm2 = tm0.arg2
        tm3 = tm0.arg3
        return term_op2(nm1, subst0(tm2), subst0(tm3))
    if (ctag == "TMifb"):
        tm1 = tm0.arg1
        tm2 = tm0.arg2
        tm3 = tm0.arg3
        return term_ifb(subst0(tm1), subst0(tm2), subst0(tm3))
    # assert False, "term_subst0: DEADCODE!!!"
    raise TypeError(tm0) # HX-2026-05-20: should be deadcode!

_ = print("x[y -> I] =", term_subst0(tvar_x, "y", term_I))
_ = print("x[x -> I] =", term_subst0(tvar_x, "x", term_I))
_ = print("I[x -> I] =", term_subst0(term_I, "x", term_I))
_ = print("(x(y))[y -> I] =", term_subst0(term_app(tvar_x, tvar_y), "y", term_I))
_ = print("(y(x))[y -> I] =", term_subst0(term_app(tvar_x, tvar_y), "x", term_I))
_ = print("(lam x.y)[y -> I] =", term_subst0(term_lam("x", tvar_y), "y", term_I))

############################################################

def term_interp(tm0):
    """
    HX: Call-by-value interpreter
    """
    # print("term_interp: tm0 = ", tm0)
    ctag = tm0.ctag
    if (ctag == "TMint"):
        return tm0
    if (ctag == "TMbtf"):
        return tm0
    if (ctag == "TMvar"):
        return tm0
    if (ctag == "TMlam"):
        return tm0
    if (ctag == "TMfix"):
        return tm0
    if (ctag == "TMapp"):
        # tm0 = TMapp(tm1, tm2)
        tm1 = tm0.arg1
        tm2 = tm0.arg2
        tm1 = term_interp(tm1)
        tm2 = term_interp(tm2)
        ctg1 = tm1.ctag
        if (ctg1 == "TMlam"):
            # tm1 = TMlam(tm1_x, tm1_t)
            # tm0 = TMapp(TMlam(tm1_x, tm1_t), tm2)
            tm1_x = tm1.arg1
            tm1_t = tm1.arg2
            tm1_t = term_subst0(tm1_t, tm1_x, tm2)
            return term_interp(tm1_t)
        if (ctg1 == "TMfix"):
            # tm1 = TMfix(tm1_f, tm1_x, tm1_t)
            # tm0 = TMapp(TMfix(tm1_f, tm1_x, tm1_t), tm2)
            tm1_f = tm1.arg1
            tm1_x = tm1.arg2
            tm1_t = tm1.arg3
            tm1_t = term_subst0(tm1_t, tm1_f, tm1)
            tm1_t = term_subst0(tm1_t, tm1_x, tm2)
            return term_interp(tm1_t)
        # print("TypeError: non-function!")
        raise TypeError(tm1) # HX: TypeError: non-function
    if (ctag == "TMop2"):
        # tm0 = TMop2(tm1, tm2, tm3)
        nm1 = tm0.arg1
        tm2 = term_interp(tm0.arg2)
        tm3 = term_interp(tm0.arg3)
        if (nm1 == "+"):
            assert tm2.ctag == "TMint"
            assert tm3.ctag == "TMint"
            return term_int(tm2.arg1 + tm3.arg1)
        if (nm1 == "-"):
            assert tm2.ctag == "TMint"
            assert tm3.ctag == "TMint"
            return term_int(tm2.arg1 - tm3.arg1)
        if (nm1 == "*"):
            assert tm2.ctag == "TMint"
            assert tm3.ctag == "TMint"
            return term_int(tm2.arg1 * tm3.arg1)
        if (nm1 == ">"):
            assert tm2.ctag == "TMint"
            assert tm3.ctag == "TMint"
            return term_btf(tm2.arg1 > tm3.arg1)
        if (nm1 == "<"):
            assert tm2.ctag == "TMint"
            assert tm3.ctag == "TMint"
            return term_btf(tm2.arg1 < tm3.arg1)
        if (nm1 == ">="):
            assert tm2.ctag == "TMint"
            assert tm3.ctag == "TMint"
            return term_btf(tm2.arg1 >= tm3.arg1)
        if (nm1 == "<="):
            assert tm2.ctag == "TMint"
            assert tm3.ctag == "TMint"
            return term_btf(tm2.arg1 <= tm3.arg1)
        if (nm1 == "=="):
            assert tm2.ctag == "TMint"
            assert tm3.ctag == "TMint"
            return term_btf(tm2.arg1 == tm3.arg1)
        if (nm1 == "!="):
            assert tm2.ctag == "TMint"
            assert tm3.ctag == "TMint"
            return term_btf(tm2.arg1 != tm3.arg1)
        raise TypeError(nm1) # HX: TypeError: non-supported
    if (ctag == "TMifb"):
        # tm0 = TMifb(tm1, tm2, tm3)
        tm1 = tm0.arg1
        tm1 = term_interp(tm1)
        ctg1 = tm1.ctag
        if (ctg1 == "TMbtf"):
            # tm1 = TMbtf(btf)
            if (tm1.arg1):
                return term_interp(tm0.arg2)
            else:
                return term_interp(tm0.arg3)
        # print("TypeError: non-boolean-cond!")
        raise TypeError(tm1) # HX: TypeError: non-boolean        
    raise TypeError(tm0) # HX-2026-05-27: should be deadcode!

# HX: SKK = I
term_SKK = term_app(term_app(term_S, term_K), term_K)

_ = print("interp(SKK(x)) = ", term_interp(term_app(term_SKK, tvar_x)))

_ = print("interp(term_add12) = ", term_interp(term_add12))

_ = print("interp(term_cond1) = ", term_interp(term_cond1))
_ = print("interp(term_cond2) = ", term_interp(term_cond2))

term_dbl = term_lam("x", term_op2("+", tvar_x, tvar_x))
term_sqr = term_lam("x", term_op2("*", tvar_x, tvar_x))

Church_num_0 = term_lam("f", term_lam("x", tvar_x))
Church_num_1 = term_lam("f", term_lam("x", term_app(tvar_f, tvar_x)))
Church_num_2 = term_lam("f", term_lam("x", term_app(tvar_f, term_app(tvar_f, tvar_x))))

myprog0 = term_app(term_sqr, term_int(5))
myprog1 = term_app(term_app(Church_num_2, term_sqr), term_int(5))

_ = print("interp(myprog0) = ", term_interp(myprog0))
_ = print("interp(myprog1) = ", term_interp(myprog1))

# Y = lam f.(lam x.f(x(x)))(lam x.f(x(x)))
# Yv = lam f.(lam x.lam y.(f(x(x)))y)(lam x.lam y.(f(x(x)))y)

term_f_xx = term_app(tvar_f, term_app(tvar_x, tvar_x))
_ = print("term_f_xx = ", term_f_xx)
term_f_xx_y = term_app(term_app(tvar_f, term_app(tvar_x, tvar_x)), tvar_y)
_ = print("term_f_xx_y = ", term_f_xx_y)
term_lamxy_f_xx_y = term_lam("x", term_lam("y", term_f_xx_y))
Yv = term_lam("f", term_app(term_lamxy_f_xx_y, term_lamxy_f_xx_y))
_ = print("Yv = ", Yv)

#
# fact(n) = if n <= 0 then 1 else n * fact(n-1)
# fact = lam n. if n <= 0 then 1 else n * fact(n-1)
# fact = (lam f.lam n. if n <= 0 then 1 else n * f(n-1))(fact)
# fact = Yv(lam f.lam n. if n <= 0 then 1 else n * f(n-1))
#

term_fact = \
term_app(Yv,
term_lam("f", term_lam("n",
  term_ifb(term_op2("<=", tvar_n, tint_0), tint_1,
    term_op2("*", tvar_n, term_app(tvar_f, term_op2("-", tvar_n, tint_1)))))))
_ = print("term_fact = ", term_fact)

_ = print("term_fact(0) = ", term_interp(term_app(term_fact, tint_0)))
_ = print("term_fact(1) = ", term_interp(term_app(term_fact, tint_1)))
_ = print("term_fact(2) = ", term_interp(term_app(term_fact, tint_2)))
_ = print("term_fact(3) = ", term_interp(term_app(term_fact, term_int(3))))
_ = print("term_fact(4) = ", term_interp(term_app(term_fact, term_int(4))))
_ = print("term_fact(5) = ", term_interp(term_app(term_fact, term_int(5))))
_ = print("term_fact(10) = ", term_interp(term_app(term_fact, term_int(10))))

############################################################

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34(9), 55(10), 
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-2)+fibo(n-1)

#
# fibo(n) = if n <= 1 then n else fibo(n-2)+fibo(n-1)
# fibo = lam n. if n <= 1 then n else fibo(n-2)+fibo(n-1)
# fibo = (lam f.lam n. if n <= 1 then n else f(n-2)+f(n-1))fibo
# fibo = Yv(lam f.lam n. if n <= 1 then n else f(n-2)+f(n-1))
#
term_fibo = term_app(Yv,
term_lam("f", term_lam("n",
  term_ifb(term_op2("<=", tvar_n, tint_1), tvar_n,
    term_op2("+", term_app(tvar_f, term_op2("-", tvar_n, tint_2)), term_app(tvar_f, term_op2("-", tvar_n, tint_1)))))))

_ = print("term_fibo(0) = ", term_interp(term_app(term_fibo, tint_0)))
_ = print("term_fibo(1) = ", term_interp(term_app(term_fibo, tint_1)))
_ = print("term_fibo(5) = ", term_interp(term_app(term_fibo, term_int(5))))
_ = print("term_fibo(10) = ", term_interp(term_app(term_fibo, term_int(10))))

############################################################

term_fact_fix = \
term_fix("f", "n",
  term_ifb(term_op2("<=", tvar_n, tint_0), tint_1,
    term_op2("*", tvar_n, term_app(tvar_f, term_op2("-", tvar_n, tint_1)))))
_ = print("term_fact_fix = ", term_fact_fix)

_ = print("term_fact_fix(3) = ", term_interp(term_app(term_fact_fix, term_int(3))))
_ = print("term_fact_fix(10) = ", term_interp(term_app(term_fact_fix, term_int(10))))

############################################################

term_fibo_fix = \
term_fix("f", "n",
  term_ifb(term_op2("<=", tvar_n, tint_1), tvar_n,
    term_op2("+", term_app(tvar_f, term_op2("-", tvar_n, tint_2)), term_app(tvar_f, term_op2("-", tvar_n, tint_1)))))
_ = print("term_fibo_fix = ", term_fibo_fix)

_ = print("term_fibo_fix(5) = ", term_interp(term_app(term_fibo_fix, term_int(5))))
_ = print("term_fibo_fix(10) = ", term_interp(term_app(term_fibo_fix, term_int(10))))

############################################################
############################################################
#
# datatype value =
# | VALint of sint
# | VALbtf of bool
# | VALlam of (term(*TMlam*), vlenv)
# | VALfix of (term(*TMfix*), vlenv)
# | VALpair of (value(*1st*), value(*2nd*))
#
class value:
    ctag = ""
    def __str__(self):
        return ("value(" + self.ctag + ")")
# end-of-class(value)

class value_int(value):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "VALint"
    def __str__(self):
        return ("VALint(" + str(self.arg1) + ")")
# end-of-class(value_int(value))

class value_btf(value):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "VALbtf"
    def __str__(self):
        return ("VALbtf(" + str(self.arg1) + ")")
# end-of-class(value_btf(value))

class value_lam(value):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "VALlam"
    def __str__(self):
        return ("VALlam(" + self.arg1 + "," + "..." + ")")
# end-of-class(value_lam(term)

class value_fix(value):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "VALfix"
    def __str__(self):
        return ("VALfix(" + self.arg1 + "," + "..." + ")")
# end-of-class(value_fix(term))

############################################################
#
# datatyp vlenv =
# | ENVnil of ()
# | ENVcons of (strn(*x*), value, vlenv)
#
class vlenv:
    ctag = ""
    def __str__(self):
        return ("vlenv(" + self.ctag + ")")
# end-of-class(vlenv)

class vlenv_nil(vlenv):
    def __init__(self):
        self.ctag = "ENVnil"
    def __str__(self):
        return ("ENVnil(" + ")")
# end-of-class(vlenv_nil(vlenv))

class vlenv_cons(vlenv):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "ENVcons"
    def __str__(self):
        return ("ENVcons(" + self.arg1 + "," + str(self.arg2) + "," + str(self.arg3) + ")")
# end-of-class(vlenv_cons(vlenv))

############################################################
############################################################

def vlenv_search(env0, tx):
    ctag = env0.ctag
    if ctag == "ENVnil":
      return None
    if ctag == "ENVcons":
        if tx == env0.arg1:
            return env0.arg2
        else:
            return vlenv_search(env0.arg3, tx)
    raise TypeError(env0) # HX-2026-06-02: should be deadcode!    

############################################################

def term_evaluate(tm0):
    env0 = vlenv_nil()
    return term_enveval(tm0, env0)

def term_enveval(tm0, env0):
    # print("term_enveval: tm0 = ", tm0)
    ctag = tm0.ctag
    if ctag == "TMint":
        return value_int(tm0.arg1)
    if ctag == "TMbtf":
        return value_btf(tm0.arg1)
    if (ctag == "TMvar"):
        return vlenv_search(env0, tm0.arg1)
    if (ctag == "TMlam"):
        return value_lam(tm0, env0)
    if (ctag == "TMfix"):
        return value_fix(tm0, env0)
    if (ctag == "TMapp"):
        # tm0 = TMapp(tm1, tm2)
        tm1 = tm0.arg1
        tm2 = tm0.arg2
        vl1 = term_enveval(tm1, env0)
        vl2 = term_enveval(tm2, env0)
        ctg1 = vl1.ctag
        # print("TMapp: ctg1 = ", ctg1)
        if (ctg1 == "VALlam"):
            vl1_tm1 = vl1.arg1
            vl1_env0 = vl1.arg2
            vl1_tm1_x = vl1_tm1.arg1
            vl1_tm1_t = vl1_tm1.arg2
            vl1_env1 = \
                vlenv_cons(vl1_tm1_x, vl2, vl1_env0)
            return term_enveval(vl1_tm1_t, vl1_env1)
        if (ctg1 == "VALfix"):
            vl1_tm1 = vl1.arg1
            vl1_env0 = vl1.arg2
            vl1_tm1_f = vl1_tm1.arg1
            vl1_tm1_x = vl1_tm1.arg2
            vl1_tm1_t = vl1_tm1.arg3
            vl1_env1 = \
                vlenv_cons(vl1_tm1_f, vl1, vl1_env0)
            vl1_env2 = \
                vlenv_cons(vl1_tm1_x, vl2, vl1_env1)
            return term_enveval(vl1_tm1_t, vl1_env2)
        # print("TypeError: non-function!")
        raise TypeError(tm1) # HX: TypeError: non-function
    if (ctag == "TMop2"):
        # tm0 = TMop2(tm1, tm2, tm3)
        nm1 = tm0.arg1
        vl2 = term_enveval(tm0.arg2, env0)
        vl3 = term_enveval(tm0.arg3, env0)
        if (nm1 == "+"):
            assert vl2.ctag == "VALint"
            assert vl3.ctag == "VALint"
            return value_int(vl2.arg1 + vl3.arg1)
        if (nm1 == "-"):
            assert vl2.ctag == "VALint"
            assert vl3.ctag == "VALint"
            return value_int(vl2.arg1 - vl3.arg1)
        if (nm1 == "*"):
            assert vl2.ctag == "VALint"
            assert vl3.ctag == "VALint"
            return value_int(vl2.arg1 * vl3.arg1)
        if (nm1 == "%"):
            assert vl2.ctag == "VALint"
            assert vl3.ctag == "VALint"
            return value_int(vl2.arg1 % vl3.arg1)
        if (nm1 == "/"):
            assert vl2.ctag == "VALint"
            assert vl3.ctag == "VALint"
            return value_int(vl2.arg1 // vl3.arg1)
        if (nm1 == ">"):
            assert vl2.ctag == "VALint"
            assert vl3.ctag == "VALint"
            return value_btf(vl2.arg1 > vl3.arg1)
        if (nm1 == "<"):
            assert vl2.ctag == "VALint"
            assert vl3.ctag == "VALint"
            return value_btf(vl2.arg1 < vl3.arg1)
        if (nm1 == ">="):
            assert vl2.ctag == "VALint"
            assert vl3.ctag == "VALint"
            return value_btf(vl2.arg1 >= vl3.arg1)
        if (nm1 == "<="):
            assert vl2.ctag == "VALint"
            assert vl3.ctag == "VALint"
            return value_btf(vl2.arg1 <= vl3.arg1)
        if (nm1 == "=="):
            assert vl2.ctag == "VALint"
            assert vl3.ctag == "VALint"
            return value_btf(vl2.arg1 == vl3.arg1)
        if (nm1 == "!="):
            assert vl2.ctag == "VALint"
            assert vl3.ctag == "VALint"
            return value_btf(vl2.arg1 != vl3.arg1)
        raise TypeError(nm1) # HX: TypeError: non-supported
    if (ctag == "TMifb"):
        # tm0 = TMifb(tm1, tm2, tm3)
        tm1 = tm0.arg1
        vl1 = term_enveval(tm1, env0)
        ctg1 = vl1.ctag
        # print("TMifb: ctg1 = ", ctg1)
        if (ctg1 == "VALbtf"):
            # vl1 = VALbtf(btf)
            if (vl1.arg1):
                return term_enveval(tm0.arg2, env0)
            else:
                return term_enveval(tm0.arg3, env0)
        # print("TypeError: non-boolean-cond!")
        raise TypeError(tm1) # HX: TypeError: non-boolean        
    raise TypeError(tm1) # HX: TypeError: term_enveval(...)
############################################################

_ = print("evaluate(tint_2) = ", term_evaluate(tint_2))
_ = print("evaluate(tbtf_t) = ", term_evaluate(tbtf_t))
_ = print("evaluate(tbtf_f) = ", term_evaluate(tbtf_f))
_ = print("evaluate(term_I(tint_2)) = ", term_evaluate(term_app(term_I, tint_2)))
_ = print("evaluate(term_I(tbtf_t)) = ", term_evaluate(term_app(term_I, tbtf_t)))
_ = print("evaluate(term_dbl(tint_2)) = ", term_evaluate(term_app(term_dbl, tint_2)))
_ = print("evaluate(term_sqr(tint_2)) = ", term_evaluate(term_app(term_sqr, tint_2)))

############################################################

term_fact_fix = \
term_fix("f", "n",
  term_ifb(term_op2("<=", tvar_n, tint_0), tint_1,
    term_op2("*", tvar_n, term_app(tvar_f, term_op2("-", tvar_n, tint_1)))))
_ = print("term_fact_fix = ", term_fact_fix)

_ = print("evaluate(term_fact_fix(3)) = ", term_evaluate(term_app(term_fact_fix, term_int(3))))
_ = print("evaluate(term_fact_fix(10)) = ", term_evaluate(term_app(term_fact_fix, term_int(10))))

############################################################

