# -*- coding: utf-8 -*-
#
import decimal2rational


def test_rational():

    num, den, root, diff = \
        decimal2rational.decimal2rational(3.0 / 7.0)

    print(num)
    print(den)
    print(root)

    assert num == 3
    assert den == 7
    assert root == 1

    return


def test_root2():

    num, den, root, diff = \
        decimal2rational.decimal2rational((3.0 / 7.0)**0.5)

    assert num == 3
    assert den == 7
    assert root == 2

    return


def test_root3():

    num, den, root, diff = \
        decimal2rational.decimal2rational((3.0 / 7.0)**(1.0/3.0))

    assert num == 3
    assert den == 7
    assert root == 3

    return


def test_root34():

    num, den, root, diff = \
        decimal2rational.decimal2rational(3.0**0.5 / 2.0)

    assert num == 3
    assert den == 4
    assert root == 2

    return


if __name__ == '__main__':
    test_d2r()
