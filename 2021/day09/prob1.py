
class Grid(object):


    def __init__(self):
        self.rows = []

    def add_row(self, row):
        self.rows.append(row)

    def __iter__(self):
        self.x = 0
        self.y = 0
        return self

    def __next__(self):
        val = self.get_val(self.x, self.y)
        rx = self.x
        ry = self.y
        self.x += 1
        if self.x == self.width():
            self.y += 1
            self.x = 0
            if self.y == self.length():
                raise StopIteration
        return (rx, ry, val)

    def length(self):
        return len(self.rows)

    def width(self):
        return len(self.rows[0])

    def get_val(self, x, y):
        return int(self.rows[y][x])

    def neighbors(self, x, y):
        #print(f'checking {x}, {y} neighbors')
        n_coords = [
            (x, y - 1),
            (x, y + 1),
            (x - 1, y),
            (x + 1, y)
        ]
        for nx, ny in n_coords:
            if nx < 0 or ny < 0:
                continue
            try:
                yield self.get_val(nx, ny)
            except IndexError:
                continue                

    def is_low_point(self, x, y):
        #print(f'checking low point {x}, {y}')
        val = self.get_val(x, y)
        for neighbor in self.neighbors(x, y):
            if val >= neighbor:
                return False
        return True


grid = Grid()
risk = 0

with open('in.txt') as fh:
    for line in fh:
        line = line.strip()
        grid.add_row(line)

for x, y, val in grid:
    if grid.is_low_point(x, y):
        risk += val + 1

print(risk)
