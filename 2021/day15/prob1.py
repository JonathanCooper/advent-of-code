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
        if not end:
            end = (self.width() - 1, self.length() - 1)
        seen = set([start])
        #print(seen)
        not_seen = set()
        paths = {start: []}
        dvals = PriorityQueue()
        for y in range(self.length()):
            for x in range(self.width()):
                not_seen.add((x, y))
        distances = {start: 0}
        while seen != not_seen:
            print(len(seen), len(not_seen))
            dvals = {}
            for x, y in seen: 
                for nx, ny in self.neighbors(x, y):
                    if (nx, ny) in seen:
                        continue
                    #if (x, y, nx, ny) in dvals.keys():
                        #continue
                    distance = distances[(x, y)] + self.get_val(nx, ny)
                    dvals.insert(
                        Node(
                            label=f'{nx}:{ny}',
                            priority=distance,


                #if not dvals:
                #    continue
            #coords, distance = sorted(dvals.items(), key=lambda x: x[1])[0]
            coords, distance = ((1, 2, 3, 4), 25)
            source_coords = (coords[0], coords[1])
            dest_coords = (coords[2], coords[3])
            distances[dest_coords] = distance
            seen.add(dest_coords)
            #paths[smallest[0]] = paths[(x, y)] + [smallest[0]]
        #print(paths[end])
        return distances[end]


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


print(grid.shortest_path())
#print(grid.shortest_path(end=(4, 2)))
