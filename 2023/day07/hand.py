

class Hand(object):
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = int(bid)
        self.hand_rankings = {
            0: "high card",
            1: "one pair",
            2: "two pair",
            3: "three of a kind",
            4: "full house",
            5: "four of a kind",
            6: "five of a kind",
        }

        self.rank = self.get_rank()

    def get_rank(self):
        counts = {}
        for card in self.cards:
            try:
                counts[card] += 1
            except KeyError:
                counts[card] = 1

        match sorted(counts.values(), reverse=True):
            case [1, 1, 1, 1, 1]:
                return 0
            case [2, 1, 1, 1]:
                return 1
            case [2, 2, 1]:
                return 2
            case [3, 1, 1]:
                return 3
            case [3, 2]:
                return 4
            case [4, 1]:
                return 5
            case [5]:
                return 6
            case _:
                raise ValueError(f"problem with counts: {sorted(counts.values(), reverse=True)}")

    @classmethod
    def gt(cls, hand1, hand2):
        card_rankings = "23456789TJQKA"
        if hand1.rank == hand2.rank:
            for i in range(5):
                if hand1.cards[i] == hand2.cards[i]:
                    continue
                return card_rankings.index(hand1.cards[i]) > card_rankings.index(hand2.cards[i])
            raise ValueError(f"Did not resolve comparison {hand1} {hand2}")
        else:
            return hand1.rank > hand2.rank

    def pretty(self):
        return self.hand_rankings[self.rank]

    def __repr__(self):
        return f"{self.cards} {self.pretty()} {self.bid}"
