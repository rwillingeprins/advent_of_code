def parse_train_ticket_notes(file_path):
    with open(file_path) as file:
        rules_string, my_ticket_string, other_tickets_string = file.read().split('\n\n', 3)
    ranges_per_field = {}
    for rule_line in rules_string.splitlines():
        field, ranges_string = rule_line.split(': ', 2)
        ranges = []
        for range_string in ranges_string.split(' or '):
            minimum, maximum = range_string.split('-')
            ranges.append((int(minimum), int(maximum)))
        ranges_per_field[field] = ranges
    my_ticket = [int(value) for value in my_ticket_string.splitlines()[1].split(',')]
    other_tickets = [[int(value) for value in line.split(',')] for line in other_tickets_string.splitlines()[1:]]
    return ranges_per_field, my_ticket, other_tickets


def value_in_any_range(value, ranges):
    return any(minimum <= value <= maximum for minimum, maximum in ranges)


def get_error_rate_per_ticket(tickets, valid_ranges):
    error_rates = []
    for ticket in tickets:
        error_rate = 0
        for value in ticket:
            if not value_in_any_range(value, valid_ranges):
                error_rate += value
        error_rates.append(error_rate)
    return error_rates


def day16a():
    ranges_per_field, _, other_tickets = parse_train_ticket_notes('input/day16.txt')
    all_ranges = {min_max for ranges in ranges_per_field.values() for min_max in ranges}
    return sum(get_error_rate_per_ticket(other_tickets, all_ranges))


def day16b():
    ranges_per_field, my_ticket, other_tickets = parse_train_ticket_notes('input/day16.txt')
    all_ranges = {min_max for ranges in ranges_per_field.values() for min_max in ranges}
    ticket_error_rates = get_error_rate_per_ticket(other_tickets, all_ranges)
    field_value_indices = range(len(my_ticket))
    possible_field_sets = [set(ranges_per_field.keys()) for _ in field_value_indices]
    for ticket_index, ticket_values in enumerate(other_tickets):
        if ticket_error_rates[ticket_index] > 0:
            continue
        for value_index, value in enumerate(ticket_values):
            for field in list(possible_field_sets[value_index]):
                if not value_in_any_range(value, ranges_per_field[field]):
                    possible_field_sets[value_index].remove(field)
    unknown_field_value_indices = set(field_value_indices)
    value_index_per_field = {}
    while unknown_field_value_indices:
        for value_index in list(unknown_field_value_indices):
            possible_field_sets[value_index] -= set(value_index_per_field.keys())
            if len(possible_field_sets[value_index]) == 1:
                (field,) = possible_field_sets[value_index]
                value_index_per_field[field] = value_index
                unknown_field_value_indices.remove(value_index)
    answer = 1
    for field, value_index in value_index_per_field.items():
        if field.startswith('departure'):
            answer *= my_ticket[value_index]
    return answer


print(day16a())
print(day16b())
