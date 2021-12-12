
class Grid(object):


    def __init__(self):
        self.rows = []
        self.flashed = set()
        self.flash_count = 0

    def add_row(self, row):
        self.rows.append(row)

    def length(self):
        return len(self.rows)

    def width(self):
        return len(self.rows[0])

    def get_val(self, x, y):
        #print(f'getting val {x}, {y}')
        return int(self.rows[y][x])

    def run_steps(self):
        start_count = self.flash_count
        flash = False
        for y, _ in enumerate(self.rows):
            for x, val in enumerate(self.rows[y]):
                self.rows[y][x] += 1
                if self.rows[y][x] > 9:
                    flash = True
            #print(flash)
        while flash:
            flash = False
            for y, _ in enumerate(self.rows):
                for x, val in enumerate(self.rows[y]):
                    if val > 9 and (x, y) not in self.flashed:
                        self.flash(x, y)
                        flash = True
                    #print(len(self.rows[1]))
        for  x, y in self.flashed:
            self.rows[y][x] = 0
        self.clear_flashes()
        return self.flash_count - start_count

    def flash(self, x, y):
        #print(f'flashing ({x}, {y})')
        for nx, ny in self.neighbors(x, y):
            self.rows[ny][nx] += 1
            #if self.rows[ny][ny] == 9:
                #self.flash(nx, ny)
        self.flashed.add((x, y))
        self.flash_count += 1

    def clear_flashes(self):
        self.flashed = set()

    def neighbors(self, x, y):
        #print(f'checking {x}, {y} neighbors')
        n_coords = [
            (x, y - 1),
            (x, y + 1),
            (x - 1, y),
            (x + 1, y),
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

    def __repr__(self):
        repr_str = ''
        for row in self.rows:
            repr_str += ''.join([ str(x) for x in row ])
            repr_str += '\n'
        return repr_str

grid = Grid()

with open('in.txt') as fh:
    for line in fh:
        line = line.strip()
        grid.add_row([ int(x) for x in line ])

step = 1

while True:
    step_flashes = grid.run_steps()
    if step_flashes == 100:
        print(step)
        break
    step += 1
