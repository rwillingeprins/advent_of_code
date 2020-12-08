class BootCode:
    def __init__(self, instructions):
        self.instructions = instructions
        self.instruction_index = 0
        self.accumulator = 0

    def run_instruction(self):
        operation, argument = self.instructions[self.instruction_index]
        if operation == 'acc':
            self.accumulator += argument
        elif operation == 'jmp':
            self.instruction_index += argument
            return
        elif operation == 'nop':
            pass
        self.instruction_index += 1

    def run_no_repeat(self):
        seen_indices = set()
        while self.instruction_index < len(self.instructions):
            if self.instruction_index in seen_indices:
                return False
            seen_indices.add(self.instruction_index)
            self.run_instruction()
        return True


def parse_boot_code_instructions_from_file(file_path):
    instructions = []
    with open(file_path) as file:
        for line in file:
            operation, argument = line.strip().split(' ')
            instructions.append((operation, int(argument)))
    return instructions


def day08a():
    instructions = parse_boot_code_instructions_from_file('input/day08.txt')
    boot_code = BootCode(instructions)
    boot_code.run_no_repeat()
    return boot_code.accumulator


def day08b():
    instructions = parse_boot_code_instructions_from_file('input/day08.txt')
    operation_switch = {'jmp': 'nop', 'nop': 'jmp'}
    for instruction_index, (operation, argument) in enumerate(instructions):
        if operation in operation_switch:
            new_instructions = instructions.copy()
            new_instructions[instruction_index] = (operation_switch[operation], argument)
            boot_code = BootCode(new_instructions)
            if boot_code.run_no_repeat():
                return boot_code.accumulator


print(day08a())
print(day08b())
