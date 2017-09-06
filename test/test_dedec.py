# -*- coding: utf-8 -*-
#
import dedec
from math import pi, exp, log
import sympy


def test_rational():
    sols = dedec.dedec(3.0 / 7.0)
    assert sols[0] == sympy.Rational(3, 7)
    return


def test_root2():
    sols = dedec.dedec((3.0 / 7.0)**0.5)
    assert sols[0] == sympy.sqrt(sympy.Rational(3, 7))
    return


def test_root3():
    sols = dedec.dedec((3.0 / 7.0)**(1.0/3.0))
    assert sols[0] == sympy.Rational(3, 7)**sympy.Rational(1, 3)
    return


def test_root34():
    sols = dedec.dedec(3.0**0.5 / 2.0)
    assert sols[0] == sympy.sqrt(sympy.Rational(3, 4))
    return


def test_pi():
    sols = dedec.dedec(3.0/4.0 * pi)
    assert sols[0] == sympy.pi * sympy.Rational(3, 4)
    return


def test_sqrt_pi_2():
    sols = dedec.dedec((0.5*pi)**0.5)
    assert sols[0] == sympy.sqrt(sympy.pi * sympy.Rational(1, 2))
    return


def test_exp_2_pi():
    sols = dedec.dedec(exp(2*pi))
    assert sols[0] == sympy.exp(sympy.pi * 2)
    return


def test_logn_0_5():
    sols = dedec.dedec(log(0.5))
    assert sols[0] == sympy.log(sympy.Rational(1, 2))
    return


def test_pi2():
    sols = dedec.dedec(pi**2 / 4.0)
    assert sols[0] == sympy.pi**2 * sympy.Rational(1, 4)
    return


if __name__ == '__main__':
    test_rational()
