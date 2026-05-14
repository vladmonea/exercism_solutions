def triplets_with_sum(sum_of_triplet):
    """Rather than using the three methods suggested by the
    problem skelethon code, it's easier to do a bit of algebra
    which led to the conclusion than only one of the triplet's
    members should be used in an iteration, while the other
    two can be infered later.
    The entire range of possible square values is computed as
    an optimisation.
    """
    squares = [i * i for i in range(sum_of_triplet)]
    results = set()
    for b in range(1, int(sum_of_triplet/2)):
        num = sum_of_triplet * sum_of_triplet - 2 * b * sum_of_triplet
        den = 2 * (sum_of_triplet - b)

        if num % den != 0:
            continue

        a = int(num/den)
        if a > b:
            continue
        c = sum_of_triplet - a - b
        if squares[a] + squares[b] == squares[c]:
            results.add((a, b, c))

    return results

