from math import exp, log, pi

import sympy

import identinum


def test_rational():
    sols = identinum.identify(3.0 / 7.0)
    assert sols[0] == sympy.Rational(3, 7)


def test_root2():
    sols = identinum.identify((3.0 / 7.0) ** 0.5)
    assert sols[0] == sympy.sqrt(sympy.Rational(3, 7))


def test_root3():
    sols = identinum.identify((3.0 / 7.0) ** (1.0 / 3.0))
    assert sols[0] == sympy.Rational(3, 7) ** sympy.Rational(1, 3)


def test_root34():
    sols = identinum.identify(3.0 ** 0.5 / 2.0)
    assert sols[0] == sympy.sqrt(sympy.Rational(3, 4))


def test_pi():
    sols = identinum.identify(3.0 / 4.0 * pi)
    assert sols[0] == sympy.pi * sympy.Rational(3, 4)


def test_sqrt_pi_2():
    sols = identinum.identify((0.5 * pi) ** 0.5)
    assert sols[0] == sympy.sqrt(sympy.pi * sympy.Rational(1, 2))


def test_exp_2_pi():
    sols = identinum.identify(exp(2 * pi))
    assert sols[0] == sympy.exp(sympy.pi * 2)


def test_logn_0_5():
    sols = identinum.identify(log(0.5))
    assert sols[0] == sympy.log(sympy.Rational(1, 2))


def test_pi2():
    sols = identinum.identify(pi ** 2 / 4.0)
    assert sols[0] == sympy.pi ** 2 * sympy.Rational(1, 4)


def test_poly():
    sols = identinum.findpoly(0.17852201277, tol=1.0e-10)
    assert sols == [-79852, -12268, 4735]


if __name__ == "__main__":
    test_rational()
