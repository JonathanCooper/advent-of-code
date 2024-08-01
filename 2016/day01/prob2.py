from collections import namedtuple

class Coord(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

class Grid(object):

    dirs = ["N", "E", "S", "W"]

    def __init__(self):
        self.pos = Coord(x=0, y=0)
        self.dir_pointer = 0 # start "N"
        self.seen = set()

    def turn(self, direction):
        if direction == "R":
            self.dir_pointer += 1
        elif direction == "L":
            self.dir_pointer -= 1
        else:
            raise ValueError(f"Unexpected direction: {direction}")

    def get_dir(self):
        return self.dirs[self.dir_pointer % len(self.dirs)]

    def move(self, num):
        for _ in range(num):
            if self.get_dir() == "N":
                self.pos.y += 1
            elif self.get_dir() == "E":
                self.pos.x += 1
            elif self.get_dir() == "S":
                self.pos.y -= 1
            elif self.get_dir() == "W":
                self.pos.x -= 1
            else:
                raise ValueError(f"Unexpected direction: {self.get_dir()}")
            new_loc = (self.pos.x, self.pos.y)
            if new_loc in self.seen:
                print(self.manhattan())
                exit(0)
            else:
                self.seen.add(new_loc)

    def run_instruction(self, direction, num):
        self.turn(direction)
        self.move(num)

    def manhattan(self):
        return abs(self.pos.x) + abs(self.pos.y)


with open("in.txt") as fh:
    line = fh.readline()
    line = line.strip()
    split_line = line.split(",")

grid = Grid()

for instruction in split_line:
#for instruction in ['R8', 'R4', 'R4', 'R8']:
    instruction = instruction.strip()
    direction, num = instruction[0], int(instruction[1:])
    grid.run_instruction(direction, num)

raise ValueError("Completed without visiting any locations twice")
