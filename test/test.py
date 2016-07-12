# -*- coding: utf-8 -*-
#
import decimal2rational


def test_d2r():

    num, den, diff = decimal2rational.decimal2rational(3.0 / 7.0)

    assert num == 3
    assert den == 7

    return


if __name__ == '__main__':
    test_d2r()
