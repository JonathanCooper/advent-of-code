
movements = {
    'N': (0, -1),
    'S': (0, 1),
    'E': (1, 0),
    'W': (-1, 0)
}

class Ship(object):


    def __init__(self):
        self.direction = 'E'
        self.x = 0
        self.y = 0

    def process_inst(self, inst):
        action, num = inst[0], inst[1:]
        num = int(num)
        if action in ['L', 'R']:
            self.turn(action, num)
            return
        elif action in ['N', 'S', 'E', 'W']:
            direction = action
        elif action == 'F':
            direction = self.direction
        else:
            raise ValueError(f'Unexpected action: {action}')
        self.x += movements[direction][0] * num
        self.y += movements[direction][1] * num
        return

    def turn(self, turn_dir, amount):
        directions = ['E', 'S', 'W', 'N']
        current_idx = directions.index(self.direction)
        turns = int(amount / 90)
        if turn_dir == 'L':
            turns = turns * -1
        new_idx = (current_idx + turns) % 4
        self.direction = directions[new_idx]

    def manhattan(self):
        return abs(self.x) + abs(self.y)

    def __repr__(self):
        return f'Ship at {(self.x, self.y)} facing {self.direction}'

ship = Ship()

with open('in.txt') as fh:
    for line in fh:
        line = line.strip()
        ship.process_inst(line)

print(ship.manhattan())        
