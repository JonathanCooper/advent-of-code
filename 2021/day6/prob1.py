
class Fish(object):


    def __init__(self, timer=8):
        self.timer = timer
        self.children = []

    def advance(self):
        for child in self.children:
            child.advance()
        if self.timer == 0:
            new_fish = Fish()
            self.children.append(new_fish)
            self.timer = 6
        else:
            self.timer -= 1

    def count(self):
        c = 0
        for fish in self.children:
            c += fish.count()
        return c + 1

start_fish = []

with open('test.txt') as fh:
    line = fh.readline()
    line = line.strip()
    fish_vals = line.split(',')
    fish_vals = [ int(val) for val in fish_vals ]
    for val in fish_vals:
        fish = Fish(val)
        start_fish.append(fish)

for i in range(80):
    for fish in start_fish:
        fish.advance()

total = 0
for fish in start_fish:
    total += fish.count()
print(total)
