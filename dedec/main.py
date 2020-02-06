import mpmath
from sympy import sympify


def identify(a, abs_tol=1.0e-15):
    sols = mpmath.identify(a, ["pi"], tol=abs_tol, full=True)
    lst = list({sympify(sol) for sol in sols})
    # sort by complexity
    num_ops = [expr.count_ops() for expr in lst]
    lst = [expr for _, expr in sorted(zip(num_ops, lst))]
    return lst


def findpoly(a, tol=1.0e-15, maxcoeff=100000, max_degree=10):
    return mpmath.findpoly(a, n=max_degree, tol=tol, maxcoeff=maxcoeff)
