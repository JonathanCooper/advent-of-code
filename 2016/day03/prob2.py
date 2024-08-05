
def valid(sides):
    s = sorted([ int(side) for side in sides ])
    return s[0] + s[1] > s[2]

columns = {
    0: [],
    1: [],
    2: [],
}

with open("in.txt") as fh:
    for line in fh:
        line = line.strip()
        sides = line.split()
        for i, side in enumerate(sides):
            columns[i].append(side)

c = 0
for column in columns.values():
    for i in range(0, len(column), 3):
        if valid(column[i:i+3]):
            c += 1

print(c)
