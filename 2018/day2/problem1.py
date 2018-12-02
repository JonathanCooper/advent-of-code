import sys

def get_counts(word):
    counts = {}
    for c in word:
        try:
            counts[c] += 1
        except KeyError:
            counts[c] = 1
    return counts

def has(char_count, num):
    if num in char_count.values():
        return True
    else:
        return False

if __name__ == '__main__':
    contains_double, contains_triple = 0, 0
    infile = sys.argv[1]
    with open(infile) as fh:
        for line in fh:
            line = line.strip()
            counts = get_counts(line)
            if has(counts, 2):
                contains_double += 1
            if has(counts, 3):
                contains_triple += 1

    checksum = contains_double * contains_triple
    print(checksum)
