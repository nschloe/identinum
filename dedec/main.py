# -*- coding: utf-8 -*-
#
import mpmath
from sympy import sympify


def dedec(a, abs_tol=1.0e-15):
    sols = mpmath.identify(a, ['pi'], tol=abs_tol, full=True)
    return list(set([sympify(sol) for sol in sols]))
