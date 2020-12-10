def parse_ints_from_file(file_path):
    with open(file_path) as file:
        return [int(line.strip()) for line in file]


valid_arrangements_from_joltage = {}


def get_valid_adapter_arrangements(joltages):
    joltage, *remaining_joltages = joltages
    if joltage not in valid_arrangements_from_joltage:
        if not remaining_joltages:
            return 1
        valid_arrangements = 0
        while remaining_joltages and remaining_joltages[0] - joltage <= 3:
            valid_arrangements += get_valid_adapter_arrangements(remaining_joltages)
            remaining_joltages = remaining_joltages[1:]
        valid_arrangements_from_joltage[joltage] = valid_arrangements
    return valid_arrangements_from_joltage[joltage]


def day10a():
    adapter_joltages = sorted(parse_ints_from_file('input/day10.txt'))
    device_joltage = adapter_joltages[-1] + 3
    joltages = [0] + adapter_joltages + [device_joltage]
    n_1_jolt_differences = n_3_jolt_differences = 0
    for index in range(len(joltages) - 1):
        joltage_difference = joltages[index + 1] - joltages[index]
        if joltage_difference == 1:
            n_1_jolt_differences += 1
        elif joltage_difference == 3:
            n_3_jolt_differences += 1
    return n_1_jolt_differences * n_3_jolt_differences


def day10b():
    adapter_joltages = sorted(parse_ints_from_file('input/day10.txt'))
    device_joltage = adapter_joltages[-1] + 3
    joltages = [0] + adapter_joltages + [device_joltage]
    return get_valid_adapter_arrangements(joltages)


print(day10a())
print(day10b())
