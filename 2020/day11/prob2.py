import sys

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
        directions = [
            (-1, 0), # left
            (0, -1), # up
            (1, 0), # right
            (0, 1), # down
            (-1, -1), # up-left
            (1, -1), # up-right
            (1, 1), # down-right
            (-1, 1), # down-left
        ]
        for direction in directions:
            done = False
            nx, ny = x, y
            while not done:
                nx += direction[0]
                ny += direction[1]
                if nx < 0 or ny < 0:
                    break
                elif nx >= self.width() or ny >= self.length():
                    break
                try:
                    neighbor_val = self.get_val(nx, ny)
                except IndexError:
                    #print(f'error retrieving value for {(nx, ny)}')
                    sys.exit()
                if neighbor_val == '.':
                    continue
                elif neighbor_val in ['L', '#']:
                    done = True
                    yield (nx, ny)
                else:
                    raise ValueError(f'Unexpected value at {(x, y)}: {neighbor_val}')
                #print(f'finished checking direction {direction}')

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
                    if c >=5:
                        new_empty.append((x, y))
            for x, y in new_occupied:
                self.set_val(x, y, '#')
            for x, y in new_empty:
                self.set_val(x, y, 'L')
        #print(f'round {_} complete:\n{self}')
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
