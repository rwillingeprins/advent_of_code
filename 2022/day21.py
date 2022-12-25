root = 'root'
human = 'humn'
number_per_monkey = {}
operation_per_monkey = {}
listener_per_monkey = {}
with open('input/day21.txt') as input_file:
    for line in input_file:
        monkey, task = line.strip().split(': ')
        try:
            number_per_monkey[monkey] = int(task)
        except ValueError:
            operation_per_monkey[monkey] = (monkey1, operator, monkey2) = task.split()
            listener_per_monkey[monkey1] = monkey
            listener_per_monkey[monkey2] = monkey


def yell(monkey):
    try:
        return number_per_monkey[monkey]
    except:
        monkey1, operator, monkey2 = operation_per_monkey[monkey]
        number1 = yell(monkey1)
        number2 = yell(monkey2)
        match operator:
            case '+':
                return number1 + number2
            case '-':
                return number1 - number2
            case '*':
                return number1 * number2
            case '/':
                return number1 // number2


print(yell(root))

human_listeners = set()
human_listener = human
while human_listener:
    human_listeners.add(human_listener)
    human_listener = listener_per_monkey.get(human_listener)


def predict(monkey, target_number):
    if monkey == human:
        return target_number
    monkey1, operator, monkey2 = operation_per_monkey[monkey]
    if monkey1 in human_listeners:
        match operator:
            case '+':
                return predict(monkey1, target_number - yell(monkey2))
            case '-':
                return predict(monkey1, target_number + yell(monkey2))
            case '*':
                return predict(monkey1, target_number // yell(monkey2))
            case '/':
                return predict(monkey1, target_number * yell(monkey2))
    else:
        match operator:
            case '+':
                return predict(monkey2, target_number - yell(monkey1))
            case '-':
                return predict(monkey2, yell(monkey1) - target_number)
            case '*':
                return predict(monkey2, target_number // yell(monkey1))
            case '/':
                return predict(monkey2, yell(monkey2) // target_number)


root_monkey1, _, root_monkey2 = operation_per_monkey[root]
if root_monkey1 in human_listeners:
    print(predict(root_monkey1, yell(root_monkey2)))
else:
    print(predict(root_monkey2, yell(root_monkey1)))
