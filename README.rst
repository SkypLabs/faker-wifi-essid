=================
Faker Wi-Fi ESSID
=================

|PyPI Package| |Build Status|

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

`MIT <https://opensource.org/licenses/MIT>`__

.. |Build Status| image:: https://github.com/SkypLabs/faker-wifi-essid/actions/workflows/test.yml/badge.svg?branch=develop
   :target: https://github.com/SkypLabs/faker-wifi-essid/actions/workflows/test.yml
   :alt: Build Status
.. |PyPI Package| image:: https://badge.fury.io/py/faker-wifi-essid.svg
   :target: https://badge.fury.io/py/faker-wifi-essid
   :alt: PyPI Package
