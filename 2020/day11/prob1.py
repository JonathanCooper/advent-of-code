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

    def neighbors(self, x, y, diag=False):
        n_coords = [
            (x, y + 1),
            (x + 1, y),
            (x - 1, y),
            (x, y - 1),
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
        #print(f'new x: {self.x}, new y: {self.y}, width: {self.width()}, length: {self.length()}')
        if self.y == self.length():
            raise StopIteration
        val = self.get_val(self.x, self.y)
        rx = self.x
        ry = self.y
        self.x += 1
        if self.x == self.width():
            self.y += 1
            self.x = 0
            #print(f'new x: {self.x}, new y: {self.y}, width: {self.width()}, length: {self.length()}')
        return (rx, ry, val)

    def set_val(self, x, y, val):
        self.rows[y][x] = val

    def run_rounds(self, n=1):
        for _ in range(n):
            new_occupied = []
            new_empty = []
            for x, y, val in self:
                #print(f'checking {(x, y)}')
                if val == 'L':
                    no_neighbors = True
                    for nx, ny in self.neighbors(x, y, diag=True):
                        if self.get_val(nx, ny) == '#':
                            no_neighbors = False
                    if no_neighbors:
                        new_occupied.append((x, y))
                elif val == '#':
                    #print(f'seat is occupied')
                    c = 0
                    for nx, ny in self.neighbors(x, y, diag=True):
                        if self.get_val(nx, ny) == '#':
                            #print(f'neighbor {(nx, ny)} is occupied')
                            c += 1
                    #print(f'found {c} occupied neighbors')
                    if c >=4:
                        new_empty.append((x, y))
            for x, y in new_occupied:
                self.set_val(x, y, '#')
            for x, y in new_empty:
                self.set_val(x, y, 'L')
        return len(new_occupied) + len(new_empty)
                        
    def __repr__(self):
        repr_str = ''
        for row in self.rows:
            repr_str += ''.join(row)
            repr_str += '\n'
        return repr_str

grid = Grid()

with open('in.txt') as fh:
    for line in fh:
        line = line.strip()
        grid.add_row(list(line))

done = False

while not done:
    changed = grid.run_rounds()
    if changed == 0:
        done = True

c = 0
for _, __, val in grid:
    if val == '#':
        c += 1

print(c)
