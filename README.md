# GitFav
A system that tells you what a users favourite language is. This project is written in Python

## How it works
This script searches through through all a given users pushes, counts the language of each changed file,
and assigns that push as the most common language based on the files changed. (It's assumed that your favourite language is the
 language you author the most commits with). It won't be 100% correct but it should be better than just looking at the number of
 files in each repository of the user.

# Installation
To install this program all you need to do is enter

    pip install -e GitHubFav

in your terminal when you are in the same directory as this readme

to run the unit tests you just need to run 

    nosetests tests/tests.py
