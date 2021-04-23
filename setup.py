#! /usr/bin/env python3

from setuptools import setup

import sys

if sys.version_info < (3, 7):
    # Prevent installation in older Python versions
    sys.exit("Sorry, Python < 3.7 is not supported.")

setup(
    name="voc",
    version="0.0.1",
    python_requires=">3.7.0",
    description="VOLT command line tools",
    entry_points={
        "console_scripts": [
            "voc_extract = voc:extract",
            "voc_merge = voc:merge",
            "voc_parse = voc:parse",
        ]
    },
    author="Jens Kutilek",
    url="https://www.kutilek.de/",
    packages=["voc"],
    package_dir={"": "Lib"},
    install_requires=["fontTools[woff,unicode,lxml]"],
)
