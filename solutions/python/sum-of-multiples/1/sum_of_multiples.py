def sum_of_multiples(limit, multiples):
    all_multiples = set()

    if len(multiples) == 0:
        return 0

    if all([x == 0  for x in multiples]):
        return 0

    for i in range(limit):
        for m in multiples:
            if i >= m and m:
                if not i % m:
                    all_multiples.add(i)

    return sum(all_multiples)
