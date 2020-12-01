parent_body_per_satellite = {}
with open('input/day06.txt') as input_file:
    for line in input_file.read().splitlines():
        parent_body, satellite = line.split(')')
        parent_body_per_satellite[satellite] = parent_body


def get_parent_bodies(satellite):
    parent_body = parent_body_per_satellite.get(satellite, '')
    if parent_body:
        return [parent_body] + get_parent_bodies(parent_body)
    else:
        return []


def count_orbital_transfers_between(mass1, mass2):
    mass1_parents = get_parent_bodies(mass1)
    mass2_parents = get_parent_bodies(mass2)
    for index1, mass1_parent in enumerate(mass1_parents):
        for index2, mass2_parent in enumerate(mass2_parents):
            if mass2_parent == mass1_parent:
                n_transfers = index1 + index2
                return n_transfers


print(count_orbital_transfers_between('YOU', 'SAN'))
