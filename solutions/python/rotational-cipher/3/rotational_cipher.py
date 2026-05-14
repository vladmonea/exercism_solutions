import string


def rotate(text, key):
    if key == 0:
        return text

    ciphertext = []

    for char in text:
        if char.isupper():
            pos = string.ascii_uppercase.index(char)
            new_char = string.ascii_uppercase[(pos + key) % 26]
        elif char.islower():
            pos = string.ascii_lowercase.index(char)
            new_char = string.ascii_lowercase[(pos + key) % 26]
        else:
            new_char = char
        ciphertext.append(new_char)
    return "".join(ciphertext)
