def multiply_elements(array):
    prod = 1
    for elem in array:
        prod *= elem
    return prod

def largest_product(series, size):
    length = len(series)
    if size > length or size < 0:
        raise ValueError("span size incorrect")
    if size == length == 0:
        return 1

    max_product = 0
    for start_pos in range(length - size + 1):
        current_product = multiply_elements(
            [int(i) for i in series[start_pos:start_pos + size]]
        )
        if current_product > max_product:
            max_product = current_product
    return max_product

