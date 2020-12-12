def parse_navigation_instructions(file_path):
    with open(file_path) as file:
        navigation_instructions = []
        for line in file.read().splitlines():
            action = line[0]
            value = int(line[1:])
            navigation_instructions.append((action, value))
        return navigation_instructions


class MapLocation:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_to(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, x=0, y=0):
        self.move_to(self.x + x, self.y + y)

    def manhattan_distance(self, x=0, y=0):
        return abs(self.x - x) + abs(self.y - y)


class Ferry(MapLocation):
    def __init__(self, x=0, y=0, waypoint_x=0, waypoint_y=0):
        super().__init__(x, y)
        self.waypoint = MapLocation(waypoint_x, waypoint_y)

    def move_waypoint(self, x=0, y=0):
        self.waypoint.move(x, y)

    def move_forward(self, n):
        x = n * self.waypoint.x
        y = n * self.waypoint.y
        self.move(x, y)

    def rotate(self, degrees):
        n_quarter_turns = (degrees // 90) % 4
        if n_quarter_turns == 1:
            self.waypoint.move_to(self.waypoint.y, -self.waypoint.x)
        elif n_quarter_turns == 2:
            self.waypoint.move_to(-self.waypoint.x, -self.waypoint.y)
        elif n_quarter_turns == 3:
            self.waypoint.move_to(-self.waypoint.y, self.waypoint.x)


def day12a():
    navigation_instructions = parse_navigation_instructions('input/day12.txt')
    ferry = Ferry(waypoint_x=1)
    for action, value in navigation_instructions:
        if action == 'N':
            ferry.move(0, value)
        elif action == 'S':
            ferry.move(0, -value)
        elif action == 'E':
            ferry.move(value, 0)
        elif action == 'W':
            ferry.move(-value, 0)
        elif action == 'L':
            ferry.rotate(-value)
        elif action == 'R':
            ferry.rotate(value)
        elif action == 'F':
            ferry.move_forward(value)
    return ferry.manhattan_distance()


def day12b():
    navigation_instructions = parse_navigation_instructions('input/day12.txt')
    ferry = Ferry(waypoint_x=10, waypoint_y=1)
    for action, value in navigation_instructions:
        if action == 'N':
            ferry.move_waypoint(0, value)
        elif action == 'S':
            ferry.move_waypoint(0, -value)
        elif action == 'E':
            ferry.move_waypoint(value, 0)
        elif action == 'W':
            ferry.move_waypoint(-value, 0)
        elif action == 'L':
            ferry.rotate(-value)
        elif action == 'R':
            ferry.rotate(value)
        elif action == 'F':
            ferry.move_forward(value)
    return ferry.manhattan_distance()


print(day12a())
print(day12b())
