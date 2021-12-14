
def run(pair_counts, rules, n=1):
    for _ in range(n):
        new_counts = {}
        for pair, count in pair_counts.items():
            if count == 0:
                continue
            middle = rules[pair]
            left = pair[0] + middle
            right = middle + pair[1]
            #print(f'splitting {pair} into {left} and {right}')
            for side in [left, right]:
                try:
                    new_counts[side] += count
                except KeyError:
                    new_counts[side] = count 
        pair_counts = new_counts
    return pair_counts

rules = {}
pair_counts = {}

with open('in.txt') as fh:
    for line in fh:
        line = line.strip()
        if line == '':
            continue
        if '->' not in line:
            template = list(line)
        else:
            pair, insertion = line.split(' -> ')
            pair_counts[pair] = 0
            rules[pair] = insertion

for i, c in enumerate(template[:-1]):
    pair = c + template[i + 1]
    pair_counts[pair] += 1


res = run(pair_counts, rules, 40)

letters = {}

for pair, count in res.items():
    for c in pair:
        try:
            letters[c] += count
        except KeyError:
            letters[c] = count

for c in [template[0], template[-1]]:
    letters[c] += 1


max_v = max([ v // 2 for k, v in letters.items() ])
min_v = min([ v // 2 for k, v in letters.items() ])
print(max_v - min_v)
