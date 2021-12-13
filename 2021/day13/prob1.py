
class Grid(object):


    def __init__(self, max_x, max_y):
        self.rows = []
        for _ in range(max_y + 1):
            row = []
            for __ in range(max_x + 1):
                row.append('.')
            self.rows.append(row)
    def add_row(self, row):
        self.rows.append(row)

    def length(self):
        return len(self.rows)

    def width(self):
        return len(self.rows[0])

    def get_val(self, x, y):
        #print(f'getting val {x}, {y}')
        return int(self.rows[y][x])

    def mark(self, x, y):
        self.rows[y][x] = '#'

    def fold(self, axis, fold_val):
        for y, row in enumerate(self.rows):
            for x, val in enumerate(row):
                if axis == 'y' and y < fold_val:
                    continue
                if axis == 'x' and x < fold_val:
                    continue
                if val == '#':
                    if axis == 'y':
                        reflect_dist = y - fold_val
                        new_y = fold_val - reflect_dist
                        self.mark(x, new_y)
                    elif axis == 'x':
                        reflect_dist = x - fold_val
                        new_x = fold_val - reflect_dist
                        self.mark(new_x, y)
        if axis == 'y':
            for _ in range(fold_val, len(self.rows)):
                #print(f'deleting row {i}')
                del(self.rows[-1])
        elif axis == 'x':
            for row_id, row in enumerate(self.rows):
                for __ in range(fold_val, len(row)):
                    del(self.rows[row_id][-1])

    def count(self):
        return sum([ row.count('#') for row in self.rows ])

    def __repr__(self):
        repr_str = ''
        for row in self.rows:
            repr_str += ''.join([ str(x) for x in row ])
            repr_str += '\n'
        return repr_str

max_x = 0
max_y = 0
points = []
folds = []

with open('in.txt') as fh:
    for line in fh:
        line = line.strip()
        if line == '':
            continue
        if line.startswith('fold'):
            word = line.split()[-1]
            axis, val = word.split('=')
            folds.append((axis, int(val)))
            continue
        x, y = line.split(',')
        x, y = int(x), int(y)
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        points.append((x, y))

grid = Grid(max_x, max_y)

for x, y in points:
    grid.mark(x, y)


for axis, val in folds:
    grid.fold(axis, val)
    break

#print(grid)
print(grid.count())
