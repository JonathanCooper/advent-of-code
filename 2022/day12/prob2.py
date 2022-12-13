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
        orig_val = self.get_val(x, y)
        for nx, ny in n_coords:
            if nx < 0 or ny < 0:
                continue
            if nx >= self.width() or ny >= self.length():
                continue
            if ord(self.get_val(nx, ny)) - ord(orig_val) > 1:
                continue
            else:
                yield (nx, ny)

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

    def shortest_path(self, start=(0, 0), end=None):
        distances = {start: 0}
        seen = set()
        queue = [start]
        while queue:
            cur_node = queue.pop(0)
            for neighbor in self.neighbors(cur_node[0], cur_node[1]):
                if neighbor in seen:
                    continue
                seen.add(neighbor)
                queue.append(neighbor)
                distances[neighbor] = distances[cur_node] + 1
                if neighbor == end:
                    return distances

    def __repr__(self):
        return '\n'.join(
            [ ''.join([ str(c) for c in row ]) for row in self.rows ]
        )

grid = Grid()

cur_row = 0
with open('test.txt') as fh:
    for line in fh:
        line = line.strip()
        if 'S' in line:
            start = (line.index('S'), cur_row)
            line = line.replace('S', 'a')
        if 'E' in line:
            end = (line.index('E'), cur_row)
            line = line.replace('E', 'z')
        #row = [ ord(c) for c in line ]
        grid.add_row(line)
        cur_row += 1

paths = []
for x, y, val in grid:
    if val == 'a':
        distances = grid.shortest_path((x, y), end)
        if distances:
            paths.append(distances[end])

print(min(paths))
