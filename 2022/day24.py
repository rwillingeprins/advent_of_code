with open('input/day24.txt') as input_file:
    valley_map = [line.strip('#') for line in input_file.read().splitlines()[1:-1]]
n_rows = len(valley_map)
n_cols = len(valley_map[0])
valley_entrance = (0, -1)
valley_exit = (n_rows, n_cols - 1)
walls = {(0, -2)}
walls.update((row, col) for row in range(-1, n_rows + 1) for col in (-1, n_cols))
walls.update((row, col) for row in (-1, n_rows) for col in range(-1, n_cols + 1))
walls.remove(valley_entrance)
walls.remove(valley_exit)
up, down, left, right = set(), set(), set(), set()
for row, tiles in enumerate(valley_map):
    for col, tile in enumerate(tiles):
        if tile == '^':
            up.add((row, col))
        if tile == 'v':
            down.add((row, col))
        if tile == '<':
            left.add((row, col))
        if tile == '>':
            right.add((row, col))
steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
goal = valley_exit
positions = {valley_entrance}
minute = 0
snacks_present = False
while positions:
    up = set(((row - 1) % n_rows, col) for row, col in up)
    down = set(((row + 1) % n_rows, col) for row, col in down)
    left = set((row, (col - 1) % n_cols) for row, col in left)
    right = set((row, (col + 1) % n_cols) for row, col in right)
    positions.update([(row + row_step, col + col_step) for row, col in positions for row_step, col_step in steps])
    positions -= walls.union(up, down, left, right)
    minute += 1
    if goal in positions:
        if goal == valley_exit:
            print(minute)
            if snacks_present:
                break
            else:
                goal = valley_entrance
                positions = {valley_exit}
        elif goal == valley_entrance:
            snacks_present = True
            goal = valley_exit
            positions = {valley_entrance}
