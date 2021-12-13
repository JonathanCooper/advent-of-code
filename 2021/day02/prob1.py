
class Position(object):


    def __init__(self, horizontal, depth):
        self.horizontal = horizontal
        self.depth = depth

position = Position(0, 0)

with open('in.txt') as fh:
    for line in fh:
        line = line.strip()
        direction, distance = line.split()
        distance = int(distance)
        if direction == 'forward':
            position.horizontal += distance
        elif direction == 'up':
            position.depth -= distance
        elif direction == 'down':
            position.depth += distance
        else:
            raise ValueError(f'unknown direction: {direction}')

print(position.horizontal * position.depth)
