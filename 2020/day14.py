import re


def day14a():
    file_path = 'input/day14.txt'
    with open(file_path) as file:
        assignments = [line.split(' = ', 2) for line in file.read().splitlines()]
    memory = {}
    true_mask = 0
    false_mask = 2 ** 35
    for variable, value in assignments:
        if variable == 'mask':
            true_mask = int(''.join('1' if c == '1' else '0' for c in value), 2)
            false_mask = int(''.join('0' if c == '0' else '1' for c in value), 2)
        else:
            address = int(re.match(r'mem\[(\d+)\]$', variable).group(1))
            memory[address] = (int(value) | true_mask) & false_mask
    return sum(memory.values())


def day14b():
    file_path = 'input/day14.txt'
    with open(file_path) as file:
        assignments = [line.split(' = ', 2) for line in file.read().splitlines()]
    memory = {}
    true_mask = 0
    floating_masks = []
    for variable, value in assignments:
        if variable == 'mask':
            true_mask = int(''.join('1' if c == '1' else '0' for c in value), 2)
            floating_masks = [2 ** i for i, c in enumerate(reversed(value)) if c == 'X']
        else:
            addresses = [int(re.match(r'mem\[(\d+)\]$', variable).group(1)) | true_mask]
            for floating_mask in floating_masks:
                addresses.extend([address ^ floating_mask for address in addresses])
            for address in addresses:
                memory[address] = int(value)
    return sum(memory.values())


print(day14a())
print(day14b())
