# -*- coding: utf-8 -*-
#
__all__ = [
    'dedec', 'repr'
    ]

__version__ = '0.2.3'
__author__ = 'Nico Schlömer'
__author_email__ = 'nico.schloemer@gmail.com'
__website__ = 'https://github.com/nschloe/dedec'


def dedec(a, max_denominator=10000, abs_tol=1.0e-15):
    from math import pi, exp, log, sin, cos, tan, asin, acos, atan, copysign, \
                     pow
    from fractions import gcd

    # We need a list of tuples here since we rely on the ordering. A dict
    # doesn't have that.
    funs = [
            (None, lambda x: x, lambda x: x),
            ('sqrt', lambda x: x**0.5, lambda x: x**2),
            ('root3',
             # http://stackoverflow.com/a/1361789/353337
             lambda x: copysign(pow(abs(x), 1.0/3.0), x),
             lambda x: x**3
             ),
            ('exp', exp, log),
            ('logn', log, exp),
            ('sin', sin, asin),
            ('cos', cos, acos),
            ('tan', tan, atan)
            ]

    sols = []
    for fun_name, fun, inv in funs:
        try:
            a0 = inv(a)
        except ValueError:  # math domain error
            continue

        for mult_pi in range(3):
            a1 = a0 / pi**mult_pi

            for den in range(1, max_denominator+1):
                num = int(round(a1*den))
                if gcd(num, den) > 1:
                    continue
                x = float(num) / den * pi**mult_pi
                try:
                    error = a - fun(x)
                except ValueError:  # math domain error
                    continue
                if abs(error) < abs_tol:
                    sols.append((num, den, mult_pi, fun_name, error))

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
