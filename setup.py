# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 23:55:29 2025

@author: naveenr
"""

# setup.py
from setuptools import setup, find_packages

setup(
    name='gee-toolkit',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'earthengine-api',
        'numpy',
        'click',
    ],
    entry_points={
        'console_scripts': [
            'gee-indices=gee_indices.main:cli',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A command-line tool to calculate vegetation indices using Google Earth Engine.',
    license='MIT',
    keywords='remote sensing gee vegetation indices sentinel',
    url='https://github.com/your-username/gee-indices',
)