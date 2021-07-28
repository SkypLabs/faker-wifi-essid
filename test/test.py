# -*- coding: utf-8 -*-

"""
Unit tests written with the Python Unit testing framework.

Documentation: https://docs.python.org/3/library/unittest.html.
"""

import re
import unittest

from faker import Faker
from faker_wifi_essid import WifiESSID
from faker_wifi_essid.common_essids import COMMON_ESSIDS


class TestWifiESSID(unittest.TestCase):
    """
    Unit tests for the 'WifiESSID' class.
    """

    def setUp(self):
        self.fake = Faker()
        self.fake.add_provider(WifiESSID)

    def test_if_string(self):
        """
        Tests if the values returned by the fake Wi-Fi ESSID
        generators are strings.
        """

        for _ in range(10):
            self.assertTrue(isinstance(self.fake.common_essid(), str))
            self.assertTrue(isinstance(self.fake.upc_default_essid(), str))
            self.assertTrue(isinstance(self.fake.bbox_default_essid(), str))
            self.assertTrue(isinstance(self.fake.wifi_essid(), str))

    def test_common_essid(self):
        """
        Tests if the 'common_essid()' method returns values from
        'COMMON_ESSIDS' as expected.
        """

        for _ in range(10):
            self.assertTrue(self.fake.common_essid() in COMMON_ESSIDS)

    def test_upc_default_essid(self):
        """
        Tests if the values returned by the 'upc_default_essid()' method match
        the UPC ESSIDs' regex.
        """

        regex = re.compile(r"^UPC\d{7}$")

        for _ in range(10):
            self.assertTrue(re.match(regex, self.fake.upc_default_essid()))

    def test_bbox_default_essid(self):
        """
        Tests if the values returned by the 'bbox_default_essid()' method match
        the Bbox ESSIDs' regex.
        """

        regex = re.compile(r"^Bbox-[A-F0-9]{6}$")

        for _ in range(10):
            self.assertTrue(re.match(regex, self.fake.bbox_default_essid()))
