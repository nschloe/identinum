# -*- coding: utf-8 -*-
#
from math import pi

__all__ = [
    'decimal2rational'
    ]

__version__ = '0.2.0'
__author__ = 'Nico Schlömer'
__author_email__ = 'nico.schloemer@gmail.com'
__website__ = 'https://github.com/nschloe/decimal2rational'


def decimal2rational(a, max_denominator=1000, max_root=5, tol=1.0e-10):

    for mult_pi in range(2):
        for root in range(1, max_root+1):
            a0 = a
            a0 **= root
            if mult_pi > 0:
                a0 /= pi**mult_pi

            for den in range(1, max_denominator+1):
                rd = round(a0*den)
                diff = a0*den - rd
                if abs(diff) < tol * a0*den:
                    num0 = int(rd)
                    den0 = den
                    root0 = root
                    diff0 = diff
                    return int(rd), den, mult_pi, root, diff

    return None, None, None, None, None
