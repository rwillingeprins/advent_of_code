class IntcodeProgram:
    def __init__(self, intcode, input_list=None):
        self.intcode = intcode
        self.input_list = input_list or []
        self.instruction_address = 0
        self.relative_base = 0

    @property
    def instruction(self):
        return self.get(self.instruction_address)

    @property
    def opcode(self):
        return self.instruction % 100

    def get(self, address):
        return self.intcode.get(address, 0)

    def parameter_mode(self, parameter_number):
        return (self.instruction // (10 ** (parameter_number + 1))) % 10

    def immediate_address(self, parameter_number):
        return self.instruction_address + parameter_number

    def position_address(self, parameter_number):
        return self.get(self.immediate_address(parameter_number))

    def relative_address(self, parameter_number):
        return self.relative_base + self.position_address(parameter_number)

    def parameter(self, number):
        mode = self.parameter_mode(number)
        address = 0
        if mode == 0:
            address = self.position_address(number)
        elif mode == 1:
            address = self.immediate_address(number)
        elif mode == 2:
            address = self.relative_address(number)
        return self.get(address)

    def parameter_write(self, parameter_number, value):
        address = self.position_address(parameter_number)
        self.intcode[address] = value

    def run(self):
        while True:
            if self.opcode == 1:
                value = self.parameter(1) + self.parameter(2)
                self.parameter_write(3, value)
                self.instruction_address += 4
            elif self.opcode == 2:
                value = self.parameter(1) * self.parameter(2)
                self.parameter_write(3, value)
                self.instruction_address += 4
            elif self.opcode == 3:
                if self.input_list:
                    value = self.input_list.pop(0)
                else:
                    value = int(input())
                self.parameter_write(1, value)
                self.instruction_address += 2
            elif self.opcode == 4:
                value = self.parameter(1)
                self.instruction_address += 2
                return value
            elif self.opcode == 5:
                if self.parameter(1):
                    self.instruction_address = self.parameter(2)
                else:
                    self.instruction_address += 3
            elif self.opcode == 6:
                if not self.parameter(1):
                    self.instruction_address = self.parameter(2)
                else:
                    self.instruction_address += 3
            elif self.opcode == 7:
                value = int(self.parameter(1) < self.parameter(2))
                self.parameter_write(3, value)
                self.instruction_address += 4
            elif self.opcode == 8:
                value = int(self.parameter(1) == self.parameter(2))
                self.parameter_write(3, value)
                self.instruction_address += 4
            elif self.opcode == 9:
                self.relative_base += self.parameter(1)
                self.instruction_address += 2
            else:
                break


with open('day09.txt') as input_file:
    input_string = input_file.readline()

input_code = {i: int(x) for i, x in enumerate(input_string.split(','))}
boost_program = IntcodeProgram(input_code, [1])
print(boost_program.run())
