# -*- coding: utf-8 -*-
#
__all__ = [
    'dedec'
    ]

__version__ = '0.2.0'
__author__ = 'Nico Schlömer'
__author_email__ = 'nico.schloemer@gmail.com'
__website__ = 'https://github.com/nschloe/dedec'


def dedec(a, max_denominator=100, abs_tol=1.0e-15):
    from math import pi, exp, log, asin, acos, atan
    from fractions import gcd

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

    sols = []
    for fun_name, fun in funs:
        a0 = a
        a0 = fun(a0)
        for mult_pi in range(2):
            if mult_pi > 0:
                a0 /= pi**mult_pi

            for den in range(1, max_denominator+1):
                num = int(round(a0*den))
                if gcd(num, den) > 1:
                    continue
                diff = a0 - float(num) / den
                if abs(diff) < abs_tol:
                    sols.append((num, den, mult_pi, fun_name, diff))

    return sols


def repr(num, denom, mult_pi, fun_name):

    num_str = '%d' % num

    if denom > 1:
        num_str += ' / %d' % denom

    if mult_pi == 1:
        num_str += ' * pi'
    elif mult_pi > 1:
        num_str += ' * pi^%d' % mult_pi

    if fun_name is None:
        return '%s' % num_str

    return '%s(%s)' % (fun_name, num_str)
