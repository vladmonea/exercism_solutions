def primes(limit):
    if limit <= 1:
        return []
    prime_nums = []
    marked = []
    for i in range(2, limit + 1):
        if i in marked:
            continue
        prime_nums.append(i)
        for j in range(i + 1, limit + 1):
            if j % i == 0:
                marked.append(j)
    return prime_nums

