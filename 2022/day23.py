with open('input/day23.txt') as input_file:
    elves = set((r, c) for r, line in enumerate(input_file) for c, tile in enumerate(line.strip()) if tile == '#')
adj = {'E': (0, 1), 'NE': (-1, 1), 'N': (-1, 0), 'NW': (-1, -1), 'W': (0, -1), 'SW': (1, -1), 'S': (1, 0), 'SE': (1, 1)}
valid_directions = [('N', 'NE', 'NW'), ('S', 'SE', 'SW'), ('W', 'NW', 'SW'), ('E', 'NE', 'SE')]


def simulate_elf_process():
    proposing_elves_per_position = {}
    for row, col in elves:
        position_per_direction = {direction: (row + ra, col + ca) for direction, (ra, ca) in adj.items()}
        if any(position in elves for position in position_per_direction.values()):
            for area in valid_directions:
                if not any(position_per_direction[direction] in elves for direction in area):
                    proposing_elves = proposing_elves_per_position.setdefault(position_per_direction[area[0]], [])
                    proposing_elves.append((row, col))
                    break
    for position, (proposing_elf, *other_proposing_elves) in proposing_elves_per_position.items():
        if not other_proposing_elves:
            elves.remove(proposing_elf)
            elves.add(position)
    valid_directions.append(valid_directions.pop(0))


round_number = 10
for _ in range(round_number):
    simulate_elf_process()
min_row, min_col = max_row, max_col = next(iter(elves))
for row, col in elves:
    min_row = min(min_row, row)
    max_row = max(max_row, row)
    min_col = min(min_col, col)
    max_col = max(max_col, col)
print(sum((row, col) not in elves for row in range(min_row, max_row + 1) for col in range(min_col, max_col + 1)))
previous_elves = set()
while previous_elves != elves:
    round_number += 1
    previous_elves = elves.copy()
    simulate_elf_process()
print(round_number)
