from collections import Counter

def run(polymer, rules, n=1):
    rule_keys = set(rules.keys())
    for _ in range(n):
        print(f'running step {_}')
        insertions = {}
        for i, c in enumerate(polymer[:-1]):
            left, right = c, polymer[i + 1]
            rule_str = ''.join([left, right])
            if rule_str in rule_keys:
                insertions[i + 1] = rules[rule_str]
        polymer = insert(polymer, insertions)
    return polymer

def insert(polymer, insertions):
    offset = 0
    for k, v in sorted(insertions.items()):
        polymer.insert(k + offset, v)
        offset += 1
    return polymer

rules = {}

with open('test.txt') as fh:
    for line in fh:
        line = line.strip()
        if line == '':
            continue
        if '->' not in line:
            template = list(line)
        else:
            pair, insertion = line.split(' -> ')
            rules[pair] = insertion

polymer = run(template, rules, n=10)
print(polymer[:25])
counter = Counter(polymer)
common = counter.most_common()
print(common[0][1] - common[-1][1])
