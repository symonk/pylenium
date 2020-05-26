========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/pylenium/badge/?style=flat
    :target: https://readthedocs.org/projects/pylenium
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/symonk/pylenium.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/symonk/pylenium

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/symonk/pylenium?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/symonk/pylenium

.. |requires| image:: https://requires.io/github/symonk/pylenium/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/symonk/pylenium/requirements/?branch=master

.. |codecov| image:: https://codecov.io/gh/symonk/pylenium/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/symonk/pylenium

.. |version| image:: https://img.shields.io/pypi/v/pylenium.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/pylenium

.. |wheel| image:: https://img.shields.io/pypi/wheel/pylenium.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/pylenium

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pylenium.svg
    :alt: Supported versions
    :target: https://pypi.org/project/pylenium

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pylenium.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/pylenium

.. |commits-since| image:: https://img.shields.io/github/commits-since/symonk/pylenium/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/symonk/pylenium/compare/v0.0.0...master



.. end-badges

selenium wrapper placeholder

* Free software: ISC license

Installation
============

::

    pip install pylenium

You can also install the in-development version with::

    pip install https://github.com/symonk/pylenium/archive/master.zip


Documentation
=============


https://pylenium.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
