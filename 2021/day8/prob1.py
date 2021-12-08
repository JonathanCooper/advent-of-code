
count = 0

with open('in.txt') as fh:
    for line in fh:
        line = line.strip()
        output = line.split('|')[1]
        output = output.lstrip()
        words = output.split()
        for word in words:
            if len(word) in [2, 3, 4, 7]:
                count += 1

print(count)
