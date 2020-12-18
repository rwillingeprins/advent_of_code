def parse_initial_state(file_path):
    with open(file_path) as file:
        return {(x, y) for x, line in enumerate(file) for y, state in enumerate(line.strip()) if state == '#'}


def get_neighbor_coordinates(coordinates):
    x, *remaining_coordinates = coordinates
    neighbor_coordinates_list = [(neighbor_x,) for neighbor_x in range(x - 1, x + 2)]
    while remaining_coordinates:
        x, *remaining_coordinates = remaining_coordinates
        neighbor_coordinates_list = [
            (*neighbor_coordinates, neighbor_x)
            for neighbor_coordinates in neighbor_coordinates_list
            for neighbor_x in range(x - 1, x + 2)
        ]
    neighbor_coordinates_list.remove(coordinates)
    return neighbor_coordinates_list


def get_active_conway_cubes_after_cycle(initial_active_coordinates):
    neighbor_count_per_coordinates = {}
    for coordinates in initial_active_coordinates:
        neighbor_coordinates_list = get_neighbor_coordinates(coordinates)
        for neighbor_coordinates in neighbor_coordinates_list:
            neighbor_count_per_coordinates.setdefault(neighbor_coordinates, 0)
            neighbor_count_per_coordinates[neighbor_coordinates] += 1
    active_coordinates = set()
    for coordinates, neighbor_count in neighbor_count_per_coordinates.items():
        if neighbor_count == 3 or (neighbor_count == 2 and coordinates in initial_active_coordinates):
            active_coordinates.add(coordinates)
    return active_coordinates


def day17a():
    active_coordinates = {coordinates + (0,) for coordinates in parse_initial_state('input/day17.txt')}
    for _ in range(6):
        active_coordinates = get_active_conway_cubes_after_cycle(active_coordinates)
    return len(active_coordinates)


def day17b():
    active_coordinates = {coordinates + (0, 0) for coordinates in parse_initial_state('input/day17.txt')}
    for _ in range(6):
        active_coordinates = get_active_conway_cubes_after_cycle(active_coordinates)
    return len(active_coordinates)


print(day17a())
print(day17b())
