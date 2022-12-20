rock_shapes = [
    {(0, 0), (1, 0), (2, 0), (3, 0)},
    {(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)},
    {(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)},
    {(0, 0), (0, 1), (0, 2), (0, 3)},
    {(0, 0), (1, 0), (0, 1), (1, 1)},
]
with open('input/day17.txt') as input_file:
    gusts = [-1 if g == '<' else 1 for g in input_file.read().strip()]
for n_simulations in (2022, 1000000000000):
    tower_height = 0
    tower = set((x, -1) for x in range(7))
    rock_index = -1
    gust_index = -1
    gust_cycles = [(0, 0)]
    skipped_height = 0
    while rock_index < n_simulations - 1:
        rock_index += 1
        rock = set((x + 2, y + tower_height + 3) for x, y in rock_shapes[rock_index % len(rock_shapes)])
        while True:
            gust_index = (gust_index + 1) % len(gusts)
            gust = gusts[gust_index]
            pushed_rock = set((x + gust, y) for x, y in rock)
            if all(0 <= x < 7 for x, _ in pushed_rock) and pushed_rock.isdisjoint(tower):
                rock = pushed_rock
            fallen_rock = set((x, y - 1) for x, y in rock)
            if fallen_rock.isdisjoint(tower):
                rock = fallen_rock
            else:
                break
        tower_height = max(tower_height, max(y for _, y in rock) + 1)
        tower.update(rock)
        if gust_index == 0:
            gust_cycles.append((rock_index, tower_height))
            if len(gust_cycles) > 2:
                diff, last_diff = [tuple(gust_cycles[i][j] - gust_cycles[i - 1][j] for j in (0, 1)) for i in (-1, -2)]
                if diff == last_diff:
                    rocks_diff, height_diff = diff
                    skipped_gust_cycles = (n_simulations - rock_index) // rocks_diff
                    rock_index += skipped_gust_cycles * rocks_diff
                    skipped_height += skipped_gust_cycles * height_diff
    print(tower_height + skipped_height)
