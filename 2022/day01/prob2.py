
elfs = []

with open('in.txt') as fh:
    current_elf = 0
    for line in fh:
        if line == '\n':
            elfs.append(current_elf)
            current_elf = 0
        else:
            calories = int(line.strip())
            current_elf += calories

elfs.append(current_elf)
print(sum(sorted(elfs)[-3:]))

