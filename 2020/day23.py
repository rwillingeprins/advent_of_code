def day23a():
    cups = 1, 9, 3, 4, 6, 7, 2, 5, 8
    for _ in range(100):
        moved_cups = cups[1:4]
        destination_cup = cups[0] - 1
        while destination_cup == 0 or destination_cup in moved_cups:
            destination_cup = (destination_cup - 1) % 10
        destination_index = cups.index(destination_cup)
        cups = cups[4:destination_index + 1] + moved_cups + cups[destination_index + 1:] + cups[0:1]
    one_index = cups.index(1)
    return ''.join(map(str, cups[one_index + 1:] + cups[:one_index]))


def day23b():
    cups = 1, 9, 3, 4, 6, 7, 2, 5, 8
    max_cup = 1000000
    n_moves = 10000000
    cups += tuple(range(max(cups), max_cup + 1))
    current_cup = cups[0]
    cup = max_cup
    neighbor_per_cup = {}
    for next_cup in cups:
        neighbor_per_cup[cup] = next_cup
        cup = next_cup
    for _ in range(n_moves):
        first_neighbor = neighbor_per_cup[current_cup]
        second_neighbor = neighbor_per_cup[first_neighbor]
        third_neighbor = neighbor_per_cup[second_neighbor]
        fourth_neighbor = neighbor_per_cup[third_neighbor]
        moved_cups = (first_neighbor, second_neighbor, third_neighbor)
        destination_cup = current_cup - 1
        while destination_cup == 0 or destination_cup in moved_cups:
            if destination_cup == 0:
                destination_cup = max_cup
            else:
                destination_cup -= 1
        destination_neighbor = neighbor_per_cup[destination_cup]
        neighbor_per_cup[current_cup] = fourth_neighbor
        neighbor_per_cup[destination_cup] = first_neighbor
        neighbor_per_cup[third_neighbor] = destination_neighbor
        current_cup = fourth_neighbor
    first_one_neighbor = neighbor_per_cup[1]
    second_one_neighbor = neighbor_per_cup[first_one_neighbor]
    return first_one_neighbor * second_one_neighbor


print(day23a())
print(day23b())
