class IntcodeProgram:
    def __init__(self, initial_code, input_list=None):
        self.code = {i: x for i, x in enumerate(initial_code)}
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
        return self.code.get(address, 0)

    def parameter_mode(self, parameter_number):
        return (self.instruction // (10 ** (parameter_number + 1))) % 10

    def immediate_address(self, parameter_number):
        return self.instruction_address + parameter_number

    def position_address(self, parameter_number):
        return self.get(self.immediate_address(parameter_number))

    def relative_address(self, parameter_number):
        return self.relative_base + self.position_address(parameter_number)

    def parameter_address(self, number):
        mode = self.parameter_mode(number)
        address = 0
        if mode == 0:
            address = self.position_address(number)
        elif mode == 1:
            address = self.immediate_address(number)
        elif mode == 2:
            address = self.relative_address(number)
        return address

    def parameter(self, number):
        address = self.parameter_address(number)
        return self.get(address)

    def parameter_write(self, parameter_number, value):
        address = self.parameter_address(parameter_number)
        self.code[address] = value

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


class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.facing = 0

    @property
    def position(self):
        return self.x, self.y

    def rotate(self, direction):
        if direction == 0:
            self.facing = (self.facing + 3) % 4
        elif direction == 1:
            self.facing = (self.facing + 1) % 4

    def move(self):
        if self.facing == 0:
            self.y += 1
        elif self.facing == 1:
            self.x += 1
        elif self.facing == 2:
            self.y -= 1
        elif self.facing == 3:
            self.x -= 1


with open('day11.txt') as input_file:
    input_string = input_file.readline()
input_code = [int(x) for x in input_string.split(',')]
painting_program = IntcodeProgram(input_code)
robot = Robot()
grid_colors = {(0, 0): 1}
while True:
    tile_color = grid_colors.get(robot.position, 0)
    painting_program.input_list = [tile_color]
    paint_color = painting_program.run()
    if paint_color is None:
        break
    grid_colors[robot.position] = paint_color
    painting_program.input_list = [paint_color]
    direction = painting_program.run()
    if direction is None:
        break
    robot.rotate(direction)
    robot.move()
x_min = x_max = y_min = y_max = 0
for (x, y) in grid_colors.keys():
    if x < x_min:
        x_min = x
    elif x > x_max:
        x_max = x
    if y < y_min:
        y_min = y
    elif y > y_max:
        y_max = y
for y in range(y_max, y_min - 1, -1):
    line = ''
    for x in range(x_min, x_max + 1):
        if grid_colors.get((x, y), 0) == 1:
            line += '#'
        else:
            line += ' '
    print(line)
