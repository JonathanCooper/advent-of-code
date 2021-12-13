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
        return int(self.rows[y][x])

    def neighbors(self, x, y, diag=False):
        n_coords = [
            (x, y - 1),
            (x, y + 1),
            (x - 1, y),
            (x + 1, y),
        ]
        if diag:
            n_coords += [
                (x - 1, y - 1),
                (x + 1, y - 1),
                (x - 1, y + 1),
                (x + 1, y + 1)
            ]
        for nx, ny in n_coords:
            if nx < 0 or ny < 0:
                continue
            if nx >= self.width() or ny >= self.length():
                continue
            else:
                yield (nx, ny)

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

    def __repr__(self):
        return '\n'.join(
            [ ''.join([ str(c) for c in row ]) for row in self.rows ]
        )
