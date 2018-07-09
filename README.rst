=================
Faker Wi-Fi ESSID
=================

`Faker <https://github.com/joke2k/faker/>`__ provider for Wi-Fi ESSIDs.

Usage
=====

.. code-block:: python

    from faker import Faker
    from faker_wifi_essid import WifiESSID

    fake = Faker()
    fake.add_provider(WifiESSID)

    fake.wifi_essid()

License
=======

`MIT <https://opensource.org/licenses/MIT>`__
