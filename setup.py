#! /usr/bin/env python

from setuptools import setup
import sys, re, logging

version = ''
with open('mediacloud/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)

setup(name='mediacloud',
    version=version,
    description='MediaCloud API Client Library',
    setup_requires=['setuptools-markdown'],
    long_description_markdown_filename='README.md',
    author='Rahul Bhargava',
    author_email='rahulb@media.mit.edu',
    url='http://mediacloud.org',
    packages={'mediacloud'},
    package_data={'':['LICENSE']},
    install_requires=['requests'],
    license='MIT',
    zip_safe=False,
    extras_require={'db': ['pymongo']}
)
