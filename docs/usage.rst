=====
Usage
=====

Just like with any other Faker provider, to use Faker Wi-Fi ESSID, you need to:

1. Import Faker and Faker Wi-Fi ESSID.
2. Create an instance of Faker.
3. Add :py:class:`faker_wifi_essid.WifiESSID` to the Faker instance.
4. Call :py:meth:`faker_wifi_essid.WifiESSID.wifi_essid` or any other relevant
   method.

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
