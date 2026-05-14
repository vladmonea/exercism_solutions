import re

def abbreviate(words):
    abbreviation = []
    words = re.findall(r"[a-zA-Z_']+", words)
    for word in words:
        abbreviation.append(word.replace('_', '')[0].upper())
    return "".join(abbreviation)

