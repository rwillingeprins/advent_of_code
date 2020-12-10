def parse_ints_from_file(file_path):
    with open(file_path) as file:
        return [int(line.strip()) for line in file]


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
    path_counts = [0] * len(joltages)
    path_counts[0] = 1
    for index in range(1, len(joltages)):
        for preceding_index in range(index - 1, index - 4, -1):
            if preceding_index < 0 or joltages[preceding_index] < joltages[index] - 3:
                break
            path_counts[index] += path_counts[preceding_index]
    return path_counts[-1]


print(day10a())
print(day10b())
