import re


class PhoneNumberShielding:

    def __init__(self, input, symbol, number):
        self.input = input
        self.symbol = symbol
        self.number = number

    def shield(self):
        phone_number = self.input.replace(' ', '')
        pattern = '[0-9]{' + str(self.number) + '}$'
        result = re.sub(pattern, self.replacer, phone_number)
        return '+7' + self.format_phone_number(result)

    def replacer(self, match):
        regex_result = match.group()
        return ''.join([self.symbol for i in regex_result])

    def format_phone_number(self, number):
        return ' '.join([number[i:i+3] for i in range(-1, len(number), 3)])
