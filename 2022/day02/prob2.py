
class Shape(object):


    def __init__(self, symbol):
        if symbol == 'A':
            self.name = 'ROCK'
            #self.shape_score = 1
            self.beats = 'SCISSORS'
            self.loses_to = 'PAPER'
        elif symbol == 'B':
            self.name = 'PAPER'
            #self.shape_score = 2
            self.beats = 'ROCK'
            self.loses_to = 'SCISSORS'
        elif symbol == 'C':
            self.name = 'SCISSORS'
            #self.shape_score = 3
            self.beats = 'PAPER'
            self.loses_to = 'ROCK'
        else:
            raise ValueError(f'Unexpected symbol: {symbol}')

    def round_score(self, desired_result):
        if desired_result == 'X':
            desired_shape = self.beats
            outcome_score = 0
        elif desired_result == 'Y':
            desired_shape = self.name
            outcome_score = 3
        elif desired_result == 'Z':
            desired_shape = self.loses_to
            outcome_score = 6
        else:
            raise ValueError(f'Unexpected desired_result: {desired_result}')
        #print(self.name, desired_result, desired_shape, self.shape_score(desired_shape), outcome_score)
        return outcome_score + self.shape_score(desired_shape)

    def shape_score(self, name):
        scores = {
            'ROCK': 1,
            'PAPER': 2,
            'SCISSORS': 3
        }
        return scores[name]

total = 0
with open('in.txt') as fh:
    for line in fh:
        opp_symbol, me_symbol = line.split()
        opp = Shape(opp_symbol)
        total += opp.round_score(me_symbol)
        #print(opp_symbol, me_symbol, total)
print(total)
