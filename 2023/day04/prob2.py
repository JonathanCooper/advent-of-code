
def process(game):
    global copies
    id_info, game_info = game.split(":")
    game_id = int(id_info.split()[1])
    winning_nums, my_nums = game_info.split("|")
    winning_nums = set(winning_nums.split())
    my_nums = my_nums.split()
    multiplier = copies[game_id]
    wins = sum([ 1 for num in my_nums if num in winning_nums ])
    for i in range(game_id + 1, game_id + wins + 1):
        try:
            copies[i] += 1 * multiplier
        except KeyError:
            copies[i] = 1 * multiplier
    #print(f"end of card {game_id}, copies: {copies}")

i = 0
cards = []
copies = {}
with open("in.txt") as fh:
    for line in fh:
        line = line.strip()
        cards.append(line)
        i += 1
        copies[i] = 1

for card in cards:
    process(card)

print(sum(copies.values()))
#print(total)
