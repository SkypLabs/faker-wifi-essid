============
Installation
============

From PyPI (recommended)
-----------------------

To install Faker Wi-Fi ESSID from `PyPI`_ with pip:

.. code:: sh

    pip install --upgrade faker-wifi-essid

However, as Faker Wi-Fi ESSID is a programming library (a `module <Python
Modules>`_ in Python parlance), it is most likely to be added as a dependency
to the `pyproject.toml` file of your project or its equivalent configuration
file:

.. code:: toml

    dependencies = [
      "faker_wifi_essid",
    ]

From sources
------------

Faker Wi-Fi ESSID is packaged with `Setuptools`_.

The default Git branch is `develop`. To install the latest stable version, you
need to clone the `main` branch.

.. code:: sh

    git clone -b main https://github.com/SkypLabs/faker-wifi-essid.git
    cd faker-wifi-essid
    pip install .

.. _Python Modules: https://docs.python.org/3/tutorial/modules.html
.. _PyPI: https://pypi.org/
.. _Setuptools: https://pypi.org/project/setuptools/
