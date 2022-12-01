
max_elf_cals = 0

with open('in.txt') as fh:
    current_elf = 0
    for line in fh:
        if line == '\n':
            max_elf_cals = max([max_elf_cals, current_elf])
            current_elf = 0
        else:
            calories = int(line.strip())
            current_elf += calories

print(max_elf_cals)

