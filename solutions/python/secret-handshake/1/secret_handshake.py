# decided that the dict should only hold the exponents
# it makes it easier for the way i've set up the loop

handshake = {
    0 : 'wink',
    1 : 'double blink',
    2: 'close your eyes',
    3: 'jump',
    4: 'reverse',
}


def commands(number):
    secret_handshake = []
    bin_num = bin(number)[2:]
    for i, v in enumerate(bin_num[::-1]):
        if v == '1':
            sequence = handshake[i]
            if sequence == 'reverse':
                secret_handshake = secret_handshake[::-1]
            else:
                secret_handshake.append(sequence)
    return secret_handshake

