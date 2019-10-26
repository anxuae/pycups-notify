#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from io import open
import os.path as osp
from setuptools import setup, find_packages


HERE = osp.abspath(osp.dirname(__file__))
sys.path.insert(0, HERE)
import cups_notifier


def main():
    setup(
        name="pycups-notifier",
        version=cups_notifier.__version__,
        description=cups_notifier.__doc__,
        long_description=open(osp.join(HERE, 'README.rst'), encoding='utf-8').read(),
        long_description_content_type='text/x-rst',
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Other Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Natural Language :: English',
            'Topic :: Printing',
        ],
        author="Antoine Rousseaux",
        url="https://github.com/anxuae/pycups-notifier",
        download_url="https://github.com/anxuae/pycups-notifier/archive/{}.tar.gz".format(cups_notifier.__version__),
        license='MIT license',
        platforms=['unix', 'linux'],
        keywords=[
            'printer',
            'CUPS',
        ],
        packages=find_packages(),
        package_data={
        },
        include_package_data=True,
        install_requires=[
            'pycups>=1.9.73'
        ],
        options={
            'bdist_wheel':
                {'universal': True}
        },
        zip_safe=False,  # Don't install the lib as an .egg zipfile
        entry_points={'console_scripts': ["pycups-notifier = cups_notifier.subscriber:main"]},
    )


if __name__ == '__main__':
    main()
