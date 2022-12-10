import re

with open('input/day10.txt') as input_file:
    x = new_x = 1
    processing = 0
    signal_strengths = []
    crt = ''
    for cycle in range(1, 241):
        if not processing:
            instruction = input_file.readline().strip()
            if instruction == 'noop':
                processing = 1
                new_x = x
            elif match := re.fullmatch(r'addx (-?\d+)', instruction):
                processing = 2
                new_x = x + int(match.group(1))
        position = (cycle - 1) % 40
        if position == 19:
            signal_strengths.append(cycle * x)
        crt += '#' if abs(x - position) < 2 else '.'
        if position == 39:
            crt += '\n'
        processing -= 1
        if not processing:
            x = new_x
print(sum(signal_strengths))
print(crt)  # RFKZCPEF
