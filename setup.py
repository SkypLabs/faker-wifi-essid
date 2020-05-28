#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Setuptools build system configuration file
for Faker Wi-Fi ESSID.

See https://setuptools.readthedocs.io.
"""

from codecs import open as fopen
from os.path import dirname, abspath, join
from setuptools import setup, find_packages

DIR = dirname(abspath(__file__))

VERSION = "0.2.0"

URL = "https://github.com/SkypLabs/faker-wifi-essid"
DL_URL = URL + "/archive/v{0}.zip"

with fopen(join(DIR, "README.rst"), encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="faker_wifi_essid",
    version=VERSION,
    description="Faker provider for Wi-Fi ESSIDs.",
    long_description=LONG_DESCRIPTION,
    license="MIT",
    keywords="faker faker-library faker-provider faker-generator wifi essid",
    author="Paul-Emmanuel Raoul",
    author_email="skyper@skyplabs.net",
    url=URL,
    download_url=DL_URL.format(VERSION),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
    ],
    packages=find_packages(exclude=["docs", "tests", "tests.*"]),
    test_suite="test",
    install_requires=[
        "Faker",
    ],
)
