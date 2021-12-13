class OctoGrid:
    def __init__(self, grid_string):
        self.grid = [[int(energy_string) for energy_string in line] for line in grid_string.splitlines()]
        self.flash_count = 0
        self.step_count = 0

    def __str__(self):
        return '\n'.join(''.join(map(str, row)) for row in self.grid)

    def increase_energy_level(self, row, col):
        if self.grid[row][col] <= 9:
            self.grid[row][col] += 1
            if self.grid[row][col] > 9:
                self.flash_count += 1
                for r in range(row - 1, row + 2):
                    if 0 <= r < len(self.grid):
                        for c in range(col - 1, col + 2):
                            if 0 <= c < len(self.grid[r]):
                                self.increase_energy_level(r, c)

    def step(self):
        self.step_count += 1
        for row, row_values in enumerate(self.grid):
            for col, _ in enumerate(row_values):
                self.increase_energy_level(row, col)
        for row, row_values in enumerate(self.grid):
            for col, _ in enumerate(row_values):
                if self.grid[row][col] > 9:
                    self.grid[row][col] = 0

    def is_synchronized(self):
        return all(energy_level == 0 for row in self.grid for energy_level in row)


with open('input/day11.txt') as file:
    grid_string = file.read()

octo_grid = OctoGrid(grid_string)
for _ in range(100):
    octo_grid.step()
print(octo_grid.flash_count)

octo_grid = OctoGrid(grid_string)
while not octo_grid.is_synchronized():
    octo_grid.step()
print(octo_grid.step_count)
