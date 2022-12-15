
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

    
start = 0
block = 3

pair_idx = 1
total = 0

with open('in.txt') as fh:
    lines = [ line.strip() for line in fh.readlines() ]
    while start < len(lines) - 1:
        left = lines[start]
        right = lines[start + 1]
        left = eval(left)
        right = eval(right)
        #print(f'{pair_idx}: inspecting {left} and {right}\n*****')
        if compare(left, right):
            total += pair_idx
            #print('CORRECT ORDER')
        pair_idx += 1
        start += block

print(total)
