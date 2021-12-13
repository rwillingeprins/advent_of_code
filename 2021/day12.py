connections_per_cave = {}
with open('input/day12.txt') as file:
    for line in file.read().splitlines():
        cave1, cave2 = line.split('-')
        connections_per_cave.setdefault(cave1, [])
        connections_per_cave[cave1].append(cave2)
        connections_per_cave.setdefault(cave2, [])
        connections_per_cave[cave2].append(cave1)


def find_paths1(visited_caves):
    paths = []
    current_cave = visited_caves[-1]
    if current_cave == 'end':
        paths.append(visited_caves)
    else:
        for connected_cave in connections_per_cave.get(current_cave, []):
            if connected_cave.isupper() or connected_cave not in visited_caves:
                paths.extend(find_paths1(visited_caves + [connected_cave]))
    return paths


print(len(find_paths1(['start'])))


def find_paths2(visited_caves):
    paths = []
    current_cave = visited_caves[-1]
    if current_cave == 'end':
        paths.append(visited_caves)
    else:
        visit_count_per_cave = {}
        for cave in visited_caves:
            visit_count_per_cave[cave] = visit_count_per_cave.get(cave, 0) + 1
        visited_small_cave_twice = any(cave.islower() and count == 2 for cave, count in visit_count_per_cave.items())
        for connected_cave in connections_per_cave.get(current_cave, []):
            if (
                    connected_cave.isupper() or
                    connected_cave not in visited_caves or
                    connected_cave != 'start' and not visited_small_cave_twice
            ):
                paths.extend(find_paths2(visited_caves + [connected_cave]))
    return paths


print(len(find_paths2(['start'])))
