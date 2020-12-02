import re


def day02a():
    with open('input/day02.txt') as input_file:
        n_valid_passwords = 0
        for line in input_file:
            (minimum, maximum, character, password) = re.search(r'(\d+)-(\d+) (\w): (\w+)', line).groups()
            if int(minimum) <= password.count(character) <= int(maximum):
                n_valid_passwords += 1
        return n_valid_passwords


print(day02a())
