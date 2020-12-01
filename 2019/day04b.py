def has_double(values):
    previous_value = values[0]
    n_duplicates = 0
    for value in values[1:]:
        if value == previous_value:
            n_duplicates += 1
        elif n_duplicates == 1:
            break
        else:
            n_duplicates = 0
        previous_value = value
    return n_duplicates == 1


def combinations_with_base(length, base):
    combinations = []
    for digit in range(base, 10):
        if length > 1:
            combinations.extend(
                [[digit] + sub_combination for sub_combination in combinations_with_base(length - 1, digit)]
            )
        else:
            combinations.append([digit])
    return combinations


n_passwords = 0
minimum = 246540
limit = 787419
combos = combinations_with_base(6, 2)
for combo in combos:
    if has_double(combo):
        number = int(''.join(map(str, combo)))
        if minimum <= number < limit:
            n_passwords += 1
print(n_passwords)
