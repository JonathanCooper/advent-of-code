from grid import Grid


grid = Grid()

with open("in.txt") as fh:
    for line in fh:
        line = line.strip()
        grid.add_row(line)

current_word = ""
found_gears= set()
total = 0
gears = {}

for x, y, c in grid:
    if c.isdigit():
        current_word += c
        for nx, ny in grid.neighbors(x, y, diag=True):
            neighbor_val = grid.get_val(nx, ny)
            if neighbor_val == "*":
                found_gears.add((nx, ny))
    else:
        for gear in found_gears:
            try:
                gears[gear].append(int(current_word))
            except KeyError:
                gears[gear] = [int(current_word)]
        current_word = ""
        found_gears = set()

total = 0

for l in gears.values():
    if len(l) != 2:
        continue
    total += l[0] * l[1]

print(total)
