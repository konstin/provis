# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt', 'r') as reqs:
    requirements = reqs.read().split()

setup(
    name='provis',
    packages=find_packages(),
    version='0.0.1',
    install_requires=requirements,
)
