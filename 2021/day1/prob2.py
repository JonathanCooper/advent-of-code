
previous = None
count = 0
depths = []

with open('in.txt') as fh:
    for line in fh:
        depth = int(line.strip())
        depths.append(depth)

for i in range(len(depths) - 2):
    window = sum(depths[i:i+3])
    if previous:
        if window > previous:
            count += 1
    previous = window

print(count)
