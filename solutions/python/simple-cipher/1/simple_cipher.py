import random

from string import ascii_lowercase


class Cipher(object):
    def __init__(self, key=None):
        self.key = key or ''.join([random.choice(ascii_lowercase) for i in range(100)])

    def encode(self, text):
        if len(text) > len(self.key):
            self.key = self.key * (round(len(text) / len(self.key)) + 1)
        positions = [ascii_lowercase.index(i) for i in self.key]
        encoded = ''
        for ix, letter in enumerate(text):
            if ascii_lowercase.index(letter) + positions[ix] <= 25:
                encoded += ascii_lowercase[ascii_lowercase.index(letter) + positions[ix]]
            else:
                encoded += ascii_lowercase[ascii_lowercase.index(letter) + positions[ix] - 26]
        return encoded


    def decode(self, text):
        positions = [ascii_lowercase.index(i) for i in self.key]
        decoded = ''
        for ix, letter in enumerate(text):
            if ascii_lowercase.index(letter) - positions[ix] >= 0:
                decoded += ascii_lowercase[ascii_lowercase.index(letter) - positions[ix]]
            else:
                decoded += ascii_lowercase[26 + ascii_lowercase.index(letter) - positions[ix]]
        return decoded
