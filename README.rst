========
Overview
========

Symbol Soup is a framework for generating, converting, and bundling symbols (and footprints) used in technical drawings
and CAD applications.

* Free software: MIT license

Installation
============

::

    pip install symbol-soup

You can also install the in-development version with::

    pip install git+ssh://git@1/dcoon/symbol-soup.git@main

Documentation
=============


https://symbol-soup.readthedocs.io/


Development
===========

To run all the tests run::

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
