with open('input/day09.txt') as file:
    heightmap = [[int(height) for height in line.strip()] for line in file]


def get_neighbors(row, col):
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))
    if col > 0:
        neighbors.append((row, col - 1))
    if row < len(heightmap) - 1:
        neighbors.append((row + 1, col))
    if col < len(heightmap[0]) - 1:
        neighbors.append((row, col + 1))
    return neighbors


low_points = []
for row, row_heights in enumerate(heightmap):
    for col, height in enumerate(row_heights):
        if all(heightmap[r][c] > height for r, c in get_neighbors(row, col)):
            low_points.append((row, col))
print(sum(heightmap[row][col] + 1 for row, col in low_points))


def get_basin_points(row, col):
    basin_points = {(row, col)}
    for r, c in get_neighbors(row, col):
        if heightmap[row][col] < heightmap[r][c] < 9:
            basin_points |= get_basin_points(r, c)
    return basin_points


basin_sizes = sorted([len(get_basin_points(row, col)) for row, col in low_points], reverse=True)
print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])
