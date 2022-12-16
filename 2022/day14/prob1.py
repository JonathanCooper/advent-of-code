
class Grain(object):
    
    def __init__(self):
        self.x = 500
        self.y = 0

    def coords(self):
        return (self.x, self.y)

class Cave(object):

    def __init__(self):
        self.scan = set()
        self.abyss = 0

    def set_val(self, x, y):
        self.scan.add((x, y))

    def draw(self, from_coords, to_coords):
        #print(f'running draw({from_coords}, {to_coords})')
        if from_coords[0] == to_coords[0]:
            if from_coords[1] > to_coords[1]:
                from_coords, to_coords = to_coords, from_coords
        elif from_coords[1] == to_coords[1]:
            if from_coords[0] > to_coords[0]:
                 from_coords, to_coords = to_coords, from_coords
        else:
            raise ValueError(f'Diagonal line? {from_coords} {to_coords}')
        for x in range(from_coords[0], to_coords[0] + 1):
            for y in range(from_coords[1], to_coords[1] + 1):
                #print(f'draw at {(x, y)}')
                self.set_val(x, y)
                self.abyss = max([self.abyss, y])

    def drop_sand(self):
        ''' 
        Returns True if the grain falls into the abyss
        Returns False if the grain comes to a rest
        '''
        resting = False
        grain = Grain()
        while True:
            #print(f'grain at {grain.coords()}')
            candidates = [
                (grain.x, grain.y + 1),
                (grain.x - 1, grain.y + 1),
                (grain.x + 1, grain.y + 1)
            ]
            #print(f'checking candidates {candidates}')
            #print([ candidate in self.scan for candidate in candidates ])
            if all([ candidate in self.scan for candidate in candidates ]):
                #print(f'grain resting at {grain.coords()}')
                self.set_val(grain.x, grain.y)
                return False
            for candidate in candidates:
                if candidate not in self.scan:
                    grain.x = candidate[0]
                    grain.y = candidate[1]
                    if grain.y > self.abyss:
                        return True
                    break

    def run(self):
        grains = 0
        done = False
        while not done:
            res = self.drop_sand()
            if res:
                return grains    
            else:
                grains += 1
cave = Cave()

start = None
with open('in.txt') as fh:
    for line in fh:
        line = line.strip()
        coords = line.split(' -> ')
        for coord in coords:
            s = coord.split(',')
            end = (int(s[0]), int(s[1]))
            #print(start, end)
            if start:
                cave.draw(start, end)
            start = end
        start = None 

#print(cave.scan)
print(cave.run())

