import sys

GRID_SIZE = 990

grid = []

for row_idx in range(GRID_SIZE):
    row = []
    for column_idx in range(GRID_SIZE):
        row.append(0)
    grid.append(row)

with open('in.txt') as fh:
    for line in fh:
        line = line.strip()
        left, right = line.split('->')
        x1, y1 = left.split(',')
        x2, y2 = right.split(',')
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        #print(x1, y1, x2, y2)
        if x1 == x2:
            #1,1 -> 1,3
            for y in range(min([y1, y2]), max([y1, y2]) + 1):
                grid[y][x1] += 1
        elif y1 == y2:
            for x in range(min([x1, x2]), max([x1, x2]) + 1):
                grid[y1][x] += 1
        else:
            continue

points = 0

for y in range(GRID_SIZE):
    for x in range(GRID_SIZE):
        if grid[y][x] >= 2:
            points += 1

print(points)
