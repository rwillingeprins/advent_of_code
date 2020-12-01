class IntcodeProgram:
    def __init__(self, intcode, input_list):
        self.intcode = intcode
        self.input_list = input_list
        self.instruction_pointer = 0

    @property
    def instruction(self):
        return self.intcode[self.instruction_pointer]

    @property
    def opcode(self):
        return self.instruction % 100

    def parameter_mode(self, parameter_number):
        return (self.instruction // (10 ** (parameter_number + 1))) % 10

    def immediate_parameter(self, parameter_number):
        parameter_position = self.instruction_pointer + parameter_number
        return self.intcode[parameter_position]

    def position_parameter(self, parameter_number):
        parameter_position = self.immediate_parameter(parameter_number)
        return self.intcode[parameter_position]

    def parameter(self, number):
        mode = self.parameter_mode(number)
        if mode == 0:
            return self.position_parameter(number)
        elif mode == 1:
            return self.immediate_parameter(number)

    def parameter_write(self, parameter_number, value):
        self.intcode[self.immediate_parameter(parameter_number)] = value

    def run(self):
        while self.instruction_pointer < len(self.intcode):
            if self.opcode == 1:
                value = self.parameter(1) + self.parameter(2)
                self.parameter_write(3, value)
                self.instruction_pointer += 4
            elif self.opcode == 2:
                value = self.parameter(1) * self.parameter(2)
                self.parameter_write(3, value)
                self.instruction_pointer += 4
            elif self.opcode == 3:
                if self.input_list:
                    value = self.input_list.pop(0)
                else:
                    value = int(input())
                self.parameter_write(1, value)
                self.instruction_pointer += 2
            elif self.opcode == 4:
                value = self.parameter(1)
                self.instruction_pointer += 2
                return value
            elif self.opcode == 5:
                if self.parameter(1):
                    self.instruction_pointer = self.parameter(2)
            elif self.opcode == 6:
                if not self.parameter(1):
                    self.instruction_pointer = self.parameter(2)
            elif self.opcode == 7:
                value = int(self.parameter(1) < self.parameter(2))
                self.parameter_write(3, value)
                self.instruction_pointer += 4
            elif self.opcode == 8:
                value = int(self.parameter(1) == self.parameter(2))
                self.parameter_write(3, value)
                self.instruction_pointer += 4
            else:
                break


class Amplifier:
    def __init__(self, phase, intcode):
        self.phase = phase
        self.intcode_program = IntcodeProgram(intcode, [phase])

    def amplify(self, input_signal):
        self.intcode_program.input_list.append(input_signal)
        output_signal = self.intcode_program.run()
        return output_signal


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
    amplifiers = [Amplifier(phase, amplifier_program[:]) for phase in phase_settings]
    signal = 0
    output_signal = 0
    while True:
        for amplifier in amplifiers:
            signal = amplifier.amplify(signal)
            if signal is None:
                return output_signal
        output_signal = signal


with open('input/day07.txt') as input_file:
    input_string = input_file.readline()
input_integers = [int(x) for x in input_string.split(',')]
phase_settings = [5, 6, 7, 8, 9]
max_output_signal = 0
for permutation in permutate(phase_settings):
    output_signal = run_amplifier_feedback_loop(input_integers, permutation)
    if output_signal > max_output_signal:
        max_output_signal = output_signal
print(max_output_signal)
