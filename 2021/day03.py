def day03a():
    n_diagnostics = 0
    ones_counts = [0] * 12
    with open('input/day03.txt') as file:
        for line in file:
            n_diagnostics += 1
            for bit_position, bit in enumerate(line.strip()):
                if bit == '1':
                    ones_counts[bit_position] += 1
    gamma = epsilon = 0
    for bit_power, ones_count in enumerate(reversed(ones_counts)):
        if 2 * ones_count > n_diagnostics:
            gamma += 2 ** bit_power
        else:
            epsilon += 2 ** bit_power
    return gamma * epsilon


def day03b():
    with open('input/day03.txt') as file:
        bitstrings = [bitstring.strip() for bitstring in file]
    o2_bitstrings = set(bitstrings)
    bit_position = 0
    while len(o2_bitstrings) > 1:
        o2_one_bitstrings = set(bitstring for bitstring in o2_bitstrings if bitstring[bit_position] == '1')
        if 2 * len(o2_one_bitstrings) >= len(o2_bitstrings):
            o2_bitstrings = o2_one_bitstrings
        else:
            o2_bitstrings -= o2_one_bitstrings
        bit_position += 1
    co2_bitstrings = set(bitstrings)
    bit_position = 0
    while len(co2_bitstrings) > 1:
        co2_one_bitstrings = set(bitstring for bitstring in co2_bitstrings if bitstring[bit_position] == '1')
        if 2 * len(co2_one_bitstrings) < len(co2_bitstrings):
            co2_bitstrings = co2_one_bitstrings
        else:
            co2_bitstrings -= co2_one_bitstrings
        bit_position += 1
    return int(list(o2_bitstrings)[0], 2) * int(list(co2_bitstrings)[0], 2)


print(day03a())
print(day03b())
