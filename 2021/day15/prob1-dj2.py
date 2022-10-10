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
            #print(node)
            unvisited.add(node)
            distances[node] = sys.maxsize
        current_min_node = (start[0], start[1], self.get_val(start[0], start[1]))
        distances[current_min_node] = 0
        total = len(unvisited)
        #sorted_nodes = sorted(unvisited, key=lambda x: x[2])
        #print(sorted_nodes)
        open_nodes = {}
        while len(unvisited) > 0:
            #print(len(unvisited))
            #print(f'current_node: {current_node}')
            #for node in unvisited:
            #    if current_min_node == None:
            #        current_min_node = node
            #    elif distances[node] < distances[current_min_node]:
            #        current_min_node = node
            ##print(f'selected: {current_min_node}')
            for nx, ny in self.neighbors(current_min_node[0], current_min_node[1]):
                ##print(f'checking neighbor: {nx, ny}')
                neighbor_val = self.get_val(nx, ny)
                if (nx, ny, neighbor_val) not in unvisited:
                    continue
                #print(f'visiting {(nx, ny)} with a value of {neighbor_val}, total distance of {distances[current_node] + neighbor_val}')
                tentative = distances[current_min_node] + neighbor_val
                if tentative < distances[(nx, ny, neighbor_val)]:
                    distances[(nx, ny, neighbor_val)] = tentative
                    open_nodes[(nx, ny, neighbor_val)] = tentative
                    print(f'found new shortest path to {(nx, ny)}: {tentative}')
            ##print(f'marking {current_min_node} visisted')
            #print(f'next up: {next_min_node}')
            unvisited.remove(current_min_node)
            try:
                del(open_nodes[current_min_node])
            except KeyError:
                pass
            s = sorted(open_nodes.items(), key=lambda x: x[1])
            if len(s) == 0:
                return distances
            else:
                current_min_node = s[0][0]
                ##print(f'next up: {current_min_node}')

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

