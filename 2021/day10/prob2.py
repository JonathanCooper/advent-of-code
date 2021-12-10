import sys

scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

pairs = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

rev_pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
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


def get_close(line):
    curr_opens = []
    for c in line:
        if c in open_chars:
            curr_opens.append(c)
        elif c in close_chars:
            del(curr_opens[-1])
    for c in curr_opens[::-1]:
        yield rev_pairs[c]

open_chars = set(['(', '[', '{', '<'])
close_chars = set([')', ']', '}', '>'])


line_scores = []

with open('in.txt') as fh:
    for line in fh:
        score = 0
        line = line.strip()
        res = is_corrupted(line)
        if res:
            continue
        for c in get_close(line):
            score *= 5
            score += scores[c]
        line_scores.append(score)

line_scores.sort()
num_scores = len(line_scores)
middle = num_scores // 2
print(line_scores[middle])
