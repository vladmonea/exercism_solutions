import re

def abbreviate(words):
    abbreviation = []
    words = re.findall(r"[a-zA-Z_']+", words.replace('_', '').upper())
    for word in words:
        abbreviation.append(word[0])
    return "".join(abbreviation)

