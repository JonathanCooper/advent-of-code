import sys

with open('in.txt') as fh:
    _, schedule = fh.readlines()


schedule = schedule.strip().split(',')

buses = {}

for i, bus in enumerate(schedule):
    if bus != 'x':
        buses[i] = int(bus)

s = sorted(buses.items(), key=lambda x: x[1])
max_bus_offset = s[-1][0]
max_bus_id = s[-1][1]
del(buses[max_bus_offset])

target = max_bus_id
items = buses.items()

fixed = []
for item in items:
    new_offset = item[0] - max_bus_offset
    fixed.append((new_offset, item[1]))

items = fixed

while target < 100000000000000:
    found = True
    #print(f'checking {target}')
    for offset, bus_id in items:
        #print(f'checking offet id: {bus_id}')
        constraint = target + offset
        if constraint % bus_id != 0:
            found = False
            break
    if found:
        print(target - max_bus_offset)
        break
    else:
        target += max_bus_id
    
