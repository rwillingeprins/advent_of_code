def day01a():
    with open('input/day01.txt') as input_file:
        entries = []
        for line in input_file:
            current_entry = int(line)
            for entry in entries:
                if current_entry + entry == 2020:
                    return current_entry * entry
            entries.append(current_entry)


print(day01a())
