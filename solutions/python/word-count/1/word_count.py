from collections import Counter
from string import punctuation


def word_count(phrase):
    phrase_clean = ''
    punctuation_chars = punctuation.replace('_', '').replace(',',
        '').replace("'", '')
    for position, letter in enumerate(phrase):
        if letter in '_\t\n,':
            phrase_clean += ' '
        elif letter in punctuation_chars:
            phrase_clean += ''
        elif letter == "'":
            if phrase[position-1] == ' ' or phrase[position + 1] == ' ':
                phrase_clean += ''
            else:
                phrase_clean += letter
        else:
            phrase_clean += letter.lower()
    return dict(Counter(phrase_clean.split()))