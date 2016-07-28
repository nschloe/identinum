# -*- coding: utf-8 -*-
#
import os
from setuptools import setup
import codecs

from dedec import __name__, __version__, __author__, __author_email__


def read(fname):
    try:
        content = codecs.open(
            os.path.join(os.path.dirname(__file__), fname),
            encoding='utf-8'
            ).read()
    except Exception:
        content = ''
    return content

setup(
    name=__name__,
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    packages=['dedec'],
    description='Convert decimal to (approximate) rational number',
    long_description=read('README.rst'),
    url='https://github.com/nschloe/dedec',
    download_url='https://pypi.python.org/pypi/dedec',
    license='License :: OSI Approved :: MIT License',
    platforms='any',
    requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Topic :: Utilities'
        ],
    scripts=[
        'tools/d2r'
        ]
    )
