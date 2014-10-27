#!/usr/bin/env python

from setuptools import setup

setup(name='djeasyroute',
      version='0.0.1',
      description='A simple class based route system for django similar to flask',
      author='Ryan Goggin',
      author_email='info@ryangoggin.net',
      url='http://ryangoggin.net',
      download_url='',
      classifiers=[
            "Development Status :: 3 - Alpha",
            "Framework :: Django",
            "License :: OSI Approved :: MIT",
            "Operating System :: OS Independent",
            "Topic :: Software Development",
      ],
      install_requires=[
            'django',
      ],
      packages=[
            'djeasyroute',
      ],
)
