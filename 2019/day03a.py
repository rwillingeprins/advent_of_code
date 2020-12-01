def find_wire_intersections(wires):
    intersections = []
    wire_cell_dicts = []
    for wire_steps in wires:
        x, y = 0, 0
        current_wire_cell_dict = {(x, y): True}
        for step in wire_steps:
            direction = step[0]
            distance = int(step[1:])
            while distance > 0:
                distance -= 1
                if direction == 'R':
                    x += 1
                elif direction == 'L':
                    x -= 1
                elif direction == 'U':
                    y += 1
                elif direction == 'D':
                    y -= 1
                for wire_cell_dict in wire_cell_dicts:
                    if (x, y) in wire_cell_dict:
                        intersections.append((x, y))
                current_wire_cell_dict[x, y] = True
        wire_cell_dicts.append(current_wire_cell_dict)
    return intersections


def manhattan_distance(coordinates):
    x, y = coordinates
    return abs(x) + abs(y)


def find_minimal_manhattan_distance(coordinates_list):
    minimal_manhattan = manhattan_distance(coordinates_list[0])
    for coordinates in coordinates_list:
        manhattan = manhattan_distance(coordinates)
        if manhattan < minimal_manhattan:
            minimal_manhattan = manhattan
    return minimal_manhattan


with open('day03.txt') as input_file:
    first_wire_steps = input_file.readline().split(',')
    second_wire_steps = input_file.readline().split(',')
wire_intersections = find_wire_intersections([first_wire_steps, second_wire_steps])
print(find_minimal_manhattan_distance(wire_intersections))
