
def filter(nums, digit=0, most=True):
    if len(nums) == 1:
        return nums
    ones, zeros = [], []
    for num in nums:
        if num[digit] == '0':
            zeros.append(num)
        elif num[digit] == '1':
            ones.append(num)
        else:
            raise ValueError(f'unknown value: {num[digit]}')
    if most:
        if len(ones) >= len(zeros):
            return filter(ones, digit + 1) 
        else:
            return filter(zeros, digit +1)
    else:
        if len(zeros) <= len(ones):
            return filter(zeros, digit + 1, False)
        else:
            return filter(ones, digit + 1, False)

nums = []

with open('in.txt') as fh:
    for line in fh:
        line = line.strip()
        nums.append(line)

oxygen = filter(nums)
c02 = filter(nums, 0, False)

o = oxygen[0]
c = c02[0]
print(int(o, 2) * int(c, 2))
