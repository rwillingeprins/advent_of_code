def get_depth_measurements():
    with open('input/day01.txt') as file:
        return [int(line) for line in file]


def day01a():
    measurements = get_depth_measurements()
    return sum(measurements[index + 1] > measurements[index] for index in range(len(measurements) - 1))


def day01b():
    measurements = get_depth_measurements()
    return sum(measurements[index + 3] > measurements[index] for index in range(len(measurements) - 3))


print(day01a())
print(day01b())
