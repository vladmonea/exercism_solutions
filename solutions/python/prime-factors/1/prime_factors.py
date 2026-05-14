def prime_factors(natural_number):
    if natural_number <= 0:
        raise ValueError('need a POSITIVE natural number')

    aux = natural_number
    prime_factors_list = []
    i = 2
    while i * i <= natural_number:
        if natural_number % i:
            i += 1
        else:
            natural_number //= i
            prime_factors_list.append(i)
    if natural_number > 1:
        prime_factors_list.append(natural_number)
    return prime_factors_list

