# -*- coding: utf-8 -*-

import unittest

from faker import Faker
from faker_wifi_essid import WifiESSID

class TestWifiESSID(unittest.TestCase):
    def setUp(self):
        self.fake = Faker()
        self.fake.add_provider(WifiESSID)

    def test_if_string(self):
        essid = self.fake.wifi_essid()
        self.assertTrue(isinstance(essid, str))
