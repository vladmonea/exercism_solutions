from string import ascii_lowercase, digits


encoding_map = dict(zip(ascii_lowercase + digits, ascii_lowercase[::-1] + digits))
decoding_map = dict(zip(ascii_lowercase[::-1] + digits, ascii_lowercase + digits))


def encode(plain_text):
    """Encode the plain text received and return a
    string of 5-character groups."""
    decoded_text = ""
    result = ""
    for c in plain_text.replace(" ", "").lower():
        encoded = encoding_map.get(c, c)
        if encoded in ascii_lowercase + digits:
            decoded_text += encoded
        else:
            continue

    for pos, c in enumerate(decoded_text):
        if (pos + 1) % 5:
            result += c
        else:
            result += c + " "

    return result.strip()


def decode(ciphered_text):
    """Decode the ciphered text and return a string"""
    result = ""
    for c in ciphered_text.replace(" ", ""):
        decoded = decoding_map.get(c, c)
        result += decoded
    return result

