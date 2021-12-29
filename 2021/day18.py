from copy import deepcopy


def add(x, y):
    return reduce([x, y])


def reduce(pair):
    while explode(pair) or split(pair):
        pass
    return pair


def explode(pair):
    for index1, element1 in enumerate(pair):
        if isinstance(element1, list):
            for index2, element2 in enumerate(element1):
                if isinstance(element2, list):
                    for index3, element3 in enumerate(element2):
                        if isinstance(element3, list):
                            for index4, element4 in enumerate(element3):
                                if isinstance(element4, list):
                                    x, y = element4
                                    if index4 == 1:
                                        left_add(pair[index1][index2][index3], x)
                                    elif index3 == 1:
                                        left_add(pair[index1][index2], x)
                                    elif index2 == 1:
                                        left_add(pair[index1], x)
                                    elif index1 == 1:
                                        left_add(pair, x)
                                    if index4 == 0:
                                        right_add(pair[index1][index2][index3], y)
                                    elif index3 == 0:
                                        right_add(pair[index1][index2], y)
                                    elif index2 == 0:
                                        right_add(pair[index1], y)
                                    elif index1 == 0:
                                        right_add(pair, y)
                                    pair[index1][index2][index3][index4] = 0
                                    return True
    return False


def left_add(pair, number):
    if isinstance(pair[0], int):
        pair[0] += number
    else:
        pair_add(pair[0], 1, number)


def right_add(pair, number):
    if isinstance(pair[1], int):
        pair[1] += number
    else:
        pair_add(pair[1], 0, number)


def pair_add(pair, index, number):
    if isinstance(pair[index], int):
        pair[index] += number
    else:
        pair_add(pair[index], index, number)


def split(pair):
    for index, element in enumerate(pair):
        if isinstance(element, int):
            regular_number = pair[index]
            if regular_number > 9:
                half = regular_number // 2
                pair[index] = [half, half + regular_number % 2]
                return True
        elif split(element):
            return True
    return False


def magnitude(element):
    if isinstance(element, int):
        return element
    x, y = element
    return 3 * magnitude(x) + 2 * magnitude(y)


with open('input/day18.txt') as file:
    pairs = [eval(line) for line in file.read().splitlines()]
final_sum, *remaining_pairs = pairs
while remaining_pairs:
    pair, *remaining_pairs = remaining_pairs
    final_sum = add(deepcopy(final_sum), deepcopy(pair))
print(magnitude(final_sum))

max_magnitude = 0
for x in pairs:
    for y in pairs:
        if x is not y:
            max_magnitude = max(max_magnitude, magnitude(add(deepcopy(x), deepcopy(y))))
print(max_magnitude)
