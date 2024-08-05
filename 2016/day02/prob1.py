
class Pad(object):
    
    def __init__(self):
        self.x = 1
        self.y = 1
        self.grid = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8" ,"9"],
        ]

    def get_num(self):
        if self.x < 0 or self.x > 2:
            return False
        if self.y < 0 or self.y > 2:
            return False
        return self.grid[self.y][self.x]

    def move(self, direction):
        old_coords = (self.x, self.y)

        if direction == "U":
            self.y -= 1
        elif direction == "D":
            self.y += 1
        elif direction == "L":
            self.x -= 1
        elif direction == "R":
            self.x += 1
        else:
            raise ValueError(f"Unexpected direction: {direction}")
        if not self.get_num():
            self.x, self.y = old_coords
            return False
        else:
            return True

    def process_line(self, line):
        for direction in line:
            #print(f"moving {direction}")
            self.move(direction)
            #print(f"now at {self.get_num()}")
        return self.get_num()

    def find_code(self, instructions):
        code = ""
        for instruction in instructions:
            result = self.process_line(instruction)
            code += result
            #print(f"ran {instruction}, result: {result}, code: {code}")
        return code

instructions = []
with open('in.txt') as fh:
    for line in fh:
        line = line.strip()
        instructions.append(line)

pad = Pad()
print(pad.find_code(instructions))

