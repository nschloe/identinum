# decimal2rational

[![Build Status](https://travis-ci.org/nschloe/decimal2rational.svg?branch=master)](https://travis-ci.org/nschloe/decimal2rational)
[![codecov](https://codecov.io/gh/nschloe/decimal2rational/branch/master/graph/badge.svg)](https://codecov.io/gh/nschloe/decimal2rational)
[![PyPi Version](https://img.shields.io/pypi/v/decimal2rational.svg)](https://pypi.python.org/pypi/decimal2rational)

This is a small command-line utility that converts decimal numbers into
(approximate) rational numbers (with roots).
```
$ d2r 0.42857142857142
0.42857142857142 = 3 / 7   -5.9952e-14
$ d2r 0.8660254037844
0.8660254037844 = sqrt(3 / 4)   -2.6823e-13
```
It can also be used from Python
```python
import decimal2rational

a = 3.0 / 7.0
numerator, denominator, root, diff = decimal2rational.decimal2rational(a)
assert numerator == 3
assert denominator == 7
assert root == 1
```

### Installation

#### Python Package Index

decimal2rational is [available from the Python Package
Index](https://pypi.python.org/pypi/decimal2rational/), so simply type
```
pip install -U decimal2rational
```
to install or upgrade.

#### Manual installation

Download decimal2rational from [GitHub](https://github.com/nschloe/decimal2rational) and
install it with
```
python setup.py install
```

### Testing

To run the decimal2rational unit tests, check out this repository and type
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

decimal2rational is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
