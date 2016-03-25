#!/usr/bin/env python3

from distutils.core import setup

setup(
      name='GitHubFav',
      version='1.0',
      description='Tool for getting the favourite programming language' +
      'for a GitHub username',
      author='Andrew Barrett-Sprot',
      author_email='abarrettsprot+setup@gmail.com',
      packages=['githubfav'],
      license='BSD',
      install_requires=[
          'nose',  # Test suite, doesn't get used but its here to force you to have it
          'github3'  # github wrapper for python, so I don't need to handle authentication
          ]
)
