import string


def rotate(text, key):
    if key == 0:
        return text

    ciphertext = []

    for char in text:
        if char.isupper():
            pos = string.ascii_uppercase.index(char)
            char = string.ascii_uppercase[(pos + key) % 26]
        if char.islower():
            pos = string.ascii_lowercase.index(char)
            char = string.ascii_lowercase[(pos + key) % 26]
        ciphertext.append(char)
    return "".join(ciphertext)
