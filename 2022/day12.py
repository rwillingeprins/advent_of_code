import math

elevation_per_character = {character: elevation for elevation, character in enumerate('SabcdefghijklmnopqrstuvwxyzE')}
with open('input/day12.txt') as input_file:
    heightmap = [[elevation_per_character[character] for character in line] for line in input_file.read().splitlines()]


def find_shortest_path(start_position):
    path_length = 0

    frontiers = [start_position]
    eliminated = set()
    eliminated.update((row, outer_col) for row in range(len(heightmap)) for outer_col in (-1, len(heightmap[0])))
    eliminated.update((outer_row, col) for col in range(len(heightmap[0])) for outer_row in (-1, len(heightmap)))
    eliminated.add(start_position)
    while frontiers:
        path_length += 1
        new_frontiers = []
        for row, col in frontiers:
            elevation = heightmap[row][col]
            for new_row, new_col in [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)]:
                if (new_row, new_col) not in eliminated:
                    new_elevation = heightmap[new_row][new_col]
                    if new_elevation - elevation <= 1:
                        if new_elevation == 27:
                            return path_length
                        new_frontiers.append((new_row, new_col))
                        eliminated.add((new_row, new_col))
        frontiers = new_frontiers
    return math.inf


print(find_shortest_path(next(
    (row, col) for row, elevations in enumerate(heightmap) for col, elevation in enumerate(elevations) if elevation == 0
)))
print(min(
    find_shortest_path((row, col))
    for row, elevations in enumerate(heightmap) for col, elevation in enumerate(elevations) if elevation == 1
))
