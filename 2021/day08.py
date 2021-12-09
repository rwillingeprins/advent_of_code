with open('input/day08.txt') as file:
    notes = [
        tuple(
            tuple(
                frozenset(pattern_string) for pattern_string in patterns_string.split()
            ) for patterns_string in line.strip().split(' | ', 2)
        ) for line in file
    ]
print(sum(1 for _, outputs in notes for output in outputs if len(output) in {2, 4, 3, 7}))


def decode(signals, outputs):
    one = next(signal for signal in signals if len(signal) == 2)
    four = next(signal for signal in signals if len(signal) == 4)
    seven = next(signal for signal in signals if len(signal) == 3)
    eight = next(signal for signal in signals if len(signal) == 7)
    three = next(signal for signal in signals if len(signal) == 5 and len(signal - seven) == 2)
    nine = three | four
    six = next(signal for signal in signals if len(signal) == 6 and len(signal - one) == 5)
    five = six - (eight - nine)
    zero = next(signal for signal in signals if len(signal) == 6 and signal != six and signal != nine)
    two = next(signal for signal in signals if len(signal) == 5 and signal != three and signal != five)
    decoder = {zero: 0, one: 1, two: 2, three: 3, four: 4, five: 5, six: 6, seven: 7, eight: 8, nine: 9}
    return int(''.join(str(decoder[output]) for output in outputs))


print(sum(decode(signals, outputs) for signals, outputs in notes))
