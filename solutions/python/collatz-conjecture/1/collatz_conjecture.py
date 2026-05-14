def collatz_steps(number):
    if number <= 0:
        raise ValueError('Number cannot be smaller than 1.')
    steps = 0
    while number > 1:
        steps += 1
        if number % 2:
            number = 3 * number + 1
        else:
            number /= 2
    return steps
