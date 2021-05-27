#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
import re

from setuptools import setup, find_packages


with open('src/epub_thumbnailer.py', 'r') as fh:
    version = re.search(r'__version__ *= *(["\'])(.*?[^\\])\1', fh.read()).group(2)


with open("README.md", "r") as fh:
    long_description = fh.read()


with open("requirements.txt", "r") as fh:
    requirements = []
    for line in fh.readlines():
        line = line.strip()
        if line and not line.startswith('#'):
            requirements.append(line)


setup(
    name='epub_thumbnailer',
    version=version,
    package_dir={'':'src'},
    #packages=find_packages("src", exclude=['test*']),
    py_modules=["epub_thumbnailer"],
    entry_points={
        'console_scripts': [
            'epub-thumbnailer = epub_thumbnailer:main',
        ],
        'setuptools.installation': [
            'eggsecutable = epub_thumbnailer:main'
        ],
    },
#    test_suite="test",
    install_requires=requirements,
    zip_safe=True,

    # Various MIME files that need to be copied to certain system locations on Linux.
    # Note that these files are only installed correctly if
    # --single-version-externally-managed is used as argument to "setup.py install".
    # Otherwise, these files end up in a MComix egg directory in site-packages.
    # (Thank you, setuptools!)
    data_files=[
    	('share/thumbnailers', ['src/epub.thumbnailer']),
    ],

    # Package metadata
    author='Mariano Simone',
    author_email='marianosimone@users.noreply.github.com',
    maintainer='Mariano Simone',
    maintainer_email='marianosimone@users.noreply.github.com',
    url='https://github.com/marianosimone/epub-thumbnailer',
    description='A simple script that tries to find a cover into an epub file and creates a thumbnail for it.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    platforms=[
        'Operating System :: POSIX :: Linux',
    ],
)
