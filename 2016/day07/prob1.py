
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

def abba(chunk):
    if len(chunk) < 4:
        return False
    for i in range(len(chunk) - 3):
        if chunk[i] == chunk[i + 1]:
            continue
        if chunk[i] == chunk[i + 3] and chunk[i + 1] == chunk[i + 2]:
            return True
    return False


def tls(address):
    outer, inner = get_chunks(address)
    #print(outer, inner)
    for chunk in inner:
        if abba(chunk):
            return False
    for chunk in outer:
        if abba(chunk):
            return True
    return False

def run_tests():
    assert(tls("abba[mnop]qrst") == True)
    assert(tls("abcd[bddb]xyyx") == False)
    assert(tls("aaaa[qwer]tyui") == False)
    assert(tls("ioxxoj[asdfgh]zxcvbn") == True)

run_tests()

total = 0
with open("in.txt") as fh:
    for line in fh:
        line = line.strip()
        #print(line, tls(line))
        if tls(line):
            total += 1

print(total)
