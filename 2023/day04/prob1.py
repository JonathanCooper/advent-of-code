
def process(game):
    game_info = game.split(":")[1]
    winning_nums, my_nums = game_info.split("|")
    winning_nums = set(winning_nums.split())
    my_nums = my_nums.split()
    wins = 0
    for num in my_nums:
        if num in winning_nums:
            wins +=1
    return 2 ** (wins - 1) if wins > 0 else 0

total = 0

with open("in.txt") as fh:
    for line in fh:
        line = line.strip()
        total += process(line)

print(total)
