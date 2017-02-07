#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'requests',
    'pandas',
    'ckanapi',
    'pyyaml',
    'xlrd',
    'xlwt',
    'lxml',
    'html5lib',
    'beautifulsoup4'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='ckan_loaddata',
    version='0.1.0',
    description="A utility for loading data into CKAN from remote sources",
    long_description=readme + '\n\n' + history,
    author="Tanzania Open Data Initiative",
    author_email='',
    url='https://github.com/WorldBank-Transport/ckan-loaddata',
    packages=[
        'ckan_loaddata',
    ],
    package_dir={'ckan_loaddata':
                 'ckan_loaddata'},
    entry_points={
        'console_scripts': [
            'ckan_loaddata=ckan_loaddata.cli:loaddata'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='ckan_loaddata',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
