with open('input/day14.txt') as input_file:
    rock_paths = [[tuple(map(int, point.split(','))) for point in line.strip().split(' -> ')] for line in input_file]
blocked_tiles = set()
y_max = 0
for rock_path in rock_paths:
    (x, y), *target_tiles = rock_path
    blocked_tiles.add((x, y))
    y_max = max(y_max, y)
    for (target_x, target_y) in target_tiles:
        y_max = max(y_max, target_y)
        while x != target_x or y != target_y:
            x += (1 if x < target_x else -1 if x > target_x else 0)
            y += (1 if y < target_y else -1 if y > target_y else 0)
            blocked_tiles.add((x, y))
n_rock_tiles = len(blocked_tiles)
sand_source = (500, 0)
floor_hit = False
while sand_source not in blocked_tiles:
    x, y = sand_source
    while y <= y_max:
        fall_tile_gen = (tile for tile in [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)] if tile not in blocked_tiles)
        if fall_tile := next(fall_tile_gen, None):
            x, y = fall_tile
        else:
            blocked_tiles.add((x, y))
            break
    if y > y_max:
        if not floor_hit:
            floor_hit = True
            print(len(blocked_tiles) - n_rock_tiles)
        blocked_tiles.add((x, y))
print(len(blocked_tiles) - n_rock_tiles)
