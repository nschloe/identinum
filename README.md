# identinum

A command-line wrapper around [mpmath's identify](http://docs.sympy.org/0.7.1/modules/mpmath/identification.html#identify).

[![CircleCI](https://img.shields.io/circleci/project/github/nschloe/identinum/master.svg?style=flat-square)](https://circleci.com/gh/nschloe/identinum/tree/master)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/identinum.svg?style=flat-square)](https://codecov.io/gh/nschloe/identinum)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)
[![PyPi Version](https://img.shields.io/pypi/v/identinum.svg?style=flat-square)](https://pypi.org/project/identinum)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/identinum.svg?style=flat-square&logo=github&label=Stars&logoColor=white)](https://github.com/nschloe/identinum)

You come across the number 0.866025. It looks vaguely familiar but you can't
quite point your finger at it? Then identinum is for you.

identinum is a small command-line utility that "de-decimalizes" decimal numbers into
approximate rational expressions (with some basic functions).
```
$ identinum 0.4285714285
3/7   -7.14285297576112E-11
```
```
$ identinum 0.866025403
sqrt(3)/2   -7.84438675343059E-10
```

### Installation

identinum is [available from the Python Package Index](https://pypi.org/project/identinum/), so
simply type
```
pip install identinum
```
to install or upgrade.

### Testing

To run the identinum unit tests, check out this repository and type
```
pytest
```

### License

identinum is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
