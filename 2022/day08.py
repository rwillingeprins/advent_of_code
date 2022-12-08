with open('input/day08.txt') as input_file:
    lines = input_file.read().splitlines()
height_per_tree = {(row, col): int(height) for row, line in enumerate(lines) for col, height in enumerate(line)}
n_row = len(lines)
n_col = len(lines[0])


def view_trees(row, col, direction):
    if direction == 'up':
        return ((row2, col) for row2 in range(row - 1, -1, -1))
    if direction == 'down':
        return ((row2, col) for row2 in range(row + 1, n_row))
    if direction == 'left':
        return ((row, col2) for col2 in range(col - 1, -1, -1))
    if direction == 'right':
        return ((row, col2) for col2 in range(col + 1, n_col))


visible_trees_set = set()
for direction, start_trees in [
    ('up', view_trees(n_row, -1, 'right')),
    ('down', view_trees(-1, -1, 'right')),
    ('left', view_trees(-1, n_col - 1, 'down')),
    ('right', view_trees(-1, -1, 'down')),
]:
    for row, col in start_trees:
        highest = -1
        visible_trees = []
        for tree in view_trees(row, col, direction):
            height = height_per_tree[tree]
            if height > highest:
                visible_trees_set.add(tree)
                highest = height
print(len(visible_trees_set))
score_per_tree = {}
for (row, col), height in height_per_tree.items():
    scenic_score = 1
    for direction in ['up', 'down', 'left', 'right']:
        viewing_distance = 0
        for tree in view_trees(row, col, direction):
            viewing_distance += 1
            if height_per_tree[tree] >= height:
                break
        scenic_score *= viewing_distance
    score_per_tree[(row, col)] = scenic_score
print(max(score_per_tree.values()))
