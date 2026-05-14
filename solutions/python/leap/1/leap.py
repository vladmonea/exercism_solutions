def is_leap_year(year):
    try:
        if not year % 4 and year % 100 or not year % 400:
            return True
        return False
    except TypeError:
        raise TypeError("Please enter an integer or a floating point number.")