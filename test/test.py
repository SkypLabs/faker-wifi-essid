# -*- coding: utf-8 -*-

import re
import unittest

from faker import Faker
from faker_wifi_essid import WifiESSID

class TestWifiESSID(unittest.TestCase):
    def setUp(self):
        self.fake = Faker()
        self.fake.add_provider(WifiESSID)

    def test_if_string(self):
        for i in range(10):
            self.assertTrue(isinstance(self.fake.wifi_essid(), str))

    def test_common_essid(self):
        for i in range(10):
            self.assertTrue(self.fake.common_essid() in WifiESSID.common_essids)

    def test_upc_default_essid(self):
        r = re.compile("^UPC\d{7}$")

        for i in range(10):
            self.assertTrue(re.match(r, self.fake.upc_default_essid()))

    def test_bbox_default_essid(self):
        r = re.compile("^Bbox-[A-F0-9]{6}$")

        for i in range(10):
            self.assertTrue(re.match(r, self.fake.bbox_default_essid()))
