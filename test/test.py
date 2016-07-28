# -*- coding: utf-8 -*-
#
import decimal2rational
from math import pi, exp, log


def test_rational():

    num, den, mult_pi, fun, diff = \
        decimal2rational.decimal2rational(3.0 / 7.0)

    assert num == 3
    assert den == 7
    assert mult_pi == 0
    assert fun is None

    return


def test_root2():

    num, den, mult_pi, fun, diff = \
        decimal2rational.decimal2rational((3.0 / 7.0)**0.5)

    assert num == 3
    assert den == 7
    assert mult_pi == 0
    assert fun == 'sqrt'

    return


def test_root3():

    num, den, mult_pi, fun, diff = \
        decimal2rational.decimal2rational((3.0 / 7.0)**(1.0/3.0))

    assert num == 3
    assert den == 7
    assert mult_pi == 0
    assert fun == 'root3'

    return


def test_root34():

    num, den, mult_pi, fun, diff = \
        decimal2rational.decimal2rational(3.0**0.5 / 2.0)

    assert num == 3
    assert den == 4
    assert mult_pi == 0
    assert fun == 'sqrt'

    return


def test_pi():

    num, den, mult_pi, fun, diff = \
        decimal2rational.decimal2rational(3.0/4.0 * pi)

    assert num == 3
    assert den == 4
    assert mult_pi == 1
    assert fun is None

    return


def test_sqrt_pi_2():

    num, den, mult_pi, fun, diff = \
        decimal2rational.decimal2rational((0.5*pi)**0.5)

    assert num == 1
    assert den == 2
    assert mult_pi == 1
    assert fun == 'sqrt'

    return


def test_exp_2_pi():

    num, den, mult_pi, fun, diff = \
        decimal2rational.decimal2rational(exp(2*pi))

    assert num == 2
    assert den == 1
    assert mult_pi == 1
    assert fun == 'exp'

    return


def test_logn_0_5():

    num, den, mult_pi, fun, diff = \
        decimal2rational.decimal2rational(log(0.5))

    assert num == 1
    assert den == 2
    assert mult_pi == 0
    assert fun == 'logn'

    return


if __name__ == '__main__':
    test_d2r()
