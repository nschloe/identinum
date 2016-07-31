# dedec

[![Build Status](https://travis-ci.org/nschloe/dedec.svg?branch=master)](https://travis-ci.org/nschloe/dedec)
[![codecov](https://codecov.io/gh/nschloe/dedec/branch/master/graph/badge.svg)](https://codecov.io/gh/nschloe/dedec)
[![PyPi Version](https://img.shields.io/pypi/v/dedec.svg)](https://pypi.python.org/pypi/dedec)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/dedec.svg?style=social&label=Star&maxAge=2592000)](https://github.com/nschloe/dedec)

You come across the number 0.866025. It looks vaguely familiar but you can't
quite point your finger at it? Then dedec is for you.

dedec is a small command-line utility that "de-decimalizes" decimal numbers into
approximate rational expressions (with some basic functions).
```
$ dedec 0.4285714285
3 / 7   -7.1429e-11
sqrt(9 / 49)   -7.1429e-11
```
```
$ dedec 0.866025
sqrt(3 / 4)   -4.0378e-07
sin(1 / 3 * pi)   -4.0378e-07
cos(1 / 6 * pi)   -4.0378e-07
```
It can also be used from Python
```python
import dedec

a = 3.0 / 7.0
sols = dedec.dedec(a)
numerator, denominator, mult_pi, fun, diff = sols[0]
assert numerator == 3
assert denominator == 7
```

### Installation

#### Python Package Index

dedec is [available from the Python Package
Index](https://pypi.python.org/pypi/dedec/), so simply type
```
pip install -U dedec
```
to install or upgrade.

#### Manual installation

Download dedec from [GitHub](https://github.com/nschloe/dedec) and
install it with
```
python setup.py install
```

### Testing

To run the dedec unit tests, check out this repository and type
```
nosetests
```


### Distribution
To create a new release

1. bump the `__version__` number,

2. create a Git tag,
    ```
    $ git tag v0.3.1
    $ git push --tags
    ```
    and

3. upload to PyPi:
    ```
    $ make upload
    ```

### License

dedec is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
