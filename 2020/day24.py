import re

p = re.compile(r'(e|se|sw|w|nw|ne)')
with open('input/day24.txt') as file:
    tile_paths = (p.findall(line) for line in file.read().splitlines())
xy_per_direction = {'e': (2, 0), 'se': (1, -1), 'sw': (-1, -1), 'w': (-2, 0), 'nw': (-1, 1), 'ne': (1, 1)}
black_tile_set = set()
for tile_path in tile_paths:
    x, y = 0, 0
    for direction in tile_path:
        x_step, y_step = xy_per_direction[direction]
        x += x_step
        y += y_step
    if (x, y) in black_tile_set:
        black_tile_set.remove((x, y))
    else:
        black_tile_set.add((x, y))
print(len(black_tile_set))

for day in range(100):
    black_neighbor_count_per_tile = {}
    for x, y in black_tile_set:
        black_neighbor_count_per_tile.setdefault((x, y), 0)
        for (x_step, y_step) in xy_per_direction.values():
            neighbor_xy = x + x_step, y + y_step
            black_neighbor_count_per_tile.setdefault(neighbor_xy, 0)
            black_neighbor_count_per_tile[neighbor_xy] += 1
    for tile_xy, black_neighbor_count in black_neighbor_count_per_tile.items():
        if tile_xy in black_tile_set:
            if black_neighbor_count == 0 or black_neighbor_count > 2:
                black_tile_set.remove(tile_xy)
        elif black_neighbor_count == 2:
            black_tile_set.add(tile_xy)
print(len(black_tile_set))
