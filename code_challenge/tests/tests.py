import json

from github3 import login
from nose.tools import *

from githubfav.commitparser import CommitParser
from githubfav.githubfav import GitHubFav


@raises(GitHubFav.NotLoggedInException)
def test_parse_invalid_login():
    GitHubFav(login(username="invalid", password="invalid"))


def test_counter():
    assert GitHubFav.get_favourite_lang(["a", "a", "b", "c", "a", "c"]) == [("a", 3), ("c", 2), ("b", 1)]


"""
 Test for the most common file ending
"""


def test_most_common():
    """
    Test for the most common file ending
    """
    assert set(CommitParser.get_mode_endings(["a", "a", "b", "c", "c", "d"])) == {"a", "c"}


"""
 TESTS for file parsing
"""


def test_file_endings_basic():
    """
    Tests that a file ending returns if there is a dot
    """
    assert CommitParser.get_file_ending("file.py") == "py"


def test_file_endings_no_dot():
    """
    Tests that a file ending returns if there's no dot
    """
    assert CommitParser.get_file_ending("file") == "file"


def test_file_endings_dot():
    """
    Tests that a file ending returns if it is a dot file
    """
    assert CommitParser.get_file_ending(".file") == "file"


def test_file_endings_directory():
    """
    Tests that a file ending returns if it is in a directory
    """
    assert CommitParser.get_file_ending("directory/file.py") == "py"


def test_file_endings_just_a_dot():
    """
    Tests that a file ending returns if it is a dot file in a directory
    """
    assert CommitParser.get_file_ending("directory/.gitignore") == "gitignore"


def test_file_endings_no_name():
    """
    Tests that a file ending returns if it has no dot and is in a directory
    """
    assert CommitParser.get_file_ending("directory/noExtension") == "noExtension"
