import re

with open('input/day22.txt') as input_file:
    board_input, path = input_file.read().split('\n\n', 2)
board = board_input.splitlines()
instructions = re.findall(r'(\d+|L|R)', path)
n_rows = len(board)
n_columns = max(len(tiles) for tiles in board)
board = [tiles.ljust(n_columns) for tiles in board]
steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def wrap_step(row, column, facing):
    row_step, column_step = steps[facing]
    next_row = (row + row_step) % n_rows
    next_column = (column + column_step) % n_columns
    while board[next_row][next_column] == ' ':
        next_row = (next_row + row_step) % n_rows
        next_column = (next_column + column_step) % n_columns
    return next_row, next_column, facing


def cube_step(row, column, facing):
    if facing == 0:
        if column == 149 and 0 <= row < 50:
            return 149 - row, 99, 2
        elif column == 99 and 50 <= row < 100:
            return 49, row + 50, 3
        elif column == 99 and 100 <= row < 150:
            return 149 - row, 149, 2
        elif column == 49 and 150 <= row < 200:
            return 149, row - 100, 3
        else:
            return row, column + 1, facing
    elif facing == 1:
        if row == 199 and 0 <= column < 50:
            return 0, 100 + column, 1
        elif row == 149 and 50 <= column < 100:
            return column + 100, 49, 2
        elif row == 49 and 100 <= column < 150:
            return column - 50, 99, 2
        else:
            return row + 1, column, facing
    elif facing == 2:
        if column == 50 and 0 <= row < 50:
            return 149 - row, 0, 0
        elif column == 50 and 50 <= row < 100:
            return 100, row - 50, 1
        elif column == 0 and 100 <= row < 150:
            return 149 - row, 50, 0
        elif column == 0 and 150 <= row < 200:
            return 0, row - 100, 1
        else:
            return row, column - 1, facing
    elif facing == 3:
        if row == 100 and 0 <= column < 50:
            return column + 50, 50, 0
        elif row == 0 and 50 <= column < 100:
            return column + 100, 0, 0
        elif row == 0 and 100 <= column < 150:
            return 199, column - 100, 3
        else:
            return row - 1, column, facing


def get_password(step_func=wrap_step):
    row = 0
    column = next(c for c, tile in enumerate(board[0]) if tile == '.')
    facing = 0
    for instruction in instructions:
        if instruction == 'L':
            facing = (facing - 1) % 4
        elif instruction == 'R':
            facing = (facing + 1) % 4
        else:
            for _ in range(int(instruction)):
                next_row, next_column, next_facing = step_func(row, column, facing)
                if board[next_row][next_column] == '#':
                    break
                row, column, facing = next_row, next_column, next_facing
    return 1000 * (row + 1) + 4 * (column + 1) + facing


print(get_password())
print(get_password(cube_step))
