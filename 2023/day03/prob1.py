from grid import Grid


grid = Grid()

with open("in.txt") as fh:
    for line in fh:
        line = line.strip()
        grid.add_row(line)

current_word = ""
found_symbol = False
total = 0

for x, y, c in grid:
    #print(f"current c {c}")
    if c.isdigit():
        current_word += c
        #print(f"current word {current_word}")
        for nx, ny in grid.neighbors(x, y, diag=True):
            neighbor_val = grid.get_val(nx, ny)
            if neighbor_val != "." and not neighbor_val.isdigit():
                found_symbol = True
                #print(f"found symbol {neighbor_val}")
                break
    else:
        if found_symbol:
            total += int(current_word)
            #print(f"found word {current_word}")
        #elif current_word != "":
        #    print(f"{current_word} on row {y} is not a part")
        current_word = ""
        found_symbol = False

if found_symbol:
    total += current_word

print(total)
