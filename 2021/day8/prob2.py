
'''
2 segments:  c and f, 1
3 segments but not in 1:  a, 7
take 3 len6 digits, the segments that is in all of them but is not a is b
take 3 len5 digits, the segment that appears in only one but is not b is e
in the len 4 digit, the segment that is not in the len2 digit and is not b is d
in the len6 digit that contains a, b , e, and d, the segment that is in the len2 digit is f, the one that is not is c
remaining one is g
'''

def decode(lengths):
    for digit in lengths[3]:
        for char in digit:
            if char not in lengths[2][0]:
                a = char
    b_candidates = list(lengths[6][0])
    for digit in lengths[6][1:]:
        for char in lengths[6][0]:
            if char not in digit:
                b_candidates.remove(char)
    b_candidates.remove(a)
    for candidate in b_candidates:
        if candidate not in lengths[4][0]:
            g = candidate
    b_candidates.remove(g)
    for candidate in b_candidates:
        if candidate not in lengths[2][0]:
            b = candidate
    b_candidates.remove(b)
    f = b_candidates[0]
    e_counts = {}
    for digit in lengths[5]:
        for char in digit:
            try:
                e_counts[char] += 1
            except KeyError:
                e_counts[char] = 1
    for k, v in e_counts.items():
        if v == 1:
            if k != b:
                e = k
    for char in lengths[4][0]:
        if char != b and char not in lengths[2][0]:
            d = char
    found = [a, b, d, e, f, g]
    for char in lengths[7][0]:
        if char not in found:
            c = char
    mapping = {
        'a': a,
        'b': b,
        'c': c,
        'd': d,
        'e': e,
        'f': f,
        'g': g
    }
    return mapping

def get_digit(signal, mapping):
    if len(signal) == 2:
        return 1
    elif len(signal) == 3:
        return 7
    elif len(signal) == 4:
        return 4
    elif len(signal) == 7:
        return 8
    elif len(signal) == 5:
        if mapping['b'] in signal:
            return 5
        elif mapping['e'] in signal:
            return 2
        else:
            return 3
    elif len(signal) == 6:
        if mapping['d'] not in signal:
            return 0
        elif mapping['c'] in signal:
            return 9
        else:
            return 6
total = 0

with open('in.txt') as fh:
    for line in fh:
        lengths = {}
        line = line.strip()
        patterns, output = line.split('|')
        words = patterns.split()
        for word in words:
            try:
                lengths[len(word)].append(word)
            except KeyError:
                lengths[len(word)] = [word]
        mapping = decode(lengths)
        output_val = ''
        for word in output.split():
            output_val += str(get_digit(word, mapping))
        total += int(output_val)

print(total)


