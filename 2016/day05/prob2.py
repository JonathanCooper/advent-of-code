import hashlib

#door_id = "abc"
door_id = "abbhdwsy"
password = {}
found = set()
i = 0

while len(found) < 8:
    seed_str = f"{door_id}{str(i)}".encode()
    #print(seed_str)
    h = hashlib.new("md5")
    h.update(seed_str)
    digest = h.hexdigest()
    i += 1
    if all([ c == "0" for c in digest[:5] ]):
        #print(f"found digit {h.hexdigest()} i=={i}")
        position, target_c = digest[5], digest[6]
        if not position.isdigit():
            continue
        elif not 0 <= int(position) < 8:
            continue
        else: # valid position
            if position in found:
                continue
            else:
                password[position] = target_c
                found.add(position)
                print(password)

print("".join([ password[str(pos)] for pos in range(8) ]))
