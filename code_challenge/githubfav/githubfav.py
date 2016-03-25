import github3
from github3 import login
from .commitparser import CommitParser
from .languages import extension_to_language


class GitHubFav:
    class NotLoggedInException(Exception):
        pass

    class HTTPException(Exception):
        pass

    # How many commits of the user to check.
    COMMIT_COUNT = 50
    COMMITS_PER_PUSH = 3

    def __init__(self, github3_login: github3.GitHubEnterprise):
        if github3_login:
            self.gh = github3_login
            try:
                # Check for if the login succeeded
                self.logged_in_user = self.gh.user()
            except github3.models.GitHubError as e:
                if e.code == 401:
                    raise self.NotLoggedInException("Bad Login!")
        else:
            self.gh = login(username="invalid",password="invalid")

    def get_push_list(self, user):
        user = self.gh.user(login=user)
        # If the user doesn't exist
        if user is None:
            return None
        return filter(lambda x: x.type == "PushEvent", user.iter_events())

    def get_commit(self, commit_dict):
        url = commit_dict["url"]
        # Do a bit of API wrangling, as the github3 api doesn't support loading individual commits
        response = self.gh._get(url)
        if response.status_code > 400:
            print("x", end="", flush=True)
            raise self.HTTPException("Error when getting commit")
        print(".", end="", flush=True)
        return response.json()

    @staticmethod
    def get_favourite_lang(list_of_endings):
        freq = {}
        for ending in list_of_endings:
            if ending not in freq:
                freq[ending] = 1
            else:
                freq[ending] += 1

        return sorted(freq.items(), key=lambda x: x[1], reverse=True)

    def get_all_commits(self, user):
        pushes = self.get_push_list(user)
        if pushes is None:
            return None

        most_common_endings = []

        for push in pushes:
            commits = push.payload["commits"][:self.COMMITS_PER_PUSH]
            endings = []
            for commit in commits:
                try:
                    endings += CommitParser.get_file_endings(
                        CommitParser.get_files(
                            self.get_commit(commit)
                        )
                    )
                except self.HTTPException:
                    pass
            print("|", end="", flush=True)
            # Most common endings
            most_common_endings += CommitParser.get_mode_endings(endings)

        print()
        languages = [(extension_to_language(x)) for x in most_common_endings]
        return self.get_favourite_lang(languages)
