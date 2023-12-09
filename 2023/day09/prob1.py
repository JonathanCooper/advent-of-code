

def extrapolate(l):
    if all([ diff == 0 for diff in l ]):
        return 0
    differences = []
    for i, val in enumerate(l[1:]):
        differences.append(val - l[i])
    return l[0] - extrapolate(differences)

total = 0
with open("in.txt") as fh:
    for line in fh:
        line = line.strip()
        history = [ int(i) for i in line.split() ]
        total += extrapolate(history)

print(total)
