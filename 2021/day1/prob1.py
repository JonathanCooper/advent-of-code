
previous = None
count = 0

with open('in.txt') as fh:
    for line in fh:
        depth = int(line.strip())
        if previous:
            if depth > previous:
                count += 1
        previous = depth

print(count)
