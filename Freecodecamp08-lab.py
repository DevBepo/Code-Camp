def number_pattern(n):
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    sequence = []
    for number in range(1, n + 1):
        sequence.append(str(number))
    return ' '.join(sequence)

print(number_pattern(4))