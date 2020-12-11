def parse_seat_layout(file_path):
    with open(file_path) as input_file:
        seat_layout = [list(line.strip()) for line in input_file]
    return seat_layout


def day11a():
    grid = parse_seat_layout('input/day11.txt')
    row_length = len(grid)
    col_length = len(grid[0])
    while True:
        new_grid = [list(row) for row in grid]
        for row_i, row in enumerate(grid):
            for col_i, state in enumerate(row):
                if state == '.':
                    continue
                n_adjacent_occupied = 0
                for row_step, col_step in (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1):
                    adj_row_i = row_i + row_step
                    adj_col_i = col_i + col_step
                    if not 0 <= adj_row_i < row_length or not 0 <= adj_col_i < col_length:
                        continue
                    if grid[adj_row_i][adj_col_i] == '#':
                        n_adjacent_occupied += 1
                        if n_adjacent_occupied >= 4:
                            new_grid[row_i][col_i] = 'L'
                            break
                if n_adjacent_occupied == 0:
                    new_grid[row_i][col_i] = '#'
        if new_grid == grid:
            break
        grid = new_grid
    return sum([sum(state == '#' for state in row) for row in grid])


def day11b():
    grid = parse_seat_layout('input/day11.txt')
    row_length = len(grid)
    col_length = len(grid[0])
    while True:
        new_grid = [list(row) for row in grid]
        for row_i, row in enumerate(grid):
            for col_i, state in enumerate(row):
                if state == '.':
                    continue
                n_adjacent_occupied = 0
                for row_step, col_step in (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1):
                    adj_row_i = row_i + row_step
                    adj_col_i = col_i + col_step
                    while 0 <= adj_row_i < row_length and 0 <= adj_col_i < col_length:
                        seen_state = grid[adj_row_i][adj_col_i]
                        if seen_state != '.':
                            if seen_state == '#':
                                n_adjacent_occupied += 1
                            break
                        adj_row_i += row_step
                        adj_col_i += col_step
                    if n_adjacent_occupied >= 5:
                        new_grid[row_i][col_i] = 'L'
                if n_adjacent_occupied == 0:
                    new_grid[row_i][col_i] = '#'
        if new_grid == grid:
            break
        grid = new_grid
    return sum([sum(state == '#' for state in row) for row in grid])


print(day11a())
print(day11b())
