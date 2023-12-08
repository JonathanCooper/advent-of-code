

with open("in.txt") as fh:
    lines = fh.readlines()

parts = "".join(lines).split("\n\n")

seed_info = parts[0]
seeds = seed_info.split(":")[1].strip().split()
seed_range_info = [ int(seed) for seed in seeds ]

seed_ranges = []
for i in range(0, len(seed_range_info) - 1, 2):
    range_start, range_len = seed_range_info[i], seed_range_info[i+1]
    #print(f"checking {range_len} seeds starting at {range_start}")
    range_end = range_start + range_len
    seed_ranges.append((range_start, range_end))

location = 0
while True:
    seed = location
    for part in parts[:0:-1]:
        map_name = part.strip().split("\n")[0]
        ranges = part.strip().split("\n")[1:]
        #print(f"running {map_name}")
        for range_ in ranges:
            #print(f"checking {range_}")
            dst_start, src_start, length = [ int(i) for i in range_.split() ]
            if dst_start <= seed < dst_start + length:
                seed = seed - dst_start + src_start
                break
    #print(f"converted location {location} to seed {seed}, checking ranges")
    for seed_range in seed_ranges:
        #print(f"checking if {seed} is in {seed_range}")
        if seed_range[0] <= seed < seed_range[1]:
            print(location)
            exit(0)
    location += 1
