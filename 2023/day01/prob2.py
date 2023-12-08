
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

def replace_digits(line):
    new_str = ""
    #print(line)
    while len(line) > 0:
        #print(f"checking {line} to see if it starts with a spelled out digit")
        replaced = False
        for k, v in spellings.items():
            if line.startswith(k):
                new_str += v
                line = line[len(k):]
                replaced = True
                #print(f"replaced a digit, new_str is {new_str}")
                break
        if not replaced:
            #print("did not replace")
            new_str += line[0]
            line = line[1:]
    #print(new_str)
    return new_str

def process(line):
    line = line.strip()
    new_line = replace_digits(line)
    first = None
    for c in new_line:
        if c.isdigit():
            if not first:
                first = c
            last = c
    return int(first + last)

total = 0

#with open("in.txt") as fh:
#    for line in fh:
#        total += process(line)


with open("test3.txt") as fh:
    for test_str in fh:
        test_str = test_str.strip()
        print(test_str, process(test_str))

