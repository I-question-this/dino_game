#!/usr/bin/env python
"""The setup file for installing this as a module"""
import os
from setuptools import setup, find_packages

version_path = os.path.join(os.path.dirname(__file__), 'src/dino/version.py')
# Get current version
with open(version_path, 'r') as fin:
    exec(fin.read())

setup(
    version=str(__version__),
    setup_requires=[],
    test_require=[],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'dino = dino.main:main'
        ]
    }
)
