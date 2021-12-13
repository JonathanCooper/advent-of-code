


with open('in.txt') as fh:
    line = fh.readline()
    line = line.strip()
    fish_vals = line.split(',')
    fish_vals = [ int(val) for val in fish_vals ]

fish_counts = {}

for i in range(9):
    fish_counts[i] = 0

for val in fish_vals:
    fish_counts[val] += 1

for i in range(256):
    resets = fish_counts[0]
    for j in range(8):
        fish_counts[j] = fish_counts[j + 1]
    fish_counts[6] += resets
    fish_counts[8] = resets

total = 0
for v in fish_counts.values():
    total += v

print(total)
