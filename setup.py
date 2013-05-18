#-*- coding: utf-8 -*-

"""
    opener
    ~~~~~

    Setup
    `````

    $ pip install .
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
        'whoosh >= 2.4.1',
        ],
    scripts=[
        "scripts/er"
        ],
    description="OpenER is an open entity resolution toolkit",
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
)
