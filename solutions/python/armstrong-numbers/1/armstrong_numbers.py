def is_armstrong(number):
    exponent = 0
    digits = []
    initial = number
    while number:
        exponent += 1
        digits.append(number % 10)
        number //= 10
    armstrong = sum([d ** exponent for d in digits])

    return armstrong == initial