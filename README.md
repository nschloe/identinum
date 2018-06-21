# dedec

A command-line wrapper around [mpmath's identify](http://docs.sympy.org/0.7.1/modules/mpmath/identification.html#identify).

[![CircleCI](https://img.shields.io/circleci/project/github/nschloe/dedec/master.svg)](https://circleci.com/gh/nschloe/dedec/tree/master)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/dedec.svg)](https://codecov.io/gh/nschloe/dedec)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![PyPi Version](https://img.shields.io/pypi/v/dedec.svg)](https://pypi.python.org/pypi/dedec)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/dedec.svg?logo=github&label=Star)](https://github.com/nschloe/dedec)

You come across the number 0.866025. It looks vaguely familiar but you can't
quite point your finger at it? Then dedec is for you.

dedec is a small command-line utility that "de-decimalizes" decimal numbers into
approximate rational expressions (with some basic functions).
```
$ dedec 0.4285714285
3/7   -7.14285297576112E-11
```
```
$ dedec 0.866025403
sqrt(3)/2   -7.84438675343059E-10
```

### Installation

#### Python Package Index

dedec is [available from the Python Package
Index](https://pypi.python.org/pypi/dedec/), so simply type
```
pip install -U dedec
```
to install or upgrade.

### Testing

To run the dedec unit tests, check out this repository and type
```
pytest
```

### Distribution

To create a new release

1. bump the `__version__` number,

2. publish to PyPi and GitHub:
    ```
    $ make publish
    ```

### License

dedec is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
