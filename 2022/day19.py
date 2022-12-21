import math
import re

with open('input/day19.txt') as input_file:
    blueprints = input_file.read().splitlines()


def get_geode_max(blueprint, n_minutes, filter_cutoff=150):
    costs_per_robot = {}
    for robot_resource, costs_string in re.findall(r'Each (\w+) robot costs ([^.]+).', blueprint):
        amount_per_resource = {}
        for cost_string in costs_string.split(' and '):
            amount, resource = cost_string.split(' ')
            amount_per_resource[resource] = int(amount)
        costs_per_robot[robot_resource] = amount_per_resource
    resources = ['geode', 'obsidian', 'clay', 'ore']
    initial_robot_state = {resource: 0 for resource in resources}
    initial_robot_state['ore'] = 1
    initial_resource_state = {resource: 0 for resource in resources}
    states = [(initial_robot_state, initial_resource_state)]
    for _ in range(n_minutes):
        next_states = []
        for robot_state, resource_state in states:
            collected_resource_state = resource_state.copy()
            for robot_resource, amount in robot_state.items():
                collected_resource_state[robot_resource] += amount
            next_states.append((robot_state, collected_resource_state))
            for robot_resource in resources:
                if all(resource_state[resource] >= amount for resource, amount in
                       costs_per_robot[robot_resource].items()):
                    next_robot_state = robot_state.copy()
                    next_resource_state = collected_resource_state.copy()
                    for resource, amount in costs_per_robot[robot_resource].items():
                        next_resource_state[resource] -= amount
                    next_robot_state[robot_resource] += 1
                    next_states.append((next_robot_state, next_resource_state))
        states = next_states
        flat_states = [[x for r in resources for x in (s[1][r], s[0][r])] for s in states]
        unfiltered_indices = list(sorted(range(len(states)), key=lambda x: flat_states[x]))
        filtered_indices = []
        while unfiltered_indices and len(filtered_indices) <= filter_cutoff:
            filter_index = unfiltered_indices.pop()
            filtered_indices.append(filter_index)
            filter_flat_state = flat_states[filter_index]
            remaining_unfiltered_indices = []
            for index in unfiltered_indices:
                flat_state = flat_states[index]
                if any(flat_state[i] > filter_flat_state[i] for i in range(8)):
                    remaining_unfiltered_indices.append(index)
            unfiltered_indices = remaining_unfiltered_indices
        states = [states[index] for index in filtered_indices]
    return states[0][1]['geode']


print(sum((blueprint_i + 1) * get_geode_max(blueprint, 24) for blueprint_i, blueprint in enumerate(blueprints)))
print(math.prod(get_geode_max(blueprint, 32) for blueprint in blueprints[:3]))
