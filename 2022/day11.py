import re


def monkey_business(rounds=20, relief=3):
    with open('input/day11.txt') as input_file:
        monkey_inputs = input_file.read().split('\n\n')
    monkeys = []
    divisor_product = 1
    for monkey_input in monkey_inputs:
        _, items_input, operation_input, test_input, true_input, false_input = monkey_input.splitlines()
        items = [int(item) for item in re.search(r'Starting items: ((?:\d+, )*\d+)', items_input).group(1).split(', ')]
        operator_string, value_string = re.search(r'Operation: new = old ([+\-*/]) (old|\d+)', operation_input).groups()
        divisor = int(re.search(r'Test: divisible by (\d+)', test_input).group(1))
        true_monkey = int(re.search(r'If true: throw to monkey (\d+)', true_input).group(1))
        false_monkey = int(re.search(r'If false: throw to monkey (\d+)', false_input).group(1))
        monkeys.append({
            'items': items,
            'operation': (operator_string, value_string, divisor, true_monkey, false_monkey),
            'inspected': 0,
        })
        divisor_product *= divisor
    for _ in range(rounds):
        for monkey in monkeys:
            operator_string, value_string, divisor, true_monkey, false_monkey = monkey['operation']
            while monkey['items']:
                monkey['inspected'] += 1
                worry_level = monkey['items'].pop()
                operation_value = worry_level if value_string == 'old' else int(value_string)
                if operator_string == '+':
                    worry_level += operation_value
                elif operator_string == '*':
                    worry_level *= operation_value
                worry_level %= divisor_product
                worry_level //= relief
                throw_to = true_monkey if not worry_level % divisor else false_monkey
                monkeys[throw_to]['items'].append(worry_level)
    first_inspected, second_inspected = list(reversed(sorted(monkey['inspected'] for monkey in monkeys)))[0:2]
    return first_inspected * second_inspected


print(monkey_business())
print(monkey_business(10000, 1))
