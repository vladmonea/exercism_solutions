def is_isogram(string):
    string = string.replace('-', '').lower()
    string = string.replace(' ', '')
    return len(string) == len(set(string))