# -*- coding: utf-8 -*-

"""
A Faker provider for Wi-Fi ESSIDs.
"""

from faker.providers import BaseProvider

from .common_essids import COMMON_ESSIDS


class WifiESSID(BaseProvider):
    """
    A Faker provider for Wi-Fi ESSIDs.
    """

    def common_essid(self):
        """
        Returns a random ESSID from a list of the most
        commonly used ones.
        See https://wigle.net/stats#ssidstats.
        """

        return self.random_element(COMMON_ESSIDS)

    def upc_default_essid(self):
        """
        Generates a random ESSID similar to the default ones
        used by UPC.
        https://deadcode.me/blog/2016/07/01/UPC-UBEE-EVW3226-WPA2-Reversing.html.
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
