import sys

def candidate(word1, word2):
    if word1[0] != word2[0] and word1[1] != word2[1]:
        return False
    else:
        return True

def check(pair):
    differences = 0
    i = 0
    while differences < 2 and i < len(pair[0]):
        if pair[0][i] != pair[1][i]:
            differences += 1
        i += 1
    if differences == 1:
        return True
    else:
        return False

def common_letters(pair):
    for i, c in enumerate(pair[0]):
        if c != pair[1][i]:
            break
    return ''.join(pair[0][:i] + pair[0][i+1:])

if __name__ == '__main__':
    infile = sys.argv[1]
    word_list = []
    with open(infile) as fh:
        for line in fh:
            line = line.strip()
            word_list.append(line)
    candidate_pairs = []
    for i in word_list:
        for j in word_list:
            if candidate(i, j):
                candidate_pairs.append((i, j))
    for pair in candidate_pairs:
        if check(pair):
            print(common_letters(pair))
            sys.exit(0)
