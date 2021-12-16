import re


def fold(dot_map, fold_instruction):
    (fold_dimension, fold_coordinate_string) = re.search(r'fold along ([xy])=(\d+)', fold_instruction).groups()
    fold_coordinate = int(fold_coordinate_string)
    folded_dot_map = set()
    if fold_dimension == 'x':
        for x, y in dot_map:
            if x > fold_coordinate:
                x = 2 * fold_coordinate - x
            folded_dot_map.add((x, y))
    elif fold_dimension == 'y':
        for x, y in dot_map:
            if y > fold_coordinate:
                y = 2 * fold_coordinate - y
            folded_dot_map.add((x, y))
    return folded_dot_map


def stringify_dot_map(dot_map):
    x_max = max(x for x, _ in dot_map)
    y_max = max(y for _, y in dot_map)
    return '\n'.join(''.join('#' if (x, y) in dot_map else '.' for x in range(x_max + 1)) for y in range(y_max + 1))


with open('input/day13.txt') as file:
    dots_input, folds_input = file.read().split('\n\n', 2)
dot_map = set()
for dot_line in dots_input.splitlines():
    x, y = map(int, dot_line.split(','))
    dot_map.add((x, y))
fold_instructions = folds_input.splitlines()
print(len(fold(dot_map, fold_instructions[0])))

for fold_instruction in fold_instructions:
    dot_map = fold(dot_map, fold_instruction)
print(stringify_dot_map(dot_map))
