parent_body_per_satellite = {}
with open('day06.txt') as input_file:
    for line in input_file.read().splitlines():
        parent_body, satellite = line.split(')')
        parent_body_per_satellite[satellite] = parent_body


def count_orbits(satellite):
    parent_body = parent_body_per_satellite.get(satellite, '')
    if parent_body:
        return 1 + count_orbits(parent_body)
    else:
        return 0


n_orbits = 0
for satellite in parent_body_per_satellite.keys():
    n_orbits += count_orbits(satellite)
print(n_orbits)
