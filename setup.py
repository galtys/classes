# Copyright (c) 2014, Facebook, Inc.  All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.
#
from setuptools import setup, find_packages

NAME = 'classes'
VERSION = '0.4.1'

setup(
    name=NAME,
    version=VERSION,
    py_modules=['classes'],
    description="type classes",

    author='Jan Troler',
    author_email='jan.troler@galtys.com',
    license='MIT',
    keywords='utils',
    url='http://github.com/galtys/classes',
    #download_url='https://github.com/galtys/classes/%s.tar.gz' % VERSION,
    classifiers=[
        "Development Status :: 0 - Development/Unstable",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
    ],
)
