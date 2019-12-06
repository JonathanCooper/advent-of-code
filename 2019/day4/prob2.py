import sys

class Group(object):
    
    def __init__(self):
        self.char = ''
        self.count = 0

def meets_criteria(word):
    return (
        len(word) == 6 and
        contains_exactly_double(word) and
        does_not_decrease(word)
    )

def contains_exactly_double(word):
    current_group = Group()
    for i in range(len(word)):
        if word[i] != current_group.char:
            if current_group.count == 2:
                return True
            else:
                current_group.char = word[i]
                current_group.count = 1
        else:
            current_group.count += 1
    return current_group.count == 2

def does_not_decrease(word):
    digits = [ int(c) for c in word]
    for i in range(len(digits) - 1):
        if digits[i + 1] < digits[i]:
            return False
    return True

testcases = [
    "112233",
    "123444",
    "111122"
]

#for testcase in testcases:
#    print(f'{testcase}, {meets_criteria(testcase)}')

count = 0
for i in range(183564, 657475):
    word = str(i)
    if meets_criteria(word):
        count += 1

print(count)
