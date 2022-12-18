import re

valve_pattern = re.compile(r'Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? ((?:[A-Z]{2}(?:, )?)+)')
valve_dict = {}
all_valves = set()
with open('input/day16.txt') as input_file:
    for line in input_file:
        valve, flow_rate_string, tunnels_string = re.fullmatch(valve_pattern, line.strip()).groups()
        flow_rate = int(flow_rate_string)
        valve_dict[valve] = (flow_rate, tuple(tunnels_string.split(', ')))
        if flow_rate:
            all_valves.add(valve)

states = [('AA', 0, set())]
best_per_valve = {valve: -1 for valve in valve_dict.keys()}
for remaining_minutes in range(29, 0, -1):
    next_states = []
    for current_valve, released_pressure, opened_valves in states:
        if released_pressure > best_per_valve[current_valve]:
            best_per_valve[current_valve] = released_pressure
            flow_rate, tunnels = valve_dict[current_valve]
            if flow_rate and current_valve not in opened_valves:
                next_released_pressure = released_pressure + flow_rate * remaining_minutes
                next_opened_valves = opened_valves | {current_valve}
                next_states.append((current_valve, next_released_pressure, next_opened_valves))
            for next_valve in tunnels:
                next_states.append((next_valve, released_pressure, opened_valves))
    states = next_states
print(max(*best_per_valve.values()))

states = [(('AA', 'AA'), 0, set())]
max_pressure = 0
for remaining_minutes in range(25, -1, -1):
    next_states = []
    for current_valves, released_pressure, opened_valves in sorted(states, key=lambda x: x[1], reverse=True)[:10000]:
        max_pressure = max(released_pressure, max_pressure)
        current_valve1, current_valve2 = current_valves
        flow_rate1, tunnels1 = valve_dict[current_valve1]
        flow_rate2, tunnels2 = valve_dict[current_valve2]
        if flow_rate1 and current_valve1 not in opened_valves:
            if current_valve2 != current_valve1 and flow_rate2 and current_valve2 not in opened_valves:
                next_released_pressure = released_pressure + ((flow_rate1 + flow_rate2) * remaining_minutes)
                next_opened_valves = opened_valves | {current_valve1, current_valve2}
                next_states.append((current_valves, next_released_pressure, next_opened_valves))
            for next_valve2 in tunnels2:
                next_valves = (current_valve1, next_valve2)
                next_released_pressure = released_pressure + flow_rate1 * remaining_minutes
                next_opened_valves = opened_valves | {current_valve1}
                next_states.append((next_valves, next_released_pressure, next_opened_valves))
        for next_valve1 in tunnels1:
            if flow_rate2 and current_valve2 not in opened_valves:
                next_valves = (next_valve1, current_valve2)
                next_released_pressure = released_pressure + flow_rate2 * remaining_minutes
                next_opened_valves = opened_valves | {current_valve2}
                next_states.append((next_valves, next_released_pressure, next_opened_valves))
            for next_valve2 in tunnels2:
                next_valves = (next_valve1, next_valve2)
                next_states.append((next_valves, released_pressure, opened_valves))
    states = next_states
print(max_pressure)
