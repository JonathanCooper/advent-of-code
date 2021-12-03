
nums = []

with open('in.txt') as fh:
    for line in fh:
        line = line.strip()
        nums.append(line)

gamma, epsilon = '', ''

for i in range(len(nums[0])):
    zero_count = 0
    one_count = 0
    for num in nums:
        if num[i] == '0':
            zero_count += 1
        elif num[i] == '1':
            one_count += 1
        else:
            raise ValueError(f'unexpected value: {num[i]}')
    if zero_count > one_count:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'


print(int(gamma, 2) * int(epsilon, 2))
