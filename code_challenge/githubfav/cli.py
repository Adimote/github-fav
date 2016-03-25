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
        ghf = self.login_loop()
        while True:
            try:
                self.query_loop(ghf)
            except GitHubFav.NotLoggedInException:
                print("Your login has become invalid!")
                ghf = self.login_loop()

    @staticmethod
    def query_loop(ghf):
        while True:
            user = input("Please enter a username to get the commits for: ")
            print("Getting commits for each push the user has made...")
            print("Key: '|': Github Push Event; '.': Commit; 'x': Commit that doesn't exist / failed to get")
            results = ghf.get_all_commits(user)
            if results is None:
                print("That user doesn't exist!")
            if len(results) > 0:
                language = results[0][0]
                push_count = results[0][1]
                plural = "es" if push_count > 1 or push_count == 0 else ""
                print("This User's favourite language is: {} with {} push{}".format(language, push_count, plural))
            if len(results) > 1:
                for i, result in enumerate(results):
                    language = result[0]
                    push_count = result[1]
                    plural = "es" if result[1] > 1 or result[1] == 0 else ""
                    print("{}: '{}' with {} push{}".format(i+1, language, push_count, plural))

    @staticmethod
    def login_loop():
        logged_in = False
        while not logged_in:
            usr = input("GitHub username: ")
            if usr == "":
                print("Username cannot be blank")
                continue
            tfa = input("Do you have Two Factor Authentication enabled on Github? ")
            if 'y' in tfa.lower():
                print(
                    "Turns out it's impossible to get a non-web application to handle two factor authentication for github.")
                print("Please go to https://github.com/settings/tokens and generate a token to paste in here")
                token = input("Access Token: ")
                session = login(usr, token=token)
            else:
                pwd = getpass.getpass()
                if pwd == "":
                    print("Password cannot be blank")
                    continue
                session = login(usr, pwd)
            try:
                ghf = GitHubFav(session)
                logged_in = True
            except GitHubFav.NotLoggedInException:
                print("Login Credentials invalid!")
        print("Logged in!")
        return ghf


if __name__ == "__main__":
    cli = CommandLineInterface()
    cli.main()
