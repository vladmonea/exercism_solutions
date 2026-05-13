import string


def verify(isbn):
    isbn = list(isbn.replace('-', ''))
    if len(isbn) != 10:
        return False
    result = 0
    non_valid_chars = 'abcdefghijklmnopqrstuvwyz' + string.punctuation
    for i, l in enumerate(isbn):
        if l.lower() in non_valid_chars:
            return False
        if l.lower() == 'x':
            if i < 9:
                return False
            result += 10 * (10 - i)
        else:
            result += int(l) * (10 - i)
    return not result % 11