class Amplifier:
    def __init__(self, intcode, phase):
        self.intcode = intcode
        self.phase = phase
        self.phase_is_set = False

    def amplify(self, input_signal):
        inputs = []
        if not self.phase_is_set:
            inputs.append(self.phase)
            self.phase_is_set = True
        inputs.append(input_signal)
        return run_intcode(self.intcode, inputs)


class IntcodeComputer:
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

    def __init__(self, intcode, phase):
        self.intcode = intcode

    def get_parameters(self):
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

    def add(self, a, b, output_address):
        self.intcode[output_address] = a+b

    def multiply(self, a, b, output_address):
        self.intcode[output_address] = a*b

    def run_intcode(self, intcode, inputs):
        instruction_pointer = 0
        while instruction_pointer < len(intcode):
            instruction = intcode[instruction_pointer]
            modes_code, opcode = divmod(instruction, 100)
            if opcode == 99:
                break
            parameter_types = self.parameter_types_per_opcode.get(opcode, 0)
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
            print(instruction, parameters)
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


def run_amplifier_feedback_loop(amplifier_program, phase_settings):
    amplifiers = [Amplifier(amplifier_program[:], phase) for phase in phase_settings]
    signal = 0
    output_signal = 0
    while True:
        for amplifier in amplifiers:
            signal = amplifier.amplify(signal)
            print(signal)
            if signal is None:
                return output_signal
        output_signal = signal


with open('test.txt') as input_file:
    input_string = input_file.readline()
input_integers = [int(x) for x in input_string.split(',')]
phase_settings = [5, 6, 7, 8, 9]
max_output_signal = 0
for permutation in permutate(phase_settings):
    output_signal = run_amplifier_feedback_loop(input_integers, permutation)
    if output_signal > max_output_signal:
        max_output_signal = output_signal
print(max_output_signal)
