def memory_game(starting_numbers, n_turns):
    *starting_numbers, number = starting_numbers
    latest_turn_per_number = dict((number, turn) for turn, number in enumerate(starting_numbers))
    for turn in range(len(starting_numbers), n_turns - 1):
        age = turn - latest_turn_per_number.get(number, turn)
        latest_turn_per_number[number] = turn
        number = age
    return number


def day15a():
    return memory_game([1, 0, 15, 2, 10, 13], 2020)


def day15b():
    return memory_game([1, 0, 15, 2, 10, 13], 30000000)


print(day15a())
print(day15b())
