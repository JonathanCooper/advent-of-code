
def priority(chr):
    num = ord(chr) - 96
    if num >= 1:
        return num
    else:
        return num + 58

total = 0
startline = 0
blocksize = 3

with open('in.txt') as fh:
    lines = fh.readlines()
    while startline + blocksize <= len(lines):
        #print(f'checking group starting at {startline}')
        bags = [ l.strip() for l in lines[startline:startline + blocksize] ]
        bag2, bag3 = [ set(bag) for bag in bags[1:] ]
        for c in bags[0]:
            if c in bag2 and c in bag3:
                total += priority(c)
                break
        #print('incrementing')
        startline += blocksize

print(total)

