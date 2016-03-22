import re


class CommitParser:
    # Regex to match everything past the last dot
    RE_FILE_ENDINGS = re.compile(r"^.*\.(.*?)$")

    @staticmethod
    def get_files(commit: dict):
        return commit["files"]

    @staticmethod
    def get_file_endings(files):
        names = [x["filename"] for x in files]
        endings = [re.match(CommitParser.RE_FILE_ENDINGS, x).group(1) for x in names]
        return endings

