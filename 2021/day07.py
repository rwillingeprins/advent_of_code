with open('input/day07.txt') as file:
    horizontal_positions = list(map(int, file.readline().split(',')))
fuel = min(sum(abs(crab_x - x) for crab_x in horizontal_positions) for x in range(max(horizontal_positions)))
print(fuel)

min_fuel = None
for x in range(max(horizontal_positions)):
    fuel = 0
    for crab_x in horizontal_positions:
        distance = abs(crab_x - x)
        fuel += (distance ** 2 + distance) // 2
    if min_fuel is None or fuel < min_fuel:
        min_fuel = fuel
print(min_fuel)
