
def priority(chr):
    num = ord(chr) - 96
    if num >= 1:
        return num
    else:
        return num + 58

total = 0

with open('in.txt') as fh:
    for line in fh:
        line = line.strip()
        midpoint = int(len(line) / 2)
        compartment1, compartment2 = set(line[:midpoint]), set(line[midpoint:])
        intersection = compartment1.intersection(compartment2)
        if len(intersection) > 1:
            raise ValueError(
                f'Found more than one element in both compartmens: {intersection}'
            )

        total += priority(intersection.pop())

print(total)
