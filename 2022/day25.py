with open('input/day25.txt') as input_file:
    snafus = input_file.read().splitlines()
digits = ['=', '-', '0', '1', '2']
value_per_digit = {digit: index - 2 for index, digit in enumerate(digits)}
number = sum(value_per_digit[digit] * 5 ** place for snafu in snafus for place, digit in enumerate(snafu[::-1]))
snafu = ''
while number:
    number, digit_index = divmod(number + 2, 5)
    snafu = digits[digit_index] + snafu
print(snafu)
