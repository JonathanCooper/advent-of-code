import math

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
        score = 0
        while 0 <= x < self.length() and 0 <= y < self.width():
            #print(f'{direction}: checking {self.get_val(x, y)} against {my_height}')
            #print(f'current score: {score}')
            score += 1
            if self.get_val(x, y) >= my_height:
                return score
            x += move[0]
            y += move[1]
        return score

    def check(self, x, y):
        scores = []
        for direction in ['U', 'L', 'R', 'D']:
            scores.append(self.check_dir(x, y, direction))
        #print(scores)
        return math.prod(scores)

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

max_score = 0

for x, y, _ in grid:
    max_score = max(grid.check(x, y), max_score)

print(max_score)
