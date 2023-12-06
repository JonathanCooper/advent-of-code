

def power_of(data):
    game_id, game_data = data.split(":")
    game_id = int(game_id.split()[-1])
    game_data = game_data.strip()
    sets = game_data.split(";")
    biggest = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for set_ in sets:
        for cube_data in set_.split(","):
            num, color = cube_data.split()
            num = int(num)
            if num > biggest[color]:
                biggest[color] = num
    return biggest["red"] * biggest["green"] * biggest["blue"]

total = 0

with open("in.txt") as fh:
    for line in fh:
        line = line.strip()
        total += power_of(line)

print(total)
