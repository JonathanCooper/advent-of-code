
class Wire(object):
    
    def __init__(self, instructions):
        self.instructions = instructions.split(',')
        self.position = (0, 0)
        self.points = set()
        self.steps = 0
        self.point_steps = {}

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
            self.steps += 1
            if not self.position in self.points:
                self.points.add((self.position))
                self.point_steps[self.position] = self.steps

def signal_delay(point, wire1, wire2):
    return wire1.point_steps[point] + wire2.point_steps[point]

#testcases = [
#    '''R75,D30,R83,U83,L12,D49,R71,U7,L72
#U62,R66,U55,R34,D71,R55,D58,R83''',
#    '''R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
#U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'''
#]
#
#for testcase in testcases:

with open('in.txt') as fh:
#with open('test.txt') as fh:
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
#for intersection in intersections:
#    signal_delay = wire1.point_steps[intersection] + wire2.point_steps[intersection]
#    print(signal_delay)

answer = min([ signal_delay(intersection, wire1, wire2) for intersection in intersections ])
print(answer)
