#!/usr/bin/env python3

from distutils.core import setup

package_name = 'notification-mount'
version = '1.0.1'

setup(
        name = package_name,
        version = version,
        description = 'Script to show notification for a block device with mount action',
        author = 'Patrick Ziegler',
        author_email = 'p.ziegler96 at gmail dot com',
        url = 'https://github.com/patrick96/' + package_name, 
        download_url = 'https://github.com/patrick96/' + package_name + '/tarball/v' + version, 
        keywords = ['mount', 'notification'], 
        license = 'GPLv3',
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
        scripts = ["notification-mount"],
        )
