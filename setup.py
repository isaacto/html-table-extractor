#!/usr/bin/python
# -*- coding: utf-8 -*-

"""A tool to extract data from html table

See:
https://github.com/yuanxu-li/html-table-extractor
"""

import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read() + '\n'

setup(
    name='isaacto-html-table-extractor',
    url='https://github.com/isaacto/html-table-extractor',
    version='1.4.0.1',
    author='Isaac To',
    author_email='isaac.to@gmail.com',
    description='A python library for extracting data from html table',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='html table beautifulsoup crawler scrape',
    packages=[
        'html_table_extractor',
    ],
    install_requires=[
        'beautifulsoup4>=4.0.0',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
)
