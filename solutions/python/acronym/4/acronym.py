import re

def abbreviate(words):
    words = re.findall(r"[a-zA-Z_']+", words.replace('_', '').upper())
    return "".join(w[0] for w in words)

