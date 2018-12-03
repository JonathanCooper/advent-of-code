import sys

class Claim():

    def __init__(self, claim_txt):
        claim_id, _, margins, size = line.strip().split()
        self.id = claim_id
        
        margins = margins.strip(':')
        margin_split = margins.split(',')
        self.left_margin = int(margin_split[0])
        self.top_margin = int(margin_split[1])
        
        size_split = size.split('x')
        self.width = int(size_split[0])
        self.height = int(size_split[1])

    def __repr__(self):
        print(f'left_margin: {self.left_margin}, top_margin: {self.top_margin}, width: {self.width}, height: {self.height}')

class Grid():

    def __init__(self, n):
        self.bitmap = []
        row = [0] * n
        for i in range(n):
            self.bitmap.append(list(row))
        self.claim_tracking = {}

    def process(self, claim):
        #print(f'processing claim:\n', claim)
        for row in range(claim.top_margin, claim.top_margin + claim.height):
            for column in range(claim.left_margin, claim.left_margin + claim.width):
                #print(f'marking row {row+1}, column {column+1}')
                #print(f'from {self.bitmap[row][column]} to {self.bitmap[row][column] + 1}')
                self.bitmap[row][column] += 1
                point = (column, row)
                try:
                    self.claim_tracking[point].append(claim.id)
                except KeyError:
                    self.claim_tracking[point] = [claim.id]

    def check_unique(self, claim):
        for row in range(claim.top_margin, claim.top_margin + claim.height):
            for column in range(claim.left_margin, claim.left_margin + claim.width):
                if self.bitmap[row][column] > 1:
                    return False
        return True

    def duplicates(self):
        total = 0
        for row in self.bitmap:
            for point in row:
                if point > 1:
                    total += 1
        return total

    def __repr__(self):
        repr_str = ''
        for row in self.bitmap:
            for point in row:
                repr_str += str(point)
            repr_str += '\n'
        return repr_str
            
if __name__ == '__main__':
    grid = Grid(int(sys.argv[2]))
    infile = sys.argv[1]
    with open(infile) as fh:
        for line in fh:
            claim = Claim(line)
            grid.process(claim)
    with open(infile) as fh:
        for line in fh:
            claim = Claim(line)
            if grid.check_unique(claim):
                print(claim.id)
                sys.exit(0)

