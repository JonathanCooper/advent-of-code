
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

#def replace_digits(line):
#    new_str = ""
#    #print(line)
#    while len(line) > 0:
#        #print(f"checking {line} to see if it starts with a spelled out digit")
#        replaced = False
#        for k, v in spellings.items():
#            if line.startswith(k):
#                new_str += v
#                line = line[len(k):]
#                replaced = True
#                #print(f"replaced a digit, new_str is {new_str}")
#                break
#        if not replaced:
#            #print("did not replace")
#            new_str += line[0]
#            line = line[1:]
#    #print(new_str)
#    return new_str

def process(line):
    line = line.strip()
    i = 0
    found = False
    while not found:
        if line[i].isdigit():
            first = line[i]
            found = True
            break
        for k,v in spellings.items():

            if line[i:].startswith(k):
                first = v
                found = True
                break
        i += 1

    j = len(line)
    found = False
    while not found:
        if line[j-1].isdigit():
            last = line[j-1]
            found = True
            break
        for k, v in spellings.items():
            if line[:j+1].endswith(k):
                last = v
                found = True
                break
        j -= 1
    return int(first + last)

total = 0

with open("in.txt") as fh:
    for line in fh:
        total += process(line)

print(total)
