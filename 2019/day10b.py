def greatest_common_divisor(a, b):
    if b == 0:
        return a
    remainder = a % b
    return greatest_common_divisor(b, remainder)


def line_function(point):
    x, y = point
    return y / x


laser_x = 19
laser_y = 11
up = {}
right = {}
down = {}
left = {}
with open('day10.txt') as input_file:
    lines = input_file.readlines()
    for y, line in enumerate(lines):
        relative_y = y - laser_y
        y_distance = abs(relative_y)
        for x, character in enumerate(line):
            if character == '#':
                relative_x = x - laser_x
                location = (x, y)
                if relative_x == 0:
                    if relative_y > 0:
                        up[y_distance] = location
                    else:
                        down[y_distance] = location
                else:
                    gcd = greatest_common_divisor(relative_x, relative_y)
                    x_step = relative_x // gcd
                    y_step = relative_y // gcd
                    line_point = x_step, y_step
                    if relative_x > 0:
                        right.setdefault(line_point, {})[y_distance] = location
                    else:
                        left.setdefault(line_point, {})[y_distance] = location
directions = [up]
directions.extend([right[line_point] for line_point in sorted(right.keys(), key=line_function)])
directions.append(down)
directions.extend([left[line_point] for line_point in sorted(left.keys(), key=line_function)])

asteroid_count = 0
answer = None
while answer is None:
    for asteroid_per_distance in directions:
        if asteroid_per_distance:
            closest = min(asteroid_per_distance.keys())
            asteroid_count += 1
            if asteroid_count == 200:
                x, y = asteroid_per_distance[closest]
                answer = 100 * x + y
                break
            del asteroid_per_distance[closest]
print(answer)
