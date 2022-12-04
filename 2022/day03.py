lines = open('input/day03.txt').read().splitlines()

priority_per_item_type = {chr(n): i + 1 for i, n in enumerate([*range(97, 123), *range(65, 91)])}
priority_sum = 0
for line in lines:
    c2_start = len(line) // 2
    c1_set = set(line[:c2_start])
    shared_item_type = next(item for item in line[c2_start:] if item in c1_set)
    priority_sum += priority_per_item_type[shared_item_type]
print(priority_sum)

priority_sum = 0
for line_index in range(0, len(lines), 3):
    badge = next(iter(set.intersection(*[set(line) for line in lines[line_index:line_index + 3]])))
    priority_sum += priority_per_item_type[badge]
print(priority_sum)
