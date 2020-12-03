def day03a():
    tree_grid = []
    with open('input/day03.txt') as input_file:
        for line in input_file:
            tree_line = [symbol == '#' for symbol in line.strip()]
            tree_grid.append(tree_line)
    n_rows = len(tree_grid)
    n_cols = len(tree_grid[0])
    (row, col) = (0, 0)
    (row_step, col_step) = (1, 3)
    n_trees = 0
    while 0 <= row < n_rows:
        if tree_grid[row][col % n_cols]:
            n_trees += 1
        (row, col) = (row + row_step, col + col_step)
    return n_trees


print(day03a())
