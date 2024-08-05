
def valid(sides):
    s = sorted([ int(side) for side in sides ])
    return s[0] + s[1] > s[2]

c = 0
with open("in.txt") as fh:
    for line in fh:
        line = line.strip()
        sides = line.split()
        if valid(sides):
            c += 1
print(c)
