
class Position(object):


    def __init__(self, horizontal=0, depth=0, aim=0):
        self.horizontal = horizontal
        self.depth = depth
        self.aim = aim

    def move(self, direction, distance):
        if direction == 'forward':
            position.horizontal += distance
            self.depth += self.aim * distance
        elif direction == 'up':
            position.aim -= distance
        elif direction == 'down':
            position.aim += distance
        else:
            raise ValueError(f'unknown direction: {direction}')

position = Position()

with open('in.txt') as fh:
    for line in fh:
        line = line.strip()
        direction, distance = line.split()
        distance = int(distance)
        position.move(direction, distance)

print(position.horizontal * position.depth)
