===========
Development
===========

Dropping support for deprecated Python versions
-----------------------------------------------

When a Python version is officially deprecated, it needs to be removed from the
versions supported by this package. To do so, the following actions need to be taken:

* In `setup.cfg`:

  * Remove the Python version from the classifiers.
  * Update the minimum supported Python version in `python_requires`.

* In `tox.ini`:

  * Remove the Python version from `tox.envlist`.
  * Remove the Python version from `gh-actions.python`.

* In `.github/workflows/test_and_publish.yml`:

  * Remove the Python version from the build matrix.

* In the GitHub repository settings:

  * If necessary, update the required status checks in the branch protection
    rules.

The status of the Python versions can be found `here
<https://devguide.python.org/versions/>`_.
