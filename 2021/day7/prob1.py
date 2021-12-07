

with open('in.txt') as fh:
    line = fh.readline()
    positions = line.strip().split(',')
    positions = [ int(x) for x in positions ]

max_pos = max(positions)
max_fuel = max_pos * len(positions)
least_fuel = max_fuel

for i in range(max_pos + 1):
    fuel_used = 0
    for crab in positions:
        fuel_used += abs(crab - i)
    if fuel_used < least_fuel:
        least_fuel = fuel_used

print(least_fuel)
