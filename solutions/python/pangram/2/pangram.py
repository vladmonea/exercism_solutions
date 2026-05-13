from string import ascii_lowercase


def is_pangram(sentence):
    # ascii_lowercase is the complete alphabet, but we need to account for the
    # space character too
    alphabet = set(ascii_lowercase)
    sentence_set = set(sentence.lower())
    if ' ' in sentence_set:
        sentence_set.remove(' ')
    return alphabet.intersection(sentence_set) == alphabet