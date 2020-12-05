def get_sorted_seat_ids_from_file(file_path):
    with open(file_path) as file:
        return sorted(decode_seat_id(line.strip()) for line in file.readlines())


def decode_seat_id(boarding_pass):
    return int(''.join('1' if x in ('B', 'R') else '0' for x in boarding_pass), 2)


def day05a():
    seat_ids = get_sorted_seat_ids_from_file('input/day05.txt')
    return seat_ids[-1]


def day05b():
    seat_ids = get_sorted_seat_ids_from_file('input/day05.txt')
    for seat_index, seat_id in enumerate(seat_ids):
        next_seat = seat_id + 1
        if seat_ids[seat_index + 1] != next_seat:
            return next_seat


print(day05a())
print(day05b())
