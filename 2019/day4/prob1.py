

def meets_criteria(word):
    return (
        len(word) == 6 and
        contains_double(word) and
        does_not_decrease(word)
    )

def contains_double(word):
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            return True
    return False

def does_not_decrease(word):
    digits = [ int(c) for c in word]
    for i in range(len(digits) - 1):
        if digits[i + 1] < digits[i]:
            return False
    return True

testcases = [
    "111111",
    "223450",
    "123789"
]

#for testcase in testcases:
#    print(f'{testcase}, {meets_criteria(testcase)}')

count = 0
for i in range(183564, 657475):
    word = str(i)
    if meets_criteria(word):
        count += 1

print(count)
