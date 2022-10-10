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
        print(f'new x: {self.x}, new y: {self.y}, width: {self.width()}, length: {self.length()}')
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

    def shortest_path(self, start=(0, 0), end=None):
        unvisited = set()
        distances = {}
        for node in self:
            print(node)
            unvisited.add(node)
            distances[node] = sys.maxsize
        distances[(start[0], start[1], self.get_val(start[0], start[1]))] = 0
        while len(unvisited) > 0:
            current_node = sorted(unvisited, key=lambda x: distances[x])[0]
            #print(f'current_node: {current_node}')
            for nx, ny in self.neighbors(current_node[0], current_node[1]):
                neighbor_val = self.get_val(nx, ny)
                #print(f'visiting {(nx, ny)} with a value of {neighbor_val}, total distance of {distances[current_node] + neighbor_val}')
                if distances[current_node] + neighbor_val < distances[(nx, ny, neighbor_val)]:
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


distances = grid.shortest_path()
end_coords = (grid.width() - 1, grid.length() - 1)
end_val = grid.get_val(end_coords[0], end_coords[1])
end = (end_coords[0], end_coords[1], end_val)
print(end, distances[end])
#print(distances[end])
#for node in grid:
#    print(node, distances[node])
#print(grid.shortest_path(end=(4, 2)))

