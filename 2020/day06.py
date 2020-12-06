def get_answer_sets_from_file(file_path):
    with open(file_path) as file:
        return [[set(person) for person in group.split('\n')] for group in file.read().strip().split('\n\n')]


def day06a():
    answers = get_answer_sets_from_file('input/day06.txt')
    return sum(len(set.union(*group_answers)) for group_answers in answers)


def day06b():
    answers = get_answer_sets_from_file('input/day06.txt')
    return sum(len(set.intersection(*group_answers)) for group_answers in answers)


print(day06a())
print(day06b())
