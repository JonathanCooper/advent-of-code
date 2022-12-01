import sys

with open('in.txt') as fh:
    target, schedule = fh.readlines()


target = int(target.strip())
buses = [ int(bus) for bus in schedule.strip().split(',') if bus != 'x' ]

best_bus = sys.maxsize
for bus in buses:
    arrival = bus
    while arrival < target:
        arrival += bus
    if arrival < best_bus:
        best_bus = arrival
        best_id = bus

wait = best_bus - target
print(wait * best_id)
