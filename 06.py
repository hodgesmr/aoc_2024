from utils import timed, get_input_lines

from enum import Enum


class Guard:
    class Direction(Enum):
        NORTH = "^"
        EAST = ">"
        SOUTH = "v"
        WEST = "<"

    def __init__(self, map, x=None, y=None, direction=None):
        self.map = map
        self.direction = None
        self.logbook = set()
        if not x or not y or not direction:
            for yi, y in enumerate(map):
                for xi, x in enumerate(y):
                    if x in set([member.value for member in Guard.Direction]):
                        self.direction = Guard.Direction(x)
                        self.x = xi
                        self.y = yi
                        break  # I'm not bothering to refactor this
        else:
            self.x = x
            self.y = y
            self.direction = direction
        self.start = (self.x, self.y, self.direction)
        self.map[self.y][self.x] = "X"
        self.log()

    # log an x, y, direction to the logbook
    # return True if it's a new log item
    # return False if the log item already exists
    def log(self):
        log_item = (self.x, self.y, self.direction)
        if log_item in self.logbook:
            return False
        self.logbook.add(log_item)
        return True

    # Return whether our next move would take us off the map
    def headed_offmap(self):
        if self.direction == Guard.Direction.NORTH:
            return self.y == 0
        elif self.direction == Guard.Direction.EAST:
            return self.x == len(self.map[self.y]) - 1
        elif self.direction == Guard.Direction.SOUTH:
            return self.y == len(self.map) - 1
        else:
            return self.x == 0

    # Return whether we're obstructed
    def is_obstructed(self):
        if not self.headed_offmap():
            if self.direction == Guard.Direction.NORTH:
                return self.map[self.y - 1][self.x] == "#"
            elif self.direction == Guard.Direction.EAST:
                return self.map[self.y][self.x + 1] == "#"
            elif self.direction == Guard.Direction.SOUTH:
                return self.map[self.y + 1][self.x] == "#"
            else:
                return self.map[self.y][self.x - 1] == "#"
        return False

    # 90 degree turn
    def rotate(self):
        if self.direction == Guard.Direction.NORTH:
            self.direction = Guard.Direction.EAST
        elif self.direction == Guard.Direction.EAST:
            self.direction = Guard.Direction.SOUTH
        elif self.direction == Guard.Direction.SOUTH:
            self.direction = Guard.Direction.WEST
        else:
            self.direction = Guard.Direction.NORTH

    # Step forward
    def move(self):
        if self.direction == Guard.Direction.NORTH:
            self.y = self.y - 1
        elif self.direction == Guard.Direction.EAST:
            self.x = self.x + 1
        elif self.direction == Guard.Direction.SOUTH:
            self.y = self.y + 1
        else:
            self.x = self.x - 1

        self.map[self.y][self.x] = "X"

    # Traverse the route
    def walk(self):
        

        while not self.headed_offmap():
            if self.is_obstructed():
                self.rotate()
            elif not self.headed_offmap():
                self.move()
            
            # If we fail to log, it's already been logged
            # that's a loop
            if not self.log():
                return False
        return True


def part_1(input_lines):
    map = [list(row) for row in input_lines]
    guard = Guard(map)
    guard.walk()
    return sum(row.count("X") for row in guard.map)


def part_2(input_lines):
    loop_positions = set()
    tried = set()
    unobstructed_guard = Guard([list(row) for row in input_lines])
    # First, do an unobstructed walk to map the path
    unobstructed_guard.walk()

    # Now, we need to place a barrier in each possible collision path
    # This is less than all the possible squares.
    # Take all the squares the unobstructed guard walked.
    for step in unobstructed_guard.logbook:
        new_map = [list(row) for row in input_lines]
        x = step[0]
        y = step[1]

        if (
            (x, y) != unobstructed_guard.start
            and (x, y) not in tried
            and new_map[y][x] != "#"
        ):

            new_map[y][x] = "#"

            new_guard = Guard(
                new_map,
                x=unobstructed_guard.start[0],
                y=unobstructed_guard.start[1],
                direction=unobstructed_guard.start[2],
            )
            unlooped = new_guard.walk()
            tried.add((x, y))
            if not unlooped:
                loop_positions.add((x, y))

    return len(loop_positions)


timed(part_1, [get_input_lines()])
timed(part_2, [get_input_lines()])
