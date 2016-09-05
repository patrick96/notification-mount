#!/usr/bin/env python3

import os
from distutils.core import setup
import glob

package_name = 'notification-mount'
version = '1.0.0'

if not os.path.exists(package_name):
    os.makedirs(package_name)

setup(
        name = package_name,
        packages = [package_name], # this must be the same as the name above
        version = version,
        description = 'Script to show notification for a block device with mount action',
        author = 'Patrick Ziegler',
        author_email = 'p.ziegler96 at gmail dot com',
        url = 'https://github.com/patrick96/' + package_name, # use the URL to the github repo
        download_url = 'https://github.com/patrick96/' + package_name + '/tarball/v' + version, # I'll explain this in a second
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
        scripts = ["notification-mount.py"],
        data_files = [
            ('/usr/lib/systemd/user', ['examples/notification-mount.service']),
            ('/usr/share/' + package_name + '/examples', glob.glob("examples/*"))
            ]
        )
