def check_number(func):
    def wrap(number):
        """I don't like repeating code everywhere"""
        if number < 1:
            raise ValueError('Number has to be positive!')
        if number == 1:
            return 1
        return func(number)
    return wrap


@check_number
def square_of_sum(number):
    s = number * (number + 1) / 2
    return s * s


@check_number
def sum_of_squares(number):
    s = 0
    for i in range(1, number+1):
        s += i * i
    return s


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)

