import sys

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

pairs = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

def is_corrupted(line):
    '''
    (], {()()()>, (((()))}, and <([]){()}[{}]).
    '''
    curr_opens = []
    for c in line:
        if c in open_chars:
            curr_opens.append(c)
        elif c in close_chars:
            if curr_opens[-1] != pairs[c]:
                return c
            else:
                del(curr_opens[-1])
        else:
            raise ValueError(f'Unexpected char: {c}')
    return False

open_chars = set(['(', '[', '{', '<'])
close_chars = set([')', ']', '}', '>'])

total_score = 0

with open('in.txt') as fh:
    for line in fh:
        line = line.strip()
        res = is_corrupted(line)
        if res:
            total_score += scores[res]

print(total_score)
