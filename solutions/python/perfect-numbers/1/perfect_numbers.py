def calculate_divisors(number):
    divisors = {1}
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0 and i not in divisors:
            divisors.add(i)
            divisors.add(number / i)
    return divisors


def classify(number):
    if number <= 0 or not isinstance(number, int):
        raise ValueError("Number must be a positive integer!") 
    divisors = calculate_divisors(number)
    if sum(divisors) < number or len(divisors) == 1:
        return "deficient"
    elif sum(divisors) == number:
        return "perfect"
    elif sum(divisors) > number:
        return "abundant"

