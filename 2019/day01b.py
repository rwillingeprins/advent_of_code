sum_of_fuel_requirements = 0
with open('day01.txt') as input_file:
    for line in input_file:
        mass = int(line)
        required_fuel = (mass // 3) - 2
        while required_fuel > 0:
            sum_of_fuel_requirements += required_fuel
            fuel_mass = required_fuel
            required_fuel = (fuel_mass // 3) - 2
print(sum_of_fuel_requirements)
