# -*- coding: utf-8 -*-
#

__all__ = [
    'decimal2rational'
    ]

__version__ = '0.1.0'
__author__ = 'Nico Schlömer'
__author_email__ = 'nico.schloemer@gmail.com'
__website__ = 'https://github.com/nschloe/decimal2rational'


def decimal2rational(a, max_denominator=1000, tol=1.0e-10):
    num0 = None
    d0 = None
    diff0 = None
    for d in range(1, max_denominator+1):
        rd = round(a*d)
        diff = a*d - rd
        if abs(diff) < tol * a*d:
            num0 = int(rd)
            d0 = d
            diff0 = diff
            break

    return num0, d0, diff0
