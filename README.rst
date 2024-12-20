=================
Faker Wi-Fi ESSID
=================

|PyPI Package| |PyPI Downloads| |PyPI Python Versions| |Build Status|

`Faker <https://github.com/joke2k/faker/>`__ provider for Wi-Fi ESSIDs.

.. image:: docs/_static/img/faker_wifi_essid_demo.gif
   :target: https://asciinema.org/a/191287
   :alt: Faker Wi-Fi ESSID - Demo

Usage
=====

.. code-block:: python

   # Import Faker.
   from faker import Faker
   # Import the WifiESSID class from Faker Wi-Fi ESSID.
   from faker_wifi_essid import WifiESSID

   # Create an instance of Faker.
   fake = Faker()
   # Add Faker Wi-Fi ESSID to the Faker providers.
   fake.add_provider(WifiESSID)

   # Call 'wifi_essid()' to get a random fake Wi-Fi ESSID.
   fake.wifi_essid()

License
=======

This project is `MIT <https://opensource.org/license/MIT>`__ licensed.

.. |Build Status| image:: https://github.com/SkypLabs/faker-wifi-essid/actions/workflows/test_and_publish.yml/badge.svg?branch=develop
   :target: https://github.com/SkypLabs/faker-wifi-essid/actions/workflows/test_and_publish.yml?query=branch%3Adevelop
   :alt: Build Status

.. |PyPI Downloads| image:: https://img.shields.io/pypi/dm/faker-wifi-essid.svg?style=flat
   :target: https://pypi.org/project/faker-wifi-essid/
   :alt: PyPI Package Downloads Per Month

.. |PyPI Package| image:: https://img.shields.io/pypi/v/faker-wifi-essid.svg?style=flat
   :target: https://pypi.org/project/faker-wifi-essid/
   :alt: PyPI Package Latest Release

.. |PyPI Python Versions| image:: https://img.shields.io/pypi/pyversions/faker-wifi-essid.svg?logo=python&style=flat
   :target: https://pypi.org/project/faker-wifi-essid/
   :alt: PyPI Package Python Versions
