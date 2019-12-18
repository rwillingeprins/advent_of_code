def greatest_common_denominator(larger_integer, smaller_integer):
    if smaller_integer == 0:
        return larger_integer
    remainder = larger_integer % smaller_integer
    return greatest_common_denominator(smaller_integer, remainder)


def integers_between(start, end):
    step = 1
    if start > end:
        step = -1
    return range(start + step, end, step)


def points_between(here, there):
    points = []
    x_here, y_here = here
    x_there, y_there = there
    x_diff = x_there - x_here
    y_diff = y_there - y_here
    if x_diff or y_diff:
        larger = max(x_diff, y_diff)
        smaller = min(x_diff, y_diff)
        gcd = greatest_common_denominator(larger, smaller)
        x_factor = x_diff // gcd
        y_factor = y_diff // gcd
        for common_factor in integers_between(0, gcd):
            x = x_here + (x_factor * common_factor)
            y = y_here + (y_factor * common_factor)
            point = x, y
            points.append(point)
    return points


asteroid_set = set()
with open('day10.txt') as input_file:
    for y, line in enumerate(input_file):
        for x, character in enumerate(line):
            if character == '#':
                point = (x, y)
                asteroid_set.add(point)

max_visible_asteroids = 0
best_location = 0, 0
for here in asteroid_set:
    visible_asteroids_count = 0
    for there in asteroid_set:
        if there == here:
            continue
        is_visible = True
        for point in points_between(here, there):
            if point in asteroid_set:
                is_visible = False
                break
        if is_visible:
            visible_asteroids_count += 1
    if visible_asteroids_count > max_visible_asteroids:
        max_visible_asteroids = visible_asteroids_count
        best_location = here
print(best_location, max_visible_asteroids)
