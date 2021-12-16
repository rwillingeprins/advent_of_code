def find_safest_path(risk_grid):
    last_row = len(risk_grid) - 1
    last_col = len(risk_grid[0]) - 1
    cumulative_risk_grid = [[None for _ in row] for row in risk_grid]
    cumulative_risk_grid[0][0] = 0
    queue = [(0, 0)]
    while queue:
        row, col = queue.pop(0)
        risk = cumulative_risk_grid[row][col]
        for row_step, col_step in (1, 0), (0, 1), (-1, 0), (0, -1):
            next_row = row + row_step
            next_col = col + col_step
            if 0 <= next_row <= last_row and 0 <= next_col <= last_col:
                next_risk = risk + risk_grid[next_row][next_col]
                min_risk = cumulative_risk_grid[next_row][next_col]
                if min_risk is None or next_risk < min_risk:
                    cumulative_risk_grid[next_row][next_col] = next_risk
                    queue.append((next_row, next_col))
    return cumulative_risk_grid[last_row][last_col]


def increase_risk_level(risk_level, increment):
    for _ in range(increment):
        risk_level = risk_level + 1 if risk_level < 9 else 1
    return risk_level


with open('input/day15.txt') as file:
    risk_grid = [[int(risk_string) for risk_string in row_string] for row_string in file.read().splitlines()]
print(find_safest_path(risk_grid))

risk_grid = [[increase_risk_level(risk_level, add) for add in range(5) for risk_level in row] for row in risk_grid]
risk_grid = [[increase_risk_level(risk_level, add) for risk_level in row] for add in range(5) for row in risk_grid]
print(find_safest_path(risk_grid))
