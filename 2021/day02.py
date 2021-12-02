def day02a():
    with open('input/day02.txt') as input_file:
        horizontal_position = 0
        depth = 0
        for line in input_file:
            (direction, distance_string) = line.split(' ', 2)
            distance = int(distance_string)
            if direction == 'forward':
                horizontal_position += distance
            elif direction == 'up':
                depth -= distance
            elif direction == 'down':
                depth += distance
        return horizontal_position * depth


def day02b():
    with open('input/day02.txt') as input_file:
        horizontal_position = 0
        depth = 0
        aim = 0
        for line in input_file:
            (direction, x_string) = line.split(' ', 2)
            x = int(x_string)
            if direction == 'forward':
                horizontal_position += x
                depth += aim * x
            elif direction == 'up':
                aim -= x
            elif direction == 'down':
                aim += x
        return horizontal_position * depth


print(day02a())
print(day02b())
