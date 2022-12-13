
class Knot(object):
    
    def __init__(self):
        self.x = 0
        self.y = 0

    def __repr__(self):
        return f'{(self.x, self.y)}'

class Rope(object):

    def __init__(self):
        self.knots = {}
        for i in range(10):
            self.knots[i] = Knot()
        self.tail_visited = set([(0, 0)])
        
    def move(self, direction, num):
        for _ in range(num):
            if direction == 'U':
                self.knots[0].y += 1
            elif direction == 'D':
                self.knots[0].y -= 1
            elif direction == 'L':
                self.knots[0].x -= 1
            elif direction == 'R':
                self.knots[0].x += 1
            else:
                raise ValueError(f'Unxpected direction: {direction}')
            self.update_tails()
            #print(self)
        
    def update_tails(self):
        for i in range(1, 10):
            this_tail = self.knots[i]
            this_head = self.knots[i - 1]
            x_diff = this_head.x - this_tail.x
            y_diff = this_head.y - this_tail.y
            #print(f'checking knot {i}, x_diff: {x_diff}, y_diff: {y_diff}')
            if abs(x_diff) == 2 and abs(y_diff) == 2:
                this_tail.x += (x_diff // 2)
                this_tail.y += (y_diff // 2)
            elif abs(x_diff) == 2:
                this_tail.x += (x_diff // 2)
                this_tail.y += y_diff
            elif abs(y_diff) == 2:
                this_tail.x += x_diff
                this_tail.y += (y_diff // 2)
        self.tail_visited.add((self.knots[9].x, self.knots[9].y))

    def num_positions(self):
        return len(self.tail_visited)

    def __repr__(self):
        repr_str = ''
        for i in range(10):
            repr_str += f'{i} is at {self.knots[i]} '
        return repr_str + '\n'

rope = Rope()

with open('in.txt') as fh:
    for line in fh:
        line = line.strip()
        direction, num = line.split()
        num = int(num)
        #print(line)
        rope.move(direction, num)

print(rope.num_positions())
