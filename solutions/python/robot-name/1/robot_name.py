import random

from string import ascii_uppercase

NUMBERS = "1234567890"


class Robot(object):

    def __init__(self):
        self.name = self._generate_name()

    def _generate_name(self):
        return self._generate_random_chars(str, 2) + self._generate_random_chars(int, 3)

    def _generate_random_chars(self, char_type, char_num):
        if char_type == str:
            characters = ascii_uppercase
        if char_type == int:
            characters = NUMBERS

        res = ''
        for i in range(char_num):
            res += random.choice(characters)

        return res

    def reset(self):
        random.seed(self.name)
        self.name = self._generate_name()
