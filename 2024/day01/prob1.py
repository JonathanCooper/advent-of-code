
left_list, right_list = [], []

with open("in.txt") as fh:
    for line in fh:
        s = line.split()
        left_list.append(int(s[0]))
        right_list.append(int(s[1]))

left_list.sort()
right_list.sort()

total = 0
for i in range(len(left_list)):
    distance = abs(left_list[i] - right_list[i])
    total += distance

print(total)
