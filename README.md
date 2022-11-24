# identinum

[![PyPi Version](https://img.shields.io/pypi/v/identinum.svg?style=flat-square)](https://pypi.org/project/identinum)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/identinum.svg?style=flat-square)](https://pypi.org/pypi/identinum/)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/identinum.svg?style=flat-square&logo=github&label=Stars&logoColor=white)](https://github.com/nschloe/identinum)
[![PyPi downloads](https://img.shields.io/pypi/dm/identinum.svg?style=flat-square)](https://pypistats.org/packages/identinum)

[![Discord](https://img.shields.io/static/v1?logo=discord&label=chat&message=on%20discord&color=7289da&style=flat-square)](https://discord.gg/Z6DMsJh4Hr)

[![gh-actions](https://img.shields.io/github/workflow/status/nschloe/identinum/ci?style=flat-square)](https://github.com/nschloe/identinum/actions?query=workflow%3Aci)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/identinum.svg?style=flat-square)](https://codecov.io/gh/nschloe/identinum)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)

A command-line wrapper around [mpmath's
identify](http://docs.sympy.org/0.7.1/modules/mpmath/identification.html#identify).

You come across the number 0.866025. It looks vaguely familiar but you can't quite point
your finger at it? Then identinum is for you.

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

identinum is [available from the Python Package
Index](https://pypi.org/project/identinum/), so simply do
```
pip install identinum
```

### Testing

To run the identinum unit tests, check out this repository and type
```
pytest
```
