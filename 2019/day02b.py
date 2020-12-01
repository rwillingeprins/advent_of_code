def run_intcode(integers, noun, verb):
    integers[1] = noun
    integers[2] = verb
    instruction_pointer = 0
    while instruction_pointer < len(integers):
        opcode = integers[instruction_pointer]
        if opcode == 99:
            break
        parameters = integers[instruction_pointer + 1: instruction_pointer + 4]
        first_input_address = parameters[0]
        second_input_address = parameters[1]
        output_address = parameters[2]
        if opcode == 1:
            integers[output_address] = integers[first_input_address] + integers[second_input_address]
        elif opcode == 2:
            integers[output_address] = integers[first_input_address] * integers[second_input_address]
        instruction_pointer += 4
    return integers[0]


with open('day02.txt') as input_file:
    input_string = input_file.readline()
input_integers = [int(x) for x in input_string.split(',')]
for n in range(100):
    for v in range(100):
        output = run_intcode(input_integers[:], n, v)
        if output == 19690720:
            result = 100 * n + v
            print(result)
            break
