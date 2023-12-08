from hand2 import Hand

hands = []
with open("in.txt") as fh:
    for line in fh:
        line = line.strip()
        cards, bid = line.split()
        hands.append(Hand(cards, bid))

def quicksort(hand_list):
    if len(hand_list) <= 1:
        return hand_list
    smaller = []
    bigger = []
    pivot = hand_list[0]

    for hand in hand_list[1:]:
        if Hand.gt(hand, pivot):
            bigger.append(hand)
        else:
            smaller.append(hand)
    return quicksort(smaller) + [pivot] + quicksort(bigger)

sorted_hands = quicksort(hands)

total = 0

for i, hand in enumerate(sorted_hands):
    total += hand.bid * (i + 1)

print(total)
