import hashlib

#door_id = "abc"
door_id = "abbhdwsy"
password = ""
i = 0

while len(password) < 8:
    seed_str = f"{door_id}{str(i)}".encode()
    #print(seed_str)
    h = hashlib.new("md5")
    h.update(seed_str)
    if all([ c == "0" for c in h.hexdigest()[:5] ]):
        #print(f"found digit {h.hexdigest()} i=={i}")
        password += h.hexdigest()[5]
    i += 1

print(password)
