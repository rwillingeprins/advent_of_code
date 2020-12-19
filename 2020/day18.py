import re

parentheses_pattern = re.compile(r'\(([^()]+)\)')
operation_pattern = re.compile(r'(\d+)([+*])(\d+)')
addition_pattern = re.compile(r'(\d+)\+(\d+)')
multiplication_pattern = re.compile(r'(\d+)\*(\d+)')


def operate(operator, a, b):
    if operator == '+':
        return a + b
    if operator == '*':
        return a * b


def evaluate(expression, pattern_evaluators):
    for pattern, evaluator in pattern_evaluators:
        m = pattern.search(expression)
        if m:
            evaluated = evaluator(m)
            if m.group() == expression:
                return evaluated
            expression = expression[:m.start()] + str(evaluated) + expression[m.end():]
            return evaluate(expression, pattern_evaluators)


def evaluate_math(expression):
    pattern_evaluators = [
        (parentheses_pattern, lambda m: evaluate_math(m.group(1))),
        (operation_pattern, lambda m: operate(m.group(2), int(m.group(1)), int(m.group(3)))),
    ]
    return evaluate(expression, pattern_evaluators)


def evaluate_advanced_math(expression):
    pattern_evaluators = [
        (parentheses_pattern, lambda m: evaluate_advanced_math(m.group(1))),
        (addition_pattern, lambda m: int(m.group(1)) + int(m.group(2))),
        (multiplication_pattern, lambda m: int(m.group(1)) * int(m.group(2))),
    ]
    return evaluate(expression, pattern_evaluators)


def day18a():
    with open('input/day18.txt') as file:
        expressions = file.read().replace(' ', '').splitlines()
    return sum(evaluate_math(expression) for expression in expressions)


def day18b():
    with open('input/day18.txt') as file:
        expressions = file.read().replace(' ', '').splitlines()
    return sum(evaluate_advanced_math(expression) for expression in expressions)


print(day18a())
print(day18b())
