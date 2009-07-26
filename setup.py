#!/usr/bin/env python

import os
from distutils.core import setup
import finaloption

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def desc():
    info = read('README')
    try:
        return info + '\n\n' + read('docs/changelog.rst')
    except IOError:
        # no docs
        return info

setup(
    name = 'finaloption',
    description = 'command line parsing done right',
    long_description = desc(),
    version = finaloption.__version__,
    author = finaloption.__author__,
    author_email = finaloption.__email__,
    url = 'http://hg.piranha.org.ua/finaloption/',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
        ],
    py_modules = ['finaloption'],
    )
