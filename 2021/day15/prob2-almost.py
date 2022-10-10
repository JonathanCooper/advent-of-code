import copy
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
            #(x, y - 1),
            (x, y + 1),
            #(x - 1, y),
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

    def shortest_path(self, start=(0, 0), end=None):
        unvisited = set()
        distances = {}
        for node in self:
            unvisited.add(node)
            distances[node] = sys.maxsize
        distances[(start[0], start[1], self.get_val(start[0], start[1]))] = 0
        while len(unvisited) > 0:
            current_node = sorted(unvisited, key=lambda x: distances[x])[0]
            #print(current_node)
            for nx, ny in self.neighbors(current_node[0], current_node[1]):
                neighbor_val = self.get_val(nx, ny)
                distances[(nx, ny, neighbor_val)] = distances[current_node] + neighbor_val
            unvisited.remove(current_node)
        return distances

    def __repr__(self):
        return '\n'.join(
            [ ''.join([ str(c) for c in row ]) for row in self.rows ]
        )


grid = Grid()

with open('test.txt') as fh:
    for line in fh:
        line = line.strip()
        row = [ int(x) for x in line ]
        grid.add_row(row)

new_grid = copy.deepcopy(grid)

for i in range(4):
    for j in range(len(grid.rows)):
        new_row = []
        for old in grid.rows[j]:
            new_val = old + i + 1
            if new_val > 9:
                new_val -= 9
            new_row.append(new_val)
        new_grid.rows.append(new_row)
        #grid.rows.append(new_row)

grid = new_grid

new_grid = copy.deepcopy(grid)

for j, row in enumerate(grid.rows):
    for i in range(4):
        new_row = []
        for old in row:
            new_val =  old + i + 1
            if new_val > 9:
                new_val -= 9
            new_row.append(new_val)
        new_grid.rows[j] += new_row

grid = new_grid
#print(grid)
distances = grid.shortest_path()
end_coords = (grid.width() - 1, grid.length() - 1)
end_val = grid.get_val(end_coords[0], end_coords[1])
end = (end_coords[0], end_coords[1], end_val)
print(distances[(3, 13, 5)])
#print(distances[end])
#for node in grid:
#    print(node, distances[node])
#print(grid.shortest_path(end=(4, 2)))
