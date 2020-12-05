def get_seat_ids_from_file(file_path):
    with open(file_path) as file:
        return sorted([decode_seat_id(line.strip()) for line in file.readlines()])


def decode_seat_id(boarding_pass):
    row = int(''.join([str(int(x == 'B')) for x in boarding_pass[:7]]), 2)
    column = int(''.join([str(int(x == 'R')) for x in boarding_pass[7:10]]), 2)
    seat_id = 8 * row + column
    return seat_id


def day05a():
    seat_ids = get_seat_ids_from_file('input/day05.txt')
    return seat_ids[-1]


def day05b():
    seat_ids = get_seat_ids_from_file('input/day05.txt')
    for seat_index, seat_id in enumerate(seat_ids):
        next_seat = seat_id + 1
        if seat_ids[seat_index + 1] != next_seat:
            return next_seat


print(day05a())
print(day05b())
