
class Wire(object):
    
    def __init__(self, instructions):
        self.instructions = instructions.split(',')
        self.position = (0, 0)
        self.points = set()

    def run_instructions(self):
        for instruction in self.instructions:
            self.move(instruction)

    def move(self, instruction):
        direction, distance = instruction[0], int(instruction[1:])
        #print(f'moving {direction} {distance}')
        for _ in range(distance):
            if direction == 'U':
                self.position = (self.position[0], self.position[1] + 1)
            elif direction == 'D':
                self.position = (self.position[0], self.position[1] - 1)
            elif direction == 'L':
                self.position = (self.position[0] - 1, self.position[1])
            elif direction == 'R':
                self.position = (self.position[0] + 1, self.position[1])
            else:
                raise Exception(f'Unknown direction: {direction}')
            self.points.add(self.position)
        #print(f'new position: {self.position}')

def manhattan(point):
    return abs(point[0]) + abs(point[1])

#testcases = [
#    '''R75,D30,R83,U83,L12,D49,R71,U7,L72
#U62,R66,U55,R34,D71,R55,D58,R83''',
#    '''R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
#U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'''
#]
#
#for testcase in testcases:

with open('in.txt') as fh:
    raw_txt = fh.read()

instructions1, instructions2 = raw_txt.rstrip('\n').split('\n')
wire1 = Wire(instructions1)
wire2 = Wire(instructions2)
wire1.run_instructions()
wire2.run_instructions()

intersections = set()
for point in wire1.points:
    if point in wire2.points:
        intersections.add(point)
print(min([ manhattan(i) for i in intersections ]))
