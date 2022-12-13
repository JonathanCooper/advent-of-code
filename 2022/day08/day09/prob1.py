
class Rope(object):

    def __init__(self):
        self.headx = 0
        self.heady = 0
        self.tailx = 0
        self.taily = 0
        self.visited = set()

    def move(self, direction, num):
        for _ in range(num):
            if direction == 'U':
                self.heady += 1
            elif direction == 'D':
                self.heady -= 1
            elif direction == 'L':
                self.headx -= 1
            elif direction == 'R':
                self.headx += 1
            else:
                raise ValueError(f'Unxpected direction: {direction}')
            self.update_tail()

    def update_tail(self):
        x_diff = self.headx - self.tailx
        y_diff = self.heady - self.taily
        if abs(x_diff) == 2:
            self.tailx += (x_diff // 2)
            self.taily += y_diff
        elif abs(y_diff) == 2:
            self.tailx += x_diff
            self.taily += (y_diff // 2)
        #print(self)
        self.visited.add((self.tailx, self.taily))


    def num_positions(self):
        return len(self.visited)

    def __repr__(self):
        return f'HEAD: {(self.headx, self.heady)}, TAIL: {(self.tailx, self.taily)}'
rope = Rope()

with open('in.txt') as fh:
    for line in fh:
        line = line.strip()
        direction, num = line.split()
        num = int(num)
        rope.move(direction, num)

print(rope.num_positions())
