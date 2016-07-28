# -*- coding: utf-8 -*-
#
import decimal2rational
from math import pi, exp, log, sin, cos, tan


def test_rational():

    sols = decimal2rational.decimal2rational(3.0 / 7.0)

    num, den, mult_pi, fun, diff = sols[0]

    assert num == 3
    assert den == 7
    assert mult_pi == 0
    assert fun is None

    assert decimal2rational.repr(num, den, mult_pi, fun) == '3 / 7'

    return


def test_root2():

    sols = decimal2rational.decimal2rational((3.0 / 7.0)**0.5)

    num, den, mult_pi, fun, diff = sols[0]

    assert num == 3
    assert den == 7
    assert mult_pi == 0
    assert fun == 'sqrt'

    assert decimal2rational.repr(num, den, mult_pi, fun) == 'sqrt(3 / 7)'

    return


def test_root3():

    sols = decimal2rational.decimal2rational((3.0 / 7.0)**(1.0/3.0))

    num, den, mult_pi, fun, diff = sols[0]

    assert num == 3
    assert den == 7
    assert mult_pi == 0
    assert fun == 'root3'

    assert decimal2rational.repr(num, den, mult_pi, fun) == 'root3(3 / 7)'

    return


def test_root34():

    sols = decimal2rational.decimal2rational(3.0**0.5 / 2.0)

    num, den, mult_pi, fun, diff = sols[0]

    assert num == 3
    assert den == 4
    assert mult_pi == 0
    assert fun == 'sqrt'

    assert decimal2rational.repr(num, den, mult_pi, fun) == 'sqrt(3 / 4)'

    return


def test_pi():

    sols = decimal2rational.decimal2rational(3.0/4.0 * pi)

    num, den, mult_pi, fun, diff = sols[0]

    assert num == 3
    assert den == 4
    assert mult_pi == 1
    assert fun is None

    assert decimal2rational.repr(num, den, mult_pi, fun) == '3 / 4 * pi'

    return


def test_sqrt_pi_2():

    sols = decimal2rational.decimal2rational((0.5*pi)**0.5)

    num, den, mult_pi, fun, diff = sols[0]

    assert num == 1
    assert den == 2
    assert mult_pi == 1
    assert fun == 'sqrt'

    assert decimal2rational.repr(num, den, mult_pi, fun) == 'sqrt(1 / 2 * pi)'

    return


def test_exp_2_pi():

    sols = decimal2rational.decimal2rational(exp(2*pi))

    num, den, mult_pi, fun, diff = sols[0]

    assert num == 2
    assert den == 1
    assert mult_pi == 1
    assert fun == 'exp'

    assert decimal2rational.repr(num, den, mult_pi, fun) == 'exp(2 * pi)'

    return


def test_logn_0_5():

    sols = decimal2rational.decimal2rational(log(0.5))

    num, den, mult_pi, fun, diff = sols[0]

    assert num == 1
    assert den == 2
    assert mult_pi == 0
    assert fun == 'logn'

    assert decimal2rational.repr(num, den, mult_pi, fun) == 'logn(1 / 2)'

    return


def test_sin_1():

    sols = decimal2rational.decimal2rational(sin(1.0))

    num, den, mult_pi, fun, diff = sols[0]

    assert num == 1
    assert den == 1
    assert mult_pi == 0
    assert fun == 'sin'

    assert decimal2rational.repr(num, den, mult_pi, fun) == 'sin(1)'

    return


def test_cos_1():

    sols = decimal2rational.decimal2rational(cos(1.0))

    num, den, mult_pi, fun, diff = sols[0]

    assert num == 1
    assert den == 1
    assert mult_pi == 0
    assert fun == 'cos'

    assert decimal2rational.repr(num, den, mult_pi, fun) == 'cos(1)'

    return


def test_tan_1():

    sols = decimal2rational.decimal2rational(tan(1.0))

    num, den, mult_pi, fun, diff = sols[0]

    assert num == 1
    assert den == 1
    assert mult_pi == 0
    assert fun == 'tan'

    assert decimal2rational.repr(num, den, mult_pi, fun) == 'tan(1)'

    return


if __name__ == '__main__':
    test_d2r()
