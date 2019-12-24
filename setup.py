#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os

from setuptools import setup, find_packages


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding="utf-8").read()


setup(
    name="pytest-pylenium",
    version="0.1.0",
    author="Simon Kerr",
    author_email="jackofspaces@gmail.com",
    maintainer="Simon Kerr",
    maintainer_email="jackofspaces@gmail.com",
    license="Apache Software License 2.0",
    url="https://github.com/symonk/pylenium",
    description="Boilerplate-less, stable end2end testing for web applications",
    long_description=read("README.md"),
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["pytest>=5.3.0"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
    ],
    entry_points={"pytest11": ["pylenium = pylenium.plugin", ], },
)
