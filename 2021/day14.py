from collections import defaultdict


def polymerize(n_steps):
    with open('input/day14.txt') as file:
        polymer_template, insertion_rules_string = file.read().split('\n\n', 2)
    count_per_polymer_pair = defaultdict(int)
    for pair_start in range(len(polymer_template) - 1):
        pair = polymer_template[pair_start:pair_start + 2]
        count_per_polymer_pair[pair] += 1
    insertion_per_pair = dict(
        tuple(insertion_rule.split(' -> ')) for insertion_rule in insertion_rules_string.splitlines())
    for _ in range(n_steps):
        new_count_per_polymer_pair = defaultdict(int)
        for pair, count in count_per_polymer_pair.items():
            insertion = insertion_per_pair[pair]
            new_count_per_polymer_pair[pair[0] + insertion] += count
            new_count_per_polymer_pair[insertion + pair[1]] += count
        count_per_polymer_pair = new_count_per_polymer_pair
    double_count_per_element = defaultdict(int)
    double_count_per_element[polymer_template[0]] += 1
    double_count_per_element[polymer_template[-1]] += 1
    for pair, count in count_per_polymer_pair.items():
        for element in pair:
            double_count_per_element[element] += count
    element_counts = sorted(double_count // 2 for double_count in double_count_per_element.values())
    return element_counts[-1] - element_counts[0]


print(polymerize(10))
print(polymerize(40))
