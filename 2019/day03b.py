def find_wire_intersections(wires):
    fewest_combined_steps = -1
    wire_cell_dicts = []
    for wire_steps in wires:
        x, y = 0, 0
        total_distance = 0
        current_wire_cell_dict = {(x, y): total_distance}
        for vector in wire_steps:
            direction = vector[0]
            distance = int(vector[1:])
            while distance > 0:
                distance -= 1
                total_distance += 1
                if direction == 'R':
                    x += 1
                elif direction == 'L':
                    x -= 1
                elif direction == 'U':
                    y += 1
                elif direction == 'D':
                    y -= 1
                if (x, y) not in current_wire_cell_dict:
                    for wire_cell_dict in wire_cell_dicts:
                        if (x, y) in wire_cell_dict:
                            combined_steps = wire_cell_dict[x, y] + total_distance
                            if fewest_combined_steps == -1 or combined_steps < fewest_combined_steps:
                                fewest_combined_steps = combined_steps
                    current_wire_cell_dict[x, y] = total_distance
        wire_cell_dicts.append(current_wire_cell_dict)
    return fewest_combined_steps


with open('day03.txt') as input_file:
    first_wire_steps = input_file.readline().split(',')
    second_wire_steps = input_file.readline().split(',')
print(find_wire_intersections([first_wire_steps, second_wire_steps]))
