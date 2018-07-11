# -*- coding: utf-8 -*-

from faker.providers import BaseProvider

class WifiESSID(BaseProvider):
    """
    A Faker provider for Wi-Fi ESSIDs.
    """

    # Based on https://wigle.net/stats#ssidstats.
    common_essids = (
        '3Com',
        'Airport_Free_WiFi_AENA',
        'AndroidAP',
        'AndroidTether',
        'eduroam',
        'Exhibitor Internet',
        'FBI Surveillance Van',
        'freeBestBuywifi',
        'freebox',
        'Free Internet Access',
        'Free Public WiFi',
        'FRITZ!Box',
        'FRITZ!Box Fon WLAN',
        'FRITZ!Box Guest Access',
        'GetYourOwn',
        'get your own WiFi',
        'GuestAccess',
        'Guest Network',
        'GuestWiFi',
        'GuestWireless',
        'H&M Free WiFi',
        'Home Network',
        'Home Sweet Home',
        'Horizon Wi-Free',
        'KFC Free WiFi',
        'McDonalds Free WiFi',
        'MGMResorts-WiFi',
        'Moscow_WiFi_FREE',
        'NETGEAR-5G-GUEST',
        'Neuf WiFi',
        'Nordstrom_Wi-Fi',
        'Radisson_Guest',
        'Rostelecom',
        'SFR WiFi Public',
        'Starbucks WiFi',
        'Swisscom_Auto_Login',
        'visitors',
        'Vodafone Homespot',
        'Vodafone Hotspot',
        'Vodafone-Guest',
        'Welcome',
    )

    def common_essid(self):
        """
        Returns a random ESSID from a list of the most
        commonly used ones.
        See https://wigle.net/stats#ssidstats.
        """

        return self.random_element(self.common_essids)

    def upc_default_essid(self):
        """
        Generates a random ESSID similar to the default ones
        used by UPC.
        See https://deadcode.me/blog/2016/07/01/UPC-UBEE-EVW3226-WPA2-Reversing.html.
        """

        return "UPC" + str(self.random_number(7, True))

    def bbox_default_essid(self):
        """
        Generates a random ESSID similar to the default ones
        used by Bouygues Telecom's Bbox.
        """

        return self.hexify("Bbox-^^^^^^", upper=True)

    # List of the different ESSID generators.
    essid_generators = [
        bbox_default_essid,
        common_essid,
        upc_default_essid,
    ]

    def wifi_essid(self):
        """
        Returns a random fake Wi-Fi essid.
        """

        return self.random_element(self.essid_generators)(self)
