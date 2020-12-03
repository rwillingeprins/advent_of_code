def day03b():
    tree_grid = []
    with open('input/day03.txt') as input_file:
        for line in input_file:
            tree_line = [symbol == '#' for symbol in line.strip()]
            tree_grid.append(tree_line)
    n_rows = len(tree_grid)
    n_cols = len(tree_grid[0])
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    answer = 1
    for (row_step, col_step) in slopes:
        (row, col) = (0, 0)
        n_trees = 0
        while 0 <= row < n_rows:
            if tree_grid[row][col % n_cols]:
                n_trees += 1
            (row, col) = (row + row_step, col + col_step)
        answer *= n_trees
    return answer


print(day03b())
