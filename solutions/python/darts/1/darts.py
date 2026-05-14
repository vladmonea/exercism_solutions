def score(x, y):
    pos = (x * x + y * y) ** 0.5
    if pos > 10:
        return 0
    elif pos > 5:
        return 1
    elif pos > 1:
        return 5
    else:
        return 10
