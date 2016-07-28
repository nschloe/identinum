# -*- coding: utf-8 -*-
#
__all__ = [
    'decimal2rational'
    ]

__version__ = '0.2.0'
__author__ = 'Nico Schlömer'
__author_email__ = 'nico.schloemer@gmail.com'
__website__ = 'https://github.com/nschloe/decimal2rational'


def decimal2rational(a, max_denominator=1000, tol=1.0e-15):
    from math import pi, exp, log, asin, acos, atan

    # We need a list of tuples here since we rely on the ordering. A dict
    # doesn't have that.
    funs = [
            (None, lambda x: x),
            ('sqrt', lambda x: x**2),
            ('root3', lambda x: x**3)
            ]

    if a > 0:
        funs.append(('exp', lambda x: log(x)))

    funs.append(('logn', lambda x: exp(x)))

    if a >= -1.0 and a <= 1.0:
        funs.append(('sin', lambda x: asin(x)))
        funs.append(('cos', lambda x: acos(x)))

    funs.append(('tan', lambda x: atan(x)))

    for fun_name, fun in funs:
        a0 = a
        a0 = fun(a0)
        for mult_pi in range(2):
            if mult_pi > 0:
                a0 /= pi**mult_pi

            for den in range(1, max_denominator+1):
                rd = round(a0*den)
                diff = a0*den - rd
                if abs(diff) < tol * a0*den:
                    return int(rd), den, mult_pi, fun_name, diff

    return None, None, None, None, None
