'''
Pair(27-89) contains Pair(7-88)
'''

class Pair(object):


    def __init__(self, s):
        s = s.split('-')
        self.start = int(s[0])
        self.end = int(s[1])


    def overlaps(self, other):
        if self.start in [other.start, other.end]:
            return True
        if self.end in [other.start, other.end]:
            return True
        if self.start > other.start:
            pair1, pair2 = other, self
        else:
            pair1, pair2 = self, other
        if pair2.start < pair1.end:
            #print(f'found overlaps {pair1},{pair2}')
            return True
        else:
            return False

    def __repr__(self):
        return f'Pair({self.start}-{self.end})'

overlap = 0

with open('in.txt') as fh:
    for line in fh:
        line = line.strip()
        pair1, pair2 = line.split(',')
        pair1 = Pair(pair1)
        pair2 = Pair(pair2)
        if pair1.overlaps(pair2):
            overlap += 1
print(overlap)
