
def process(line):
    line = line.strip()
    first = None
    for c in line:
        if c.isdigit():
            if not first:
                first = c
            last = c
    return int(first + last)

total = 0

with open("in.txt") as fh:
    for line in fh:
        total += process(line)

print(total)
