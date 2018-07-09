# -*- coding: utf-8 -*-

from faker.providers import BaseProvider

class WifiESSID(BaseProvider):
    """
    A provider for Wi-Fi access points.
    """

    # Based on https://wigle.net/stats#ssidstats.
    common_names = (
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

    def wifi_essid(self):
        """
        Returns a fake Wi-Fi access point name.
        """

        return self.random_element(self.common_names)
