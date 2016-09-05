#!/usr/bin/env python3

import os
from distutils.core import setup

package_name = 'notification-mount'

if not os.path.exists(package_name):
    os.makedirs(package_name)

setup(
        name = package_name,
        packages = [package_name], # this must be the same as the name above
        version = '1.0.2',
        description = 'Script to show notification for a block device with mount action',
        author = 'Patrick Ziegler',
        author_email = 'p.ziegler96 at gmail dot com',
        url = 'https://github.com/patrick96/' + package_name, # use the URL to the github repo
        download_url = 'https://github.com/patrick96/' + package_name + '/tarball/v1.0.0', # I'll explain this in a second
        keywords = ['mount', 'notification'], # arbitrary keywords
        classifiers = [
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3 :: Only',
            'Environment :: Console',
            'Intended Audience :: End Users/Desktop',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Natural Language :: English',
            'Topic :: Utilities'
            ],
        scripts = ["notification-mount.py"]
        )
