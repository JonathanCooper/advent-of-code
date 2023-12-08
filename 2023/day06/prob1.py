import math

with open("in.txt") as fh:
    for line in fh:
        line = line.strip()
        #values = [ int(value) for value in line.split(":")[1].split() ]
        values = [int(''.join(line.split(":")[1].split()))]
        if line.startswith("Time"):
            times = values
        elif line.startswith("Distance"):
            distances = values
        else:
            raise ValueError(f"Unexpected line: {line}")

ways_to_win = []
for i, time in enumerate(times):
    ways = 0
    for push_duration in range(1, time):
        if push_duration * (time - push_duration) > distances[i]:
            ways += 1
            #print(f"{push_duration} is a way to win race {i+1}")
    ways_to_win.append(ways)

print(math.prod(ways_to_win))

