from collections import defaultdict
from itertools import combinations_with_replacement


def largest(min_factor, max_factor):
    products = palindrome_products(min_factor, max_factor)
    if products:
        max_prod = max(products.keys())
        return max_prod, products[max_prod]
    return None, []


def smallest(min_factor, max_factor):
    products = palindrome_products(min_factor, max_factor)
    if products:
        min_prod = min(products.keys())
        return min_prod, products[min_prod]
    return None, []


def palindrome_products(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("Min is larger than max!")
    results = defaultdict(list)
    r = range(min_factor, max_factor + 1)
    for i, j in combinations_with_replacement(r, 2):
        prod = i * j
        if str(prod) == str(prod)[::-1]:
            results[prod].append((i, j))
    return results

