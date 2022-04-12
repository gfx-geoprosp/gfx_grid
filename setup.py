#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'geopandas>=0.10.2',
    'Shapely>=1.8.0',
]

test_requirements = ['pytest>=3', ]

setup(
    author="Jatmika Teja",
    author_email='jatmikatejasukmana@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="GFX Grid Generator",
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='gfx_grid',
    name='gfx_grid',
    packages=find_packages(include=['gfx_grid', 'gfx_grid.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/thejatmik/gfx_grid',
    version='1.2.0',
    zip_safe=False,
)
