import re


class EmailSheilding:

    def __init__(self, input):
        self.input = input

    def shield(self):
        return re.sub(r'(.+)(?=@)', self.replacer, self.input)

    def replacer(self, match):
        regex_result = match.group()
        return ''.join(['x' for i in regex_result])
