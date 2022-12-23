def mix(number_dicts):
    for number_dict in number_dicts:
        number = number_dict['number'] % (len(number_dicts) - 1)
        if number:
            number_dict['previous']['next'] = number_dict['next']
            number_dict['next']['previous'] = number_dict['previous']
            if number > 0:
                for _ in range(number):
                    number_dict['next'] = number_dict['next']['next']
                number_dict['previous'] = number_dict['next']['previous']
            if number < 0:
                for _ in range(abs(number)):
                    number_dict['previous'] = number_dict['previous']['previous']
                number_dict['next'] = number_dict['previous']['next']
            number_dict['previous']['next'] = number_dict
            number_dict['next']['previous'] = number_dict


def get_grove_coordinates(decryption_key=1, n_mixes=1):
    with open('input/day20.txt') as input_file:
        number_dicts = [{'number': int(line.strip()) * decryption_key} for line in input_file]
    for index, number_dict in enumerate(number_dicts):
        number_dict['previous'] = number_dicts[(index - 1) % len(number_dicts)]
        number_dict['next'] = number_dicts[(index + 1) % len(number_dicts)]
    for _ in range(n_mixes):
        mix(number_dicts)
    current_number_dict = next(number_dict for number_dict in number_dicts if number_dict['number'] == 0)
    grove_coordinates = []
    for _ in range(3):
        for _ in range(1000):
            current_number_dict = current_number_dict['next']
        grove_coordinates.append(current_number_dict['number'])
    return grove_coordinates


print(sum(get_grove_coordinates()))
print(sum(get_grove_coordinates(811589153, 10)))
