
class Shape(object):


    def __init__(self, symbol):
        if symbol in ['A', 'X']:
            self.name = 'ROCK'
            self.shape_score = 1
            self.beats = 'SCISSORS'
            self.loses_to = 'PAPER'
        elif symbol in ['B', 'Y']:
            self.name = 'PAPER'
            self.shape_score = 2
            self.beats = 'ROCK'
            self.loses_to = 'SCISSORS'
        elif symbol in ['C', 'Z']:
            self.name = 'SCISSORS'
            self.shape_score = 3
            self.beats = 'PAPER'
            self.loses_to = 'ROCK'
        else:
            raise ValueError(f'Unexpected symbol: {symbol}')

    def round_score(self, opponent_name):
        if opponent_name == self.name:
            return self.shape_score + 3
        elif opponent_name == self.loses_to:
            return self.shape_score + 0
        elif opponent_name == self.beats:
            return self.shape_score + 6
        else:
            raise ValueError(f'Unexpected opponent name: {opponent_name}')

total = 0
with open('in.txt') as fh:
    for line in fh:
        opp_symbol, me_symbol = line.split()
        opp = Shape(opp_symbol)
        me = Shape(me_symbol)
        total += me.round_score(opp.name)

print(total)
