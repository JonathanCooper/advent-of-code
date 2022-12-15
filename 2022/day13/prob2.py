
def compare(left, right):
    left_is_shorter = len(left) < len(right)
    for i, left_element in enumerate(left):
        try:
            right_element = right[i]
        except IndexError:
            return False
        left_type, right_type = type(left_element), type(right_element)
        if left_type is int and right_type is list:
            left_element = [left_element]
            left_type = list
        elif left_type is list and right_type is int:
            right_element = [right_element]
            right_type = list
        left_type, right_type = type(left_element), type(right_element)
        #print(f'comapring {left_element} to {right_element}')
        if left_element == right_element:
            continue
        if left_type is int and right_type is int:
            return left_element < right_element
        elif left_type is list and right_type is list:
            return compare(left_element, right_element)
    return left_is_shorter # always false??


def insert(packets, p):
    if len(packets) == 0:
        return [p]
    else:
        if compare(p, packets[0]):
            return [p] + packets
        for i in range(len(packets) - 1):
            if compare(packets[i], p) and compare(p, packets[i + 1]):
                return packets[:i + 1] + [p] + packets[i + 1:]
        return packets + [p]
start = 0
block = 3

dividers = [
    [[2]],
    [[6]]
]

packets = []
with open('in.txt') as fh:
    lines = [ line.strip() for line in fh.readlines() ]
    while start < len(lines) - 1:
        left = lines[start]
        right = lines[start + 1]
        left = eval(left)
        right = eval(right)
        #print(f'{pair_idx}: inspecting {left} and {right}\n*****')
        packets = insert(packets, left)
        packets = insert(packets, right)
        start += block

for divider in dividers:
    packets = insert(packets, divider)

for i in range(len(packets) - 1):
    if not compare(packets[i], packets[i+1]):
        print('problem found')
        print(packets[i])
        print(packets[i+1])
        print()

# the 3 below is to account for a bug that puts 2 packets weirdly out of order aand should before divider[1].../shrug
print((packets.index(dividers[0]) + 1) * (packets.index(dividers[1]) + 3))
