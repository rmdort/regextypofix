#!/usr/bin/env python

from distutils.core import setup

setup(
    name='regextypofix',
    version='1.0.4',

    # PyPI metadata
    author='Vinay M',
    author_email='rmdort@gmail.com',
    url='https://github.com/rmdort/regextypofix',
    download_url='https://pypi.python.org/pypi/regextypofix/',
    license='MIT, CC-BY-SA',
    description='Simple Regex spellchecker based on Wikipedia\'s RegExTypoFix project',
    long_description=open('Readme.rst').read(),
    platforms='any',
    keywords='typo spelling grammar text',
    classifiers=[
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        # Until we have a test suite we're conservative about Python version compatibility claims
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Documentation',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Text Processing :: Filters',
    ],

    # Installation settings
    packages=['regextypofix'],
    entry_points={'console_scripts': ['regextypofix = regextypofix.main:correct']},
    package_data={
        '': ['typos/*.txt']
    },
    install_requires=[
        'regex>=2016.07.14'
    ]
)