
class Grid(object):


    def __init__(self):
        self.rows = []

    def add_row(self, row):
        self.rows.append(row)

    def length(self):
        return len(self.rows)

    def width(self):
        return len(self.rows[0])

    def get_val(self, x, y):
        return self.rows[y][x]

    def check_dir(self, x, y, direction):
        directions = {
            'U': (0, -1),
            'L': (-1, 0),
            'D': (0, 1),
            'R': (1, 0)
        }
        move = directions[direction]
        my_height = self.get_val(x, y)
        x += move[0]
        y += move[1]
        while 0 <= x < self.length() and 0 <= y < self.width():
            #print(f'{direction}: checking {self.get_val(x, y)} against {my_height}')
            #print(x, y)
            if self.get_val(x, y) >= my_height:
                return False
            x += move[0]
            y += move[1]
        return True

    def check(self, x, y):
        for direction in ['U', 'L', 'D', 'R']:
            #print(x, y, direction, self.check_dir(x, y, direction))
            if self.check_dir(x, y, direction):
                return True
        return False

    def __iter__(self):
        self.x = 0
        self.y = 0
        return self

    def __next__(self):
        if self.y == self.length():
            raise StopIteration
        val = self.get_val(self.x, self.y)
        rx = self.x
        ry = self.y
        self.x += 1
        if self.x == self.width():
            self.y += 1
            self.x = 0
        return (rx, ry, val)

    def __repr__(self):
        return '\n'.join(
            [ ''.join([ str(c) for c in row ]) for row in self.rows ]
        )

grid = Grid()

with open('in.txt') as fh:
    for line in fh:
        line = line.strip()
        row = [ int(x) for x in line ]
        grid.add_row(row)

trees = 0

for x, y, _ in grid:
    #print(x, y, _, grid.check(x, y))
    if grid.check(x, y):
        trees += 1

print(trees)
