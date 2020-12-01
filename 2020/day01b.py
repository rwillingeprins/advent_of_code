def day01b():
    with open('input/day01.txt') as input_file:
        entries = []
        pairs = []
        for line in input_file:
            current_entry = int(line)
            for entry1, entry2 in pairs:
                if current_entry + entry1 + entry2 == 2020:
                    return current_entry * entry1 * entry2
            pairs.extend([(current_entry, entry) for entry in entries])
            entries.append(current_entry)


print(day01b())
