from Objects.utils import *
from Objects.deck import *
from Objects.player import *
import random

class Game:
    def __init__(self, playerlist: typing.List[Player]):
        self.deck = Deck()
        self.deck.shuffle()
        self.data = {
            "is_start_of_round": True,
            "play_to_beat": [],
            "round_history": [[]],
            "hand_sizes": [],
            "scores": [],
            "round_no": 0,
            "is_rev": False,
        }
        self.trick_end = False
        self.round_end = False
        self.game_end = False
        self.last_round_victor = None

        self.playerlist = playerlist    # may have more than 4 players
        self.data["hand_sizes"] = [0] * len(playerlist)
        self.data["scores"] = [0] * len(playerlist)

    def deal(self):
        # empty all hands
        for idx, player in enumerate(self.playerlist):
            player.hand = []
            self.data["hand_sizes"][idx] = 0

        # randomise starting player
        offset = random.randint(0, len(self.playerlist) - 1)

        # deal cards to each player until deck is empty; deck size is fixed at 54
        for i in range(54):
            card = self.deck.deal()
            curr_player = (i + offset) % len(self.playerlist)
            self.playerlist[curr_player].hand.append(card)
            self.data["hand_sizes"][curr_player] += 1

    def init_game(self):
        self.deal()
        # player that has 3D will always go first
        otherplayers = []
        firstplayer = None

        for player in self.playerlist:
            if "3D" in player.hand:
                firstplayer = player
            else:
                otherplayers.append(player)

        # randomise the order of the other players
        random.shuffle(otherplayers)
        self.playerlist = [firstplayer] + otherplayers

    def play_text_based(self):
        pass

    def play_round(self):
        pass


if __name__ == "__main__":
    # main game loop
    pass
