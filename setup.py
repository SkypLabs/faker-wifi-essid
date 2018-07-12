#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from codecs import open as fopen
from os.path import dirname, abspath, join
from setuptools import setup, find_packages

VERSION = "0.2.0"

DIR = dirname(abspath(__file__))

with fopen(join(DIR, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'faker_wifi_essid',
    version = VERSION,
    description = 'Faker provider for Wi-Fi ESSIDs.',
    long_description = long_description,
    license = 'MIT',
    keywords = 'faker faker-library faker-provider faker-generator wifi essid',
    author = 'Paul-Emmanuel Raoul',
    author_email = 'skyper@skyplabs.net',
    url = 'https://github.com/SkypLabs/faker-wifi-essid',
    download_url = 'https://github.com/SkypLabs/faker-wifi-essid/archive/v{0}.zip'.format(VERSION),
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],
    packages = find_packages(exclude=['docs', 'tests', 'tests.*']),
    test_suite = 'test',
    install_requires = [
        'Faker',
    ],
)
