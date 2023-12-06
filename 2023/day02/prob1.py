

def check_game(data, red, green, blue):
    game_id, game_data = data.split(":")
    game_id = int(game_id.split()[-1])
    game_data = game_data.strip()
    sets = game_data.split(";")
    for set_ in sets:
        for cube_data in set_.split(","):
            num, color = cube_data.split()
            num = int(num)
            if color == "red":
                if num > red:
                    return 0
            elif color == "green":
                if num > green:
                    return 0
            elif color == "blue":
                if num > blue:
                    return 0
            else:
                raise ValueError(f"Unexpected color: {color}")
    return game_id

total = 0

with open("in.txt") as fh:
    for line in fh:
        line = line.strip()
        total += check_game(line, red=12, green=13, blue=14)

print(total)
