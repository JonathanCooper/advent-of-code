
movements = {
    'N': (0, -1),
    'S': (0, 1),
    'E': (1, 0),
    'W': (-1, 0)
}

class Ship(object):


    def __init__(self):
        self.x = 0
        self.y = 0
        self.way_x = 10
        self.way_y = -1

    def process_inst(self, inst):
        action, num = inst[0], inst[1:]
        num = int(num)
        if action in ['L', 'R']:
            self.rotate(action, num)
            return
        elif action in ['N', 'S', 'E', 'W']:
            self.way_x += movements[action][0] * num
            self.way_y += movements[action][1] * num
            return
        elif action == 'F':
            self.x += self.way_x * num
            self.y += self.way_y * num
        else:
            raise ValueError(f'Unexpected action: {action}')

    def rotate(self, turn_dir, amount):
        rotations = int(amount / 90)
        for _ in range(rotations):
            if turn_dir == 'R':
                self.way_y *= -1
            elif turn_dir == 'L':
                self.way_x *= -1
            else:
                raise ValueError(f'Unexpected turn dir: {turn_dir}')
            self.way_x, self.way_y = self.way_y, self.way_x


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
        return f'Ship at {(self.x, self.y)}, waypoint at {(self.way_x, self.way_y)}'

ship = Ship()

with open('in.txt') as fh:
    for line in fh:
        line = line.strip()
        ship.process_inst(line)
        #print(ship)

print(ship.manhattan())        
