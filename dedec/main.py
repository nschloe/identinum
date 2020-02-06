import mpmath
from sympy import sympify


def identify(a, abs_tol=1.0e-15):
    # adding "pi" can sometimes hide desired solutions
    sols = mpmath.identify(a, tol=abs_tol, full=True)
    sols_pi = mpmath.identify(a, ["pi"], tol=abs_tol, full=True)
    lst = list({sympify(sol) for sol in sols + sols_pi})
    # sort by complexity
    num_ops = [expr.count_ops() for expr in lst]
    lst = [expr for _, expr in sorted(zip(num_ops, lst), key=lambda pair: pair[0])]
    return lst


def findpoly(a, tol=1.0e-15, maxcoeff=100000, max_degree=10):
    return mpmath.findpoly(a, n=max_degree, tol=tol, maxcoeff=maxcoeff)
