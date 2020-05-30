# -*- coding: utf-8 -*-

"""
Faker Wi-Fi ESSID provider.
"""

from pkg_resources import get_distribution

from .wifi_essid import WifiESSID

__version__ = get_distribution("faker_wifi_essid").version

__all__ = [
    "WifiESSID",
]
