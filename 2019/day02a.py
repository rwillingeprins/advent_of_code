def run_intcode(integers):
    opcode_position = 0
    while opcode_position < len(integers):
        opcode = integers[opcode_position]
        if opcode == 99:
            break
        first_input_position = integers[opcode_position + 1]
        second_input_position = integers[opcode_position + 2]
        output_position = integers[opcode_position + 3]
        if opcode == 1:
            integers[output_position] = integers[first_input_position] + integers[second_input_position]
        elif opcode == 2:
            integers[output_position] = integers[first_input_position] * integers[second_input_position]
        opcode_position += 4


with open('input/day02.txt') as input_file:
    input_string = input_file.readline()
input_integers = [int(x) for x in input_string.split(',')]
input_integers[1] = 12
input_integers[2] = 2
run_intcode(input_integers)
print(input_integers[0])
