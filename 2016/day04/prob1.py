
def top(name, n):
    counts = {}
    for c in name:
        try:
            counts[c] += 1
        except KeyError:
            counts[c] = 1

    s = sorted(counts.items(), key=lambda x: (x[1], -ord(x[0])), reverse=True)
    checksum = "".join([ pair[0] for pair in s[:n] ])
    return checksum

def check(room):
    split_room = room.split("-")
    name, metadata = split_room[:-1], split_room[-1]
    split_md = metadata.split("[")
    sector = split_md[0]
    checksum = split_md[1].rstrip("]")
    name = "".join(name)

    if top(name, 5) == checksum:
        return int(sector)
    else:
        return 0

tests = [
    "aaaaa-bbb-z-y-x-123[abxyz]",
    "a-b-c-d-e-f-g-h-987[abcde]",
    "not-a-real-room-404[oarel]",
    "totally-real-room-200[decoy]",
]

sum = 0
with open("in.txt") as fh:
    for line in fh:
        line = line.strip()
        sum += check(line)

print(sum)

