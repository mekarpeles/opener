#-*- coding: utf-8 -*-

"""
    waltz
    ~~~~~

    Setup
    `````

    $ pip install waltz    
"""

from distutils.core import setup

setup(
    name='er',
    version='0.0.1',
    url='http://github.com/mekarpeles/opener',
    author='mek',
    author_email='michael.karpeles@gmail.com',
    packages=[
        'er',
        ],
    platforms='any',
    license='LICENSE',
    install_requires=[
    ],
    scripts=[
        "scripts/er"
        ],
    description="OpenER is an open entity resolution toolkit",
    long_description=open('README.md').read(),
)
