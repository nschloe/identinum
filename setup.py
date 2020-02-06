import os

from setuptools import find_packages, setup

# https://packaging.python.org/single_source_version/
base_dir = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(base_dir, "identinum", "__about__.py"), "rb") as f:
    exec(f.read(), about)

setup(
    name="identinum",
    version=about["__version__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    packages=find_packages(),
    description="Convert decimals to approximate rational expressions",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nschloe/identinum",
    license=about["__license__"],
    platforms="any",
    python_requires=">=3.6",
    install_requires=["mpmath", "sympy"],
    classifiers=[
        about["__status__"],
        about["__license__"],
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: Utilities",
    ],
    entry_points={"console_scripts": ["identinum = identinum.cli:main"]},
)
