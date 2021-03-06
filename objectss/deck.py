import random


class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["S", "H", "D", "C"]:
            # set up number cards (10 = 0)
            for rank in range(2, 11):
                if rank == 10:
                    rank = "0"

                self.cards.append(f"{rank}{suit}")

            # set up face cards
            for face in ["J", "Q", "K", "A"]:
                self.cards.append(f"{face}{suit}")

    def __str__(self):
        return " ".join(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()
