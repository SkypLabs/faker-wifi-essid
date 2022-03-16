=============
Documentation
=============

The documentation is written with `Sphinx`_ and is available in the `docs`
folder.

Install the dependencies
------------------------

The dependencies required to build the documentation are defined in `setup.py`
as an optional dependency group called `docs`.

To install the dependencies in `docs`:

::

   pip3 install .[docs]


Build the documentation
-----------------------

Sphinx provides a `Makefile` to build the documentation easily. Several output
formats are available.

For example, to build the documentation in HTML:

::

   cd docs/
   make html

The documentation website will be available in `docs/_build/html`.

To see the full list of the supported output formats, just execute `make`
without any specific target.

.. _Sphinx: https://www.sphinx-doc.org
