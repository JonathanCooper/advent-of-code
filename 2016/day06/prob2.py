
def get_top(counter):
    s = sorted(counter.items(), key=lambda x: x[1], reverse=False)
    #print(s)
    return s[0][0]

message = ""
positions = {}
initiated = False

with open("in.txt") as fh:
    for line in fh:
        line = line.strip()
        counter = {}
        word_len = len(line)
        if not initiated:
            for i in range(word_len):
                positions[i] = {}
            initiated = True
        for i, c in enumerate(line):
            try:
                positions[i][c] += 1
            except KeyError:
                positions[i][c] = 1


#message += get_top(counter)
for _, counter in sorted(positions.items(), key=lambda x: x[0]):
    message += get_top(counter)

print(message)
