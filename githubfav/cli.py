#!/usr/bin/env python
from github3 import login
from .githubfav import GitHubFav
import getpass


# Prompt for two factor authentication
def prompt_for_tfa():
    code = ''
    while not code:
        code = input('Two Factor Authentication code: ')
    return code


class CommandLineInterface:
    def main(self):
        print("As this program gets all of your known commits, it will need to make lots of requests.\n"
              "GitHub's rate limiting is very vicious unless you're logged in, so please log into GitHub")
        usr = input("GitHub username: ")
        tfa = input("Do you have Two Factor Authentication enabled on Github? ")
        if 'y' in tfa.lower():
            print("Turns out it's impossible to get a non-web application to handle two factor authentication for github.")
            print("Please go to https://github.com/settings/tokens and generate a token to paste in here")
            token = input("Access Token: ")
            session = login(usr, token=token)
        else:
            pwd = getpass.getpass()
            session = login(usr, pwd)

        print("Logged in!")
        ghf = GitHubFav(session)
        while True:
            user = input("Please enter a username to get the commits for:")
            print("Getting commits...")
            print(ghf.get_all_commits(user))

if __name__ == "__main__":
    cli = CommandLineInterface()
    cli.main()
