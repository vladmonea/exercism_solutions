from datetime import timedelta

def add_gigasecond(birth_date):
    delta = timedelta(0, 10 ** 9 - 2)
    intermediate_day = delta + birth_date
    return intermediate_day + timedelta(0, 2)