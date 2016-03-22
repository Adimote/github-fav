import github3
from .commitparser import CommitParser


class GitHubFav():
    def __init__(self, github3_login: github3.GitHubEnterprise):
        self.gh = github3_login

    def get_commit_list(self, user):
        commits = []
        user = self.gh.user(login=user)
        for event in filter(lambda x: x.type == "PushEvent", user.iter_events()):
            commits = commits + event.payload["commits"]
        return commits

    def get_commit(self, commit_dict):
        url = commit_dict["url"]
        # Do a bit of API wrangling, as the github3 api doesn't support loading individual commits
        print("Getting commit")
        response = self.gh._get(url)
        return response.json()

    def get_all_commits(self, user):
        commits = self.get_commit_list(user)
        for commit in commits:
            print(CommitParser.get_file_endings(CommitParser.get_files(self.get_commit(commit))))
