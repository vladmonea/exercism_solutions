def on_square(integer_number):
    if integer_number > 0 and integer_number <= 64:
        return 2 ** (integer_number - 1)
    raise ValueError(f"invalid input {integer_number}")


def total_after(integer_number):
    if integer_number > 0 and integer_number <= 64:
        return sum([on_square(i) for i in range(1, integer_number + 1)])
    raise ValueError(f"invalid input {integer_number}")
