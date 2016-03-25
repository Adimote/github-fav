import re


class CommitParser:
    # Regex to match everything past the last dot
    RE_FILE_ENDINGS = re.compile(r"^.*\.(.*?)$")
    RE_DIR_ENDINGS = re.compile(r"^.*/(.*?)$")

    @staticmethod
    def get_files(commit: dict):
        return commit["files"]

    @staticmethod
    def get_file_ending(file):
        match = re.match(CommitParser.RE_FILE_ENDINGS, file)
        if match is None:
            # if the file has no extension, try getting the file name itself
            match = re.match(CommitParser.RE_DIR_ENDINGS, file)
            if match is None:
                # Otherwise the file must be a lone file in the root directory. return it.
                return file
            else:
                return match.group(1)
        else:
            return match.group(1)

    @staticmethod
    def get_file_endings(files):
        names = [x["filename"] for x in files]

        endings = [CommitParser.get_file_ending(x) for x in names]
        return endings

    @staticmethod
    def get_mode_endings(list_of_endings):
        """
        Get the most common file endings
        :param list_of_endings:
        :return: lists of the file endings which appear the most (will be a list if there's more than 1)
        """
        freq = {}
        highest = 0
        for ending in list_of_endings:
            if ending not in freq:
                newfreq = 1
            else:
                newfreq = freq[ending] + 1
            freq[ending] = newfreq
            highest = max(newfreq, highest)

        # Get all the line endings with the same frequency as the most frequent.
        return [x for x, y in freq.items() if y == highest]
