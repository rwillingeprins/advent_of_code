def parse_tree_map_input(file_path):
    tree_map = []
    with open(file_path) as input_file:
        for line in input_file:
            tree_line = [symbol == '#' for symbol in line.strip()]
            tree_map.append(tree_line)
    return tree_map


def count_slope_trees(tree_map, slope):
    n_rows = len(tree_map)
    n_cols = len(tree_map[0])
    (row_step, col_step) = slope
    (row, col) = (0, 0)
    n_trees = 0
    while 0 <= row < n_rows:
        if tree_map[row][col % n_cols]:
            n_trees += 1
        (row, col) = (row + row_step, col + col_step)
    return n_trees


def day03a():
    tree_map = parse_tree_map_input('input/day03.txt')
    slope = (1, 3)
    return count_slope_trees(tree_map, slope)


def day03b():
    tree_map = parse_tree_map_input('input/day03.txt')
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    answer = 1
    for slope in slopes:
        answer *= count_slope_trees(tree_map, slope)
    return answer


print(day03a())
print(day03b())
