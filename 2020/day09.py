def parse_number_series_from_file(file_path):
    with open(file_path) as file:
        return [int(line.strip()) for line in file]


def number_is_sum_of_pair_in_list(number, number_list):
    for addend_index, addend in enumerate(number_list[:len(number_list) - 1]):
        if number - addend in number_list[addend_index + 1:]:
            return True
    return False


def find_invalid_number_in_series(number_series, preamble_length=25):
    for number_index in range(preamble_length, len(number_series)):
        number = number_series[number_index]
        if not number_is_sum_of_pair_in_list(number, number_series[number_index - preamble_length:number_index]):
            return number


def day09a():
    number_series = parse_number_series_from_file('input/day09.txt')
    return find_invalid_number_in_series(number_series)


def day09b():
    number_series = parse_number_series_from_file('input/day09.txt')
    invalid_number = find_invalid_number_in_series(number_series)
    n_numbers = len(number_series)
    for start_index in range(n_numbers):
        for stop_index in range(start_index + 1, n_numbers):
            contiguous_numbers = number_series[start_index:stop_index]
            contiguous_sum = sum(contiguous_numbers)
            if contiguous_sum > invalid_number:
                break
            elif contiguous_sum == invalid_number:
                return min(contiguous_numbers) + max(contiguous_numbers)


print(day09a())
print(day09b())
