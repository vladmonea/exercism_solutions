def is_paired(input_string):
    # mapping = dict(('()', '[]', '{}'))
    # more explicit, though
    start = ('(', '[', '{')
    end = (')', ']', '}')
    mapping = {k: v for k, v in zip(start, end)}
    stack = []

    for char in input_string:
        if char in start:
            stack.append(mapping[char])
        elif char in end:
            if not stack or char != stack.pop():
                return False
    return not stack
