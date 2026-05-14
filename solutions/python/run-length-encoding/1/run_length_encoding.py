def decode(string):
    if not string:
        return ""
    message = ""
    freq = ""

    for i in range(len(string)):
        if string[i].isdigit():
            freq += string[i]
        if string[i].isalpha() or string[i] == " ":
            if freq:
                message += string[i] * int(freq)
            else:
                message += string[i]
            freq = ""

    return message


def encode(string):
    if not string:
        return ""
    ciphertext = ""
    count = 1
    current = string[0]

    for i in range(1, len(string)):
        if string[i] == current:
            count += 1
        else:
            if count > 1:
                count = str(count)
            else:
                count = ""
            ciphertext += count + current
            count = 1
            current = string[i]

    if count > 1:
        count = str(count)
    else:
        count = ""
    ciphertext += count + current

    return ciphertext
