with open('input/day18.txt') as input_file:
    cubes = set([tuple(map(int, line.split(','))) for line in input_file.readlines()])
adjacent = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
print(sum(((x + xa, y + ya, z + za) not in cubes) for x, y, z in cubes for xa, ya, za in adjacent))
max_point = [max(cube[dim] for cube in cubes) for dim in (0, 1, 2)]
steam = set()
exterior_surface_area = 0
steam_front = {(0, 0, 0)}
while steam_front:
    steam.update(steam_front)
    next_steam_front = set()
    for x, y, z in steam_front:
        for xa, ya, za in adjacent:
            adjacent_point = (x + xa, y + ya, z + za)
            if all(-1 <= adjacent_point[dim] <= max_point[dim] + 1 for dim in (0, 1, 2)):
                if adjacent_point in cubes:
                    exterior_surface_area += 1
                elif adjacent_point not in steam:
                    next_steam_front.add(adjacent_point)
    steam_front = next_steam_front
print(exterior_surface_area)
