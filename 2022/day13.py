import operator
from functools import cmp_to_key


def compare(left, right):
    for index in range(min(len(left), len(right))):
        left_val, right_val = [packet[index] for packet in (left, right)]
        if isinstance(left_val, int) and isinstance(right_val, int):
            comparison = 1 if left_val < right_val else -1 if left_val > right_val else 0
        else:
            left_val, right_val = [[val] if isinstance(val, int) else val for val in (left_val, right_val)]
            comparison = compare(left_val, right_val)
        if comparison:
            return comparison
    return 1 if len(left) < len(right) else -1 if len(left) > len(right) else 0


with open('input/day13.txt') as input_file:
    pairs = [[eval(packet) for packet in pair.split('\n', 2)] for pair in input_file.read().split('\n\n')]
right_order_pair_numbers = []
for pair_index, pair in enumerate(pairs):
    if compare(*pair) == 1:
        right_order_pair_numbers.append(pair_index + 1)
print(sum(right_order_pair_numbers))
dividers = [[2]], [[6]]
packets = [*dividers, *[packet for pair in pairs for packet in pair]]
packets.sort(key=cmp_to_key(compare), reverse=True)
print(operator.mul(*[packets.index(divider) + 1 for divider in dividers]))
