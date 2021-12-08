
def calculate_fuel(start, end):
    distance = abs(start - end) + 1
    return distance * (distance + 1) / 2

with open('in.txt') as fh:
    line = fh.readline()
    positions = line.strip().split(',')
    positions = [ int(x) for x in positions ]

max_pos = max(positions)
max_fuel = max_pos * calculate_fuel(0, max_pos)
least_fuel = max_fuel

for i in range(max_pos + 1):
    fuel_used = 0
    for crab in positions:
        fuel_used += calculate_fuel(crab, i)
    if fuel_used < least_fuel:
        least_fuel = fuel_used

print(least_fuel)
