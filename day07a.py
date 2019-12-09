def run_intcode(intcode, inputs):
    parameter_types_per_opcode = {
        1: [False, False, True],
        2: [False, False, True],
        3: [True],
        4: [False],
        5: [False, False],
        6: [False, False],
        7: [False, False, True],
        8: [False, False, True]
    }
    instruction_pointer = 0
    while instruction_pointer < len(intcode):
        instruction = intcode[instruction_pointer]
        modes_code, opcode = divmod(instruction, 100)
        if opcode == 99:
            break
        parameter_types = parameter_types_per_opcode.get(opcode, 0)
        n_parameters = len(parameter_types)
        parameters = []
        for i in range(n_parameters):
            modes_code, mode = divmod(modes_code, 10)
            parameter = intcode[instruction_pointer + 1 + i]
            is_write_parameter = parameter_types[i]
            if mode == 1 or is_write_parameter:
                parameters.append(parameter)
            else:
                parameters.append(intcode[parameter])
        if opcode == 1:
            intcode[parameters[2]] = parameters[0] + parameters[1]
        elif opcode == 2:
            intcode[parameters[2]] = parameters[0] * parameters[1]
        elif opcode == 3:
            if inputs:
                intcode[parameters[0]] = inputs.pop(0)
            else:
                print('Input:')
                intcode[parameters[0]] = int(input())
        elif opcode == 4:
            return parameters[0]
        elif opcode == 5:
            if parameters[0]:
                instruction_pointer = parameters[1]
                continue
        elif opcode == 6:
            if not parameters[0]:
                instruction_pointer = parameters[1]
                continue
        elif opcode == 7:
            if parameters[0] < parameters[1]:
                intcode[parameters[2]] = 1
            else:
                intcode[parameters[2]] = 0
        elif opcode == 8:
            if parameters[0] == parameters[1]:
                intcode[parameters[2]] = 1
            else:
                intcode[parameters[2]] = 0
        instruction_pointer += 1 + n_parameters


def permutate(values):
    permutations = []
    if values:
        for index, value in enumerate(values):
            remaining_values = values[:index] + values[index + 1:]
            if remaining_values:
                remaining_permutations = permutate(remaining_values)
                permutations.extend([[value] + permutation for permutation in remaining_permutations])
            else:
                permutations.append([value])
    return permutations


with open('day07.txt') as input_file:
    input_string = input_file.readline()
input_integers = [int(x) for x in input_string.split(',')]
phase_settings = [0, 1, 2, 3, 4]
max_output_signal = 0
for permutation in permutate(phase_settings):
    signal = 0
    for phase_setting in permutation:
        signal = run_intcode(input_integers[:], [phase_setting, signal])
    if signal > max_output_signal:
        max_output_signal = signal
print(max_output_signal)
