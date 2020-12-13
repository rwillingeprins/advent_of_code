def parse_bus_notes(file_path):
    with open(file_path) as file:
        earliest_departure = int(file.readline().strip())
        bus_id_list = file.readline().strip().split(',')
    return earliest_departure, bus_id_list


def day13a():
    earliest_departure, bus_id_list = parse_bus_notes('input/day13.txt')
    bus_ids = [int(bus_id) for bus_id in bus_id_list if bus_id != 'x']
    earliest_bus_id = None
    shortest_waiting_time = max(bus_ids)
    for bus_id in bus_ids:
        waiting_time = bus_id - (earliest_departure % bus_id)
        if waiting_time < shortest_waiting_time:
            earliest_bus_id = bus_id
            shortest_waiting_time = waiting_time
    return earliest_bus_id * shortest_waiting_time


def day13b():
    _, bus_id_list = parse_bus_notes('input/day13.txt')
    offset_for_bus_id = dict((int(bus_id), offset) for offset, bus_id in enumerate(bus_id_list) if bus_id != 'x')
    timestamp = time_step = 1
    for bus_id, offset in offset_for_bus_id.items():
        while not (timestamp + offset) % bus_id == 0:
            timestamp += time_step
        time_step *= bus_id
    return timestamp


print(day13a())
print(day13b())
