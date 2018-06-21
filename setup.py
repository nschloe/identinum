# -*- coding: utf-8 -*-
#
import os
from setuptools import setup, find_packages
import codecs

# https://packaging.python.org/single_source_version/
base_dir = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(base_dir, "dedec", "__about__.py"), "rb") as f:
    exec(f.read(), about)


def read(fname):
    return codecs.open(os.path.join(base_dir, fname), encoding="utf-8").read()


setup(
    name="dedec",
    version=about["__version__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    packages=find_packages(),
    description="Convert decimals to approximate rational expressions",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/nschloe/dedec",
    license=about["__license__"],
    platforms="any",
    install_requires=["mpmath", "sympy", "pipdate"],
    classifiers=[
        about["__status__"],
        about["__license__"],
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: Utilities",
    ],
    entry_points={"console_scripts": ["dedec = dedec.cli:main"]},
)
