
left_list = []
right_counts = {}

with open("in.txt") as fh:
    for line in fh:
        s = line.split()
        left_list.append(int(s[0]))
        try:
            right_counts[int(s[1])] += 1
        except KeyError:
            right_counts[int(s[1])] = 1


total = 0
for num in left_list:
    try:
        similarity = num * right_counts[num]
    except KeyError:
        similarity = 0
    total += similarity 

print(total)
