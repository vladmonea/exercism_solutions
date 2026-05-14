def saddle_points(matrix):
    sp = set()

    lens = {len(line) for line in matrix}
    if len(lens) > 1:
        raise ValueError("Irregular matrix!")

    for ix, row in enumerate(matrix):
        max_row = max(row)
        candidates = [(i, x) for i, x in enumerate(row) if x == max_row]

        for i, candidate in candidates:
            column = [row[i] for row in matrix]
            min_col = min(column)
            if candidate == min_col:
                sp.add((ix+1, i+1))
    return sp


