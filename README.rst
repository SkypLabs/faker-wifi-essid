=================
Faker Wi-Fi ESSID
=================

|PyPI Package| |Build Status| |Code Coverage|

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

.. |Build Status| image:: https://travis-ci.org/SkypLabs/faker-wifi-essid.svg
   :target: https://travis-ci.org/SkypLabs/faker-wifi-essid
   :alt: Build Status
.. |Code Coverage| image:: https://api.codacy.com/project/badge/Grade/81340af8ccae48fea7ecede19a2d8cfa
   :target: https://www.codacy.com/app/skyper/faker-wifi-essid?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=SkypLabs/faker-wifi-essid&amp;utm_campaign=Badge_Grade
   :alt: Code Coverage
.. |PyPI Package| image:: https://badge.fury.io/py/faker-wifi-essid.svg
   :target: https://badge.fury.io/py/faker-wifi-essid
   :alt: PyPI Package
