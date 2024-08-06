
class Screen(object):

    def __init__(self):
        self.pixels = {}
        for x in range(50):
            for y in range(6):
                self.pixels[(x, y)] = "."

    def __repr__(self):
        out_str = ""
        for y in range(6):
            for x in range(50):
                out_str += self.pixels[(x, y)]
            out_str += "\n"
        return out_str

    def rect(self, xlen, ylen):
        for y in range(ylen):
            for x in range(xlen):
                self.pixels[(x, y)] = "#"

    def column(self, x_val, offset):
        new_col = []
        for y in range(6):
            new_y = y - offset
            if new_y < 0:
                new_y = 6 + new_y
            new_col.append(self.pixels[(x_val, new_y)])
        for y in range(6):
            self.pixels[(x_val, y)] = new_col[y]

    def row(self, y_val, offset):
        new_col = []
        for x in range(50):
            new_x = x - offset
            if new_x < 0:
                new_x = 50 + new_x
            new_col.append(self.pixels[(new_x, y_val)])
        for x in range(50):
            self.pixels[(x, y_val)] = new_col[x]

    def on_pixels(self):
        return sum([ 1 if i == "#" else 0 for i in self.pixels.values() ])

def test():
    screen = Screen()
    screen.rect(3, 2)
    screen.column(1, 1)
    screen.row(0, 4)
    print(screen)

screen = Screen()

with open("in.txt") as fh:
    for line in fh:
        line = line.strip()
        split_line = line.split()
        instruction = split_line[0]
        if instruction == "rect":
            xlen, ylen = [ int(param) for param in split_line[1].split("x") ]
            screen.rect(xlen, ylen)
        elif instruction == "rotate":
            target = int(split_line[2].split("=")[1])
            offset = int(split_line[-1])
            if split_line[1] == "column":
                screen.column(target, offset)
            elif split_line[1] == "row":
                screen.row(target, offset)
            else:
                raise ValueError(f"Unexpected rotate command: {split_line[1]}")
        else:
            raise ValueError(f"Unexpected instruction: {instruction}")

print(screen)
print(screen.on_pixels())
