sum_of_fuel_requirements = 0
with open('day01.txt') as input_file:
    for line in input_file:
        mass = int(line)
        required_fuel = (mass // 3) - 2
        sum_of_fuel_requirements += required_fuel
print(sum_of_fuel_requirements)
