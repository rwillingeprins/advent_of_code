import re


def rearrange(crane='CrateMover 9000'):
    start_input, rearrangements_input = open('input/day05.txt').read().split('\n\n')
    stacks, *crate_layers = [stack_line[1::4] for stack_line in reversed(start_input.splitlines())]
    crates_per_stack = {stack_name: [] for stack_name in stacks}
    for crate_layer in crate_layers:
        for stack_index, crate in enumerate(crate_layer):
            if crate != ' ':
                crates_per_stack[stacks[stack_index]].append(crate)
    rearrangement_pattern = re.compile(r'move (\d+) from (\d) to (\d)')
    for rearrangement in rearrangements_input.splitlines():
        quantity, from_stack, to_stack = re.search(rearrangement_pattern, rearrangement).groups()
        crates = [crates_per_stack[from_stack].pop() for _ in range(int(quantity))]
        if crane == 'CrateMover 9001':
            crates.reverse()
        crates_per_stack[to_stack].extend(crates)
    return ''.join(crates_per_stack[stack_name][-1] for stack_name in stacks)


print(rearrange())
print(rearrange('CrateMover 9001'))
