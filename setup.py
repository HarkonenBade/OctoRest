#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name='octoclient',
    version='0.1.dev1',
    description='Client library for OctoPrint REST API',
    long_description=''.join(open('README.rst').readlines()),
    keywords='octoprint, 3d printing',
    author='Miro Hrončok',
    author_email='miro@hroncok.cz',
    license='MIT',
    url='https://github.com/hroncok/octoclient',
    packages=[p for p in find_packages() if p != 'test'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries',
        ]
)