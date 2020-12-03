import re


def day02a():
    with open('input/day02.txt') as input_file:
        n_valid_passwords = 0
        for line in input_file:
            (minimum, maximum, character, password) = re.search(r'(\d+)-(\d+) (\w): (\w+)', line).groups()
            if int(minimum) <= password.count(character) <= int(maximum):
                n_valid_passwords += 1
        return n_valid_passwords


def day02b():
    with open('input/day02.txt') as input_file:
        n_valid_passwords = 0
        for line in input_file:
            (pos1, pos2, character, password) = re.search(r'(\d+)-(\d+) (\w): (\w+)', line).groups()
            (pos1_char, pos2_char) = [password[int(position) - 1] for position in (pos1, pos2)]
            if (pos1_char == character) != (pos2_char == character):
                n_valid_passwords += 1
        return n_valid_passwords


print(day02a())
print(day02b())
