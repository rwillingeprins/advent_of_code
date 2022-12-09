moves = []
x_y_per_direction = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
with open('input/day09.txt') as input_file:
    for line in input_file:
        direction, n_steps = line.strip().split()
        for _ in range(int(n_steps)):
            moves.append(x_y_per_direction[direction])


class Knot:
    def __init__(self, x: int = 0, y: int = 0, tail: 'Knot' = None):
        self.x = x
        self.y = y
        self.tail = tail

    def move(self, x: int, y: int):
        self.x += x
        self.y += y
        if self.tail:
            x_diff = self.x - self.tail.x
            y_diff = self.y - self.tail.y
            if abs(x_diff) > 1 or abs(y_diff) > 1:
                x_pull, y_pull = [(diff > 0) - (diff < 0) for diff in (x_diff, y_diff)]
                self.tail.move(x_pull, y_pull)


def move_rope(n_knots: int = 2):
    tail = Knot()
    head = Knot(tail=tail)
    for _ in range(n_knots - 2):
        head = Knot(tail=head)
    tail_locations = {(tail.x, tail.y)}
    for x_move, y_move in moves:
        head.move(x_move, y_move)
        tail_locations.add((tail.x, tail.y))
    return len(tail_locations)


print(move_rope())
print(move_rope(10))
