# GitFav
A system that tells you what a users favourite language is. This project is written in Python 3.

Currently it is a command line interface, but it wouldn't be hard to write a web-based solution

## How it works
This script searches through through all a given users pushes, counts the language of each changed file,
and assigns that push as the most common language based on the files changed. (It's assumed that your favourite language is the
 language you author the most commits with). It won't be 100% correct but it should be better than just looking at the number of
 files in each repository of the user.

# Installation
Remember this program is written in Python 3!

To install this program all you need to do is enter

    pip install -r requirements.txt


in your terminal when you are in the same directory as this readme.
(you may need to use `pip3` if you default to python 2)


# Running
## Unit Tests
to run the unit tests you just need to run

    nosetests tests/tests.py

again, make sure you're running the python 3 nosetests, or it will throw a syntax error


## Running the program
To run the program you just need to run

    python -m githubfav.cli

in the current directory.
