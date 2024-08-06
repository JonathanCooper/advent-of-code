
def _tls(address):
    in_brackets = False
    for i in range(len(address) - 4):
        if in_brackets:
            continue
        elif address[i] == "[":
            in_brackets = True
            continue
        elif address[i] == "]":
            in_brackets = False
            continue
        else:
            if any([ c in ["[", "]"] for c in address[i:i+4] ]):
                continue

def get_chunks(address):
    """
    abba[mnop]qrst ->
    (["abba", "qrst"], ["mnop"])
    """
    outer, inner = [], []
    current_str = ""
    in_brackets = False
    for c in address:
        if c not in ["[", "]"]:
            current_str += c
        if not in_brackets:
            if c == "[":
                outer.append(current_str)
                current_str = ""
                in_brackets = True
        else:
            if c == "]":
                inner.append(current_str)
                current_str = ""
                in_brackets = False
    outer.append(current_str)
    return (outer, inner)

def _abba(chunk):
    if len(chunk) < 4:
        return False
    for i in range(len(chunk) - 3):
        if chunk[i] == chunk[i + 1]:
            continue
        if chunk[i] == chunk[i + 3] and chunk[i + 1] == chunk[i + 2]:
            return True
    return False

def get_babs(chunk):
    babs = []
    for i in range(len(chunk) - 2):
        if chunk[i] == chunk[i + 1]:
            continue
        if chunk[i] == chunk[i + 2]:
            babs.append(chunk[i:i+3])
    return babs

def bab2aba(bab):
    return f"{bab[1]}{bab[0]}{bab[1]}"

def ssl(address):
    outer, inner = get_chunks(address)
    #print(outer, inner)
    for chunk in inner:
        for bab in get_babs(chunk):
            for outer_chunk in outer:
                if bab2aba(bab) in outer_chunk:
                    return True
    return False

def run_tests():
    assert(ssl("aba[bab]xyz") == True)
    assert(ssl("xyx[xyx]xyx") == False)
    assert(ssl("aaa[kek]eke") == True)
    assert(ssl("zazbz[bzb]cdb") == True)

run_tests()

total = 0
with open("in.txt") as fh:
    for line in fh:
        line = line.strip()
        #print(line, tls(line))
        if ssl(line):
            total += 1

print(total)
