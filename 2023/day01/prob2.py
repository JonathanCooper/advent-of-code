
spellings = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def _replace_digits(line):
    print(line)
    i = 0
    while i < len(line):
        print(i, len(line), line[i:])
        replaced = False
        for k, v in spellings.items():
            if line[i:].startswith(k):
                line = line.replace(k, v)
                break
        i += 1
    print(" ", line)
    return line

def replace_digits(line):
    new_str = ""
    #print(line)
    while len(line) > 0:
        replaced = False
        for k, v in spellings.items():
            if line.startswith(k):
                new_str += v
                line = line[len(k):]
                replaced = True
                break
        if not replaced:
            new_str += line[0]
            line = line[1:]
    #print(new_str)
    return new_str

def process(line):
    line = line.strip()
    line = replace_digits(line)
    first = None
    for c in line:
        if c.isdigit():
            if not first:
                first = c
            last = c
    #print(int(first + last))
    return int(first + last)

total = 0

with open("in.txt") as fh:
    for line in fh:
        total += process(line)

print(total)
