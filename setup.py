""" setup.py - Script to install package using distutils

For help options run:
$ python setup.py --help

"""
# Author: elchinot7

from setuptools import setup
from stupify import stupify

VERSION = stupify.__version__

setup_args = dict(name='stupify',
                  version=VERSION,
                  author='elchinot7',
                  author_email='efraazul@gmail.com',
                  url='https://github.com/elchinot7/spotify_control.py',
                  packages=['stupify'],
                  scripts=['stupify/stupify.py'],
                  package_data={},
                  license="Modified BSD license",
                  description="""stupify extracts info from Spotify client using
                                D-bus.""",
                  long_description=open('README.rst').read(),
                  classifiers=["Topic :: Utilities",
                               "Intended Audience :: Music/tools",
                               "License :: OSI Approved :: BSD License",
                               "Operating System :: OS Independent",
                               "Programming Language :: Python",
                               "Programming Language :: Python :: 2.7",
                               ],
                  install_requires=[],
                  )

if __name__ == "__main__":
    setup(**setup_args)
