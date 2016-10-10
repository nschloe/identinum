# -*- coding: utf-8 -*-
#
import dedec
from math import pi, exp, log, sin, cos, tan


def test_rational():

    sols = dedec.dedec(3.0 / 7.0)

    num, den, mult_pi, fun, diff = sols[0]

    assert num == 3
    assert den == 7
    assert mult_pi == 0
    assert fun is None

    assert dedec.repr(num, den, mult_pi, fun) == '3 / 7'

    return


def test_root2():

    sols = dedec.dedec((3.0 / 7.0)**0.5)

    num, den, mult_pi, fun, diff = sols[0]

    assert num == 3
    assert den == 7
    assert mult_pi == 0
    assert fun == 'sqrt'

    assert dedec.repr(num, den, mult_pi, fun) == 'sqrt(3 / 7)'

    return


def test_root3():

    sols = dedec.dedec((3.0 / 7.0)**(1.0/3.0))

    num, den, mult_pi, fun, diff = sols[0]

    assert num == 3
    assert den == 7
    assert mult_pi == 0
    assert fun == 'root3'

    assert dedec.repr(num, den, mult_pi, fun) == 'root3(3 / 7)'

    return


def test_root34():

    sols = dedec.dedec(3.0**0.5 / 2.0)

    num, den, mult_pi, fun, diff = sols[0]

    assert num == 3
    assert den == 4
    assert mult_pi == 0
    assert fun == 'sqrt'

    assert dedec.repr(num, den, mult_pi, fun) == 'sqrt(3 / 4)'

    return


def test_pi():

    sols = dedec.dedec(3.0/4.0 * pi)

    num, den, mult_pi, fun, diff = sols[0]

    assert num == 3
    assert den == 4
    assert mult_pi == 1
    assert fun is None

    assert dedec.repr(num, den, mult_pi, fun) == '3 / 4 * pi'

    return


def test_sqrt_pi_2():

    sols = dedec.dedec((0.5*pi)**0.5)

    num, den, mult_pi, fun, diff = sols[0]

    assert num == 1
    assert den == 2
    assert mult_pi == 1
    assert fun == 'sqrt'

    assert dedec.repr(num, den, mult_pi, fun) == 'sqrt(1 / 2 * pi)'

    return


def test_exp_2_pi():

    sols = dedec.dedec(exp(2*pi), max_denominator=100)

    num, den, mult_pi, fun, diff = sols[0]

    assert num == 2
    assert den == 1
    assert mult_pi == 1
    assert fun == 'exp'

    assert dedec.repr(num, den, mult_pi, fun) == 'exp(2 * pi)'

    return


def test_logn_0_5():

    sols = dedec.dedec(log(0.5))

    num, den, mult_pi, fun, diff = sols[0]

    assert num == 1
    assert den == 2
    assert mult_pi == 0
    assert fun == 'logn'

    assert dedec.repr(num, den, mult_pi, fun) == 'logn(1 / 2)'

    return


def test_sin_1():

    sols = dedec.dedec(sin(1.0))

    num, den, mult_pi, fun, diff = sols[0]

    assert num == 1
    assert den == 1
    assert mult_pi == 0
    assert fun == 'sin'

    assert dedec.repr(num, den, mult_pi, fun) == 'sin(1)'

    return


def test_cos_1():

    sols = dedec.dedec(cos(1.0))

    num, den, mult_pi, fun, diff = sols[0]

    assert num == 1
    assert den == 1
    assert mult_pi == 0
    assert fun == 'cos'

    assert dedec.repr(num, den, mult_pi, fun) == 'cos(1)'

    return


def test_tan_1():

    sols = dedec.dedec(tan(1.0))

    num, den, mult_pi, fun, diff = sols[0]

    assert num == 1
    assert den == 1
    assert mult_pi == 0
    assert fun == 'tan'

    assert dedec.repr(num, den, mult_pi, fun) == 'tan(1)'

    return


def test_pi2():

    sols = dedec.dedec((pi**2) / 4.0)

    num, den, mult_pi, fun, diff = sols[0]

    assert num == 1
    assert den == 4
    assert mult_pi == 2
    assert fun is None

    assert dedec.repr(num, den, mult_pi, fun) == '1 / 4 * pi^2'

    return


if __name__ == '__main__':
    test_root3()
