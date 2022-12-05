
stack_lines = []
instructions = []

with open('in.txt') as fh:
    for line in fh:
        line = line.rstrip('\n')
        if '[' in line:
            stack_lines.append(line)
        elif line == '':
            continue
        elif line.startswith('move'):
            instructions.append(line)
        elif line[1].isdigit():
            num_stacks = int(line.strip()[-1])
        else:
            raise ValueError(f'Unexpected line: {line}')

stacks = {}

for i in range(num_stacks):
    stacks[i + 1] = []

for line in stack_lines:
    line_items = []
    for i in range(0, num_stacks):
        item_idx = (i * 4) + 1
        #print(f'stack {i+1} gets {line[item_idx]}')
        item_val = line[item_idx]
        if item_val != ' ':
            stacks[i + 1].append(item_val)

for i in range(num_stacks):
    stacks[i + 1].reverse()

#print(f'Starting state:\n{stacks}\n')

for instruction in instructions:
    split = instruction.split()
    num = int(split[1])
    src = int(split[3])
    dst = int(split[5])
    new_vals = stacks[src][-num:]
    for _ in new_vals:
        val = stacks[src].pop()
    stacks[dst] += new_vals
    #print(stacks)

for i in range(num_stacks):
    print(stacks[i + 1][-1], end='')
print()
