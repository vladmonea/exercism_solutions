def slices(series, length):
    if length < 1 or length > len(series):
        raise ValueError(f"what's the big idea? we ain't got {length} items")
    slices = []
    for i in range(0, len(series)):
        if i + length > len(series):
            return slices
        slc = series[i: i + length]
        slices.append(slc)
    return slices
