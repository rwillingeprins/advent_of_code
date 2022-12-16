import re


def manhattan_distance(point1, point2):
    return sum(abs(point2[dimension] - point1[dimension]) for dimension in range(2))


row = 2000000
row_coverage = {}
range_per_sensor = {}
with open('input/day15.txt') as input_file:
    for line in input_file:
        sensor_x, sensor_y, beacon_x, beacon_y = map(int, re.findall(r'(-?\d+)', line))
        sensor_range = manhattan_distance((sensor_x, sensor_y), (beacon_x, beacon_y))
        x_distance = sensor_range - abs(row - sensor_y)
        if x_distance >= 0:
            for x in range(sensor_x - x_distance, sensor_x + x_distance + 1):
                row_coverage.setdefault(x, False)
        if beacon_y == row:
            row_coverage[beacon_x] = True
        range_per_sensor[(sensor_x, sensor_y)] = sensor_range
print(sum(not is_beacon for is_beacon in row_coverage.values()))
sensors = list(range_per_sensor.keys())
possible_beacon_position_sets = []
for sensor_index, sensor1 in enumerate(sensors[:-1]):
    for sensor2 in sensors[sensor_index + 1:]:
        sensor_distance = manhattan_distance(sensor1, sensor2)
        if sensor_distance - range_per_sensor[sensor1] - range_per_sensor[sensor2] == 2:
            (x1, y1), (x2, y2) = sorted((sensor1, sensor2), key=lambda sensor: range_per_sensor[sensor])
            distress_signal_distance = range_per_sensor[(x1, y1)] + 1
            max_x_distance = min(abs(x2 - x1), distress_signal_distance)
            x_sign = -1 if x1 > x2 else 1
            y_sign = -1 if y1 > y2 else 1
            possible_beacon_positions = []
            for x_distance in range(max_x_distance):
                x = x1 + (x_sign * x_distance)
                y_distance = distress_signal_distance - x_distance
                y = y1 + (y_sign * y_distance)
                if 0 <= x <= 4000000 and 0 <= y <= 4000000:
                    possible_beacon_positions.append((x, y))
            possible_beacon_position_sets.append(set(possible_beacon_positions))
distress_signal_x, distress_signal_y = next(iter(set.intersection(*possible_beacon_position_sets)))
print(distress_signal_x * 4000000 + distress_signal_y)
