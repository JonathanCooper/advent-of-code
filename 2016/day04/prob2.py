
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
    sector = int(split_md[0])
    checksum = split_md[1].rstrip("]")
    name = "".join(name)

    if top(name, 5) == checksum:
        return (decrypt(name, sector), sector)
    else:
        return False

def rotate(c, n):
    if c == "-":
        return " "
    rotate_by = n % 26
    new = ord(c) + rotate_by
    if new > 122:
        new -= 26
    return chr(new)

def decrypt(room, sector):
    return "".join([ rotate(c, sector) for c in room ])

#print(rotate("z", 343))
print(decrypt("qzmt-zixmtkozy-ivhz", 343))


with open("in.txt") as fh:
    for line in fh:
        line = line.strip()
        res = check(line)
        if res:
            print(res)

