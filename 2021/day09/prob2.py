
class Grid(object):


    def __init__(self):
        self.rows = []
        self.seen = set()

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
        #print(f'getting val {x}, {y}')
        return int(self.rows[y][x])

    def neighbors(self, x, y, exclude_nine=False):
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
            if nx >= self.width() or ny >= self.length():
                continue
            if exclude_nine and self.get_val(nx, ny) == 9:
                continue
            else: 
                yield (nx, ny)

    def is_low_point(self, x, y):
        #print(f'checking low point {x}, {y}')
        val = self.get_val(x, y)
        for nx, ny in self.neighbors(x, y):
            if val >= self.get_val(nx, ny):
                return False
        return True

    #def get_basin_size(self, x, y):
        #for coord in 

    def get_basin_coords(self, x, y):
        #print(f'called get_basin_coords({x}, {y})')
        basin_neighbors = set()
        for nx, ny in self.neighbors(x, y, exclude_nine=True):
            if (nx, ny) in self.seen:
                continue
            self.seen.add((nx, ny))
            basin_neighbors.add((nx, ny))
            new_neighbors = self.get_basin_coords(nx, ny)
            basin_neighbors.update(new_neighbors)
        basin_neighbors.add((x, y))
        return basin_neighbors

    def clear(self):
        self.seen = set()

grid = Grid()

with open('in.txt') as fh:
    for line in fh:
        line = line.strip()
        grid.add_row(line)

basin_sizes = []

for x, y, val in grid:
    if grid.is_low_point(x, y):
        basin = grid.get_basin_coords(x, y)
        basin_sizes.append(len(basin))
        grid.clear()

basin_sizes.sort()
print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])
