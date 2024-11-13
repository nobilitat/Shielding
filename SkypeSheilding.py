import re


class SkypeSheilding:

    def __init__(self, input):
        self.input = input

    def shield(self):
        pattern = r'(?<=skype:).+(?=\?)|(?<=skype:).+'
        result = re.sub(pattern, replacer, self.input)
        return result


def replacer(match):
    regex_result = match.group()
    return ''.join(['x' for i in regex_result])
