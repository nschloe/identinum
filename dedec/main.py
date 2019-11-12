import mpmath
from sympy import sympify


def identify(a, abs_tol=1.0e-15):
    sols = mpmath.identify(a, ["pi"], tol=abs_tol, full=True)
    return list(set([sympify(sol) for sol in sols]))


def findpoly(a, tol=1.0e-15, maxcoeff=100000, max_degree=10):
    return mpmath.findpoly(a, n=max_degree, tol=tol, maxcoeff=maxcoeff)
