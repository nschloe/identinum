# -*- coding: utf-8 -*-
#
import decimal2rational
from numpy import pi

def test_rational():

    num, den, mult_pi, root, diff = \
        decimal2rational.decimal2rational(3.0 / 7.0)

    assert num == 3
    assert den == 7
    assert mult_pi == 0
    assert root == 1

    return


def test_root2():

    num, den, mult_pi, root, diff = \
        decimal2rational.decimal2rational((3.0 / 7.0)**0.5)

    assert num == 3
    assert den == 7
    assert mult_pi == 0
    assert root == 2

    return


def test_root3():

    num, den, mult_pi, root, diff = \
        decimal2rational.decimal2rational((3.0 / 7.0)**(1.0/3.0))

    assert num == 3
    assert den == 7
    assert mult_pi == 0
    assert root == 3

    return


def test_root34():

    num, den, mult_pi, root, diff = \
        decimal2rational.decimal2rational(3.0**0.5 / 2.0)

    assert num == 3
    assert den == 4
    assert mult_pi == 0
    assert root == 2

    return


def test_pi():

    num, den, mult_pi, root, diff = \
        decimal2rational.decimal2rational(3.0/4.0 * pi)

    assert num == 3
    assert den == 4
    assert mult_pi == 1
    assert root == 1

    return


def test_sqrt_pi_2():

    num, den, mult_pi, root, diff = \
        decimal2rational.decimal2rational((0.5*pi)**0.5)

    assert num == 1
    assert den == 2
    assert mult_pi == 1
    assert root == 2

    return


if __name__ == '__main__':
    test_d2r()
