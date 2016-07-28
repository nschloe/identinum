# -*- coding: utf-8 -*-
#

__all__ = [
    'decimal2rational'
    ]

__version__ = '0.1.0'
__author__ = 'Nico Schlömer'
__author_email__ = 'nico.schloemer@gmail.com'
__website__ = 'https://github.com/nschloe/decimal2rational'


def decimal2rational(a, max_denominator=1000, max_root=5, tol=1.0e-10):
    num0 = None
    den0 = None
    root0 = None
    diff0 = None
    for root in range(1, max_root+1):
        a0 = a**root
        for den in range(1, max_denominator+1):
            rd = round(a0*den)
            diff = a0*den - rd
            if abs(diff) < tol * a0*den:
                num0 = int(rd)
                den0 = den
                root0 = root
                diff0 = diff
                return int(rd), den, root, diff

    return None, None, None, None
