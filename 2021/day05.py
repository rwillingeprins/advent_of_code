def get_vent_lines():
    with open('input/day05.txt') as file:
        return [
            tuple(
                tuple(
                    int(coord) for coord in end.split(',')
                ) for end in line.split(' -> ')
            ) for line in file.readlines()
        ]


def day05a():
    vent_lines = get_vent_lines()
    vent_count_per_area = {}
    for ((x1, y1), (x2, y2)) in vent_lines:
        if x1 == x2 or y1 == y2:
            x_start, x_end = sorted((x1, x2))
            y_start, y_end = sorted((y1, y2))
            for x in range(x_start, x_end + 1):
                for y in range(y_start, y_end + 1):
                    vent_count_per_area.setdefault((x, y), 0)
                    vent_count_per_area[(x, y)] += 1
    dangerous_areas = [area for area, vent_count in vent_count_per_area.items() if vent_count > 1]
    return len(dangerous_areas)


def day05b():
    vent_lines = get_vent_lines()
    vent_count_per_area = {}
    for ((x1, y1), (x2, y2)) in vent_lines:
        x_diff = x2 - x1
        y_diff = y2 - y1
        n_steps = max(abs(x_diff), abs(y_diff))
        x_step_size = x_diff // n_steps
        y_step_size = y_diff // n_steps
        for step in range(n_steps + 1):
            x = x1 + step * x_step_size
            y = y1 + step * y_step_size
            vent_count_per_area.setdefault((x, y), 0)
            vent_count_per_area[(x, y)] += 1
    dangerous_areas = [area for area, vent_count in vent_count_per_area.items() if vent_count > 1]
    return len(dangerous_areas)


print(day05a())
print(day05b())
