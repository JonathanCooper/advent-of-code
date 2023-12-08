

with open("in.txt") as fh:
    lines = fh.readlines()

parts = "".join(lines).split("\n\n")

seed_info = parts[0]
seeds = seed_info.split(":")[1].strip().split()
seeds = [ int(seed) for seed in seeds ]

results = []
for seed in seeds:
    for part in parts[1:]:
        map_name = part.strip().split("\n")[0]
        ranges = part.strip().split("\n")[1:]
        for range_ in ranges:
            dst_start, src_start, length = [ int(i) for i in range_.split() ]
            if src_start <= seed < src_start + length:
                seed = dst_start + seed - src_start
                break
        #print(f"end of {map_name}, currently {seed}") 
    #print(f"found location {seed}")
    results.append(seed)


print(min(results))
    
