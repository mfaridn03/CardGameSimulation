# Setting up a deck of cards
from objectss.exceptions import *
from objectss.deck import Deck
from objectss.player import Player

import random
import typing


class Game:
    def __init__(self, playerlist: typing.List[Player]):
        self.deck = Deck()
        self.deck.shuffle()
        self.data = {
            "is_start_of_round": True,
            "play_to_beat": [],
            "round_history": [[]],
            "hand_sizes": [13, 13, 13, 13],
            "scores": [0, 0, 0, 0],
            "round_no": 0,
        }
        self.round_end = False
        self.game_end = False

        self.playerlist = playerlist  # 4 players always

    def deal(self):
        # deal 13 cards each to 4 players
        for _ in range(13):
            for player in self.playerlist:
                card = self.deck.deal()
                player.hand.append(card)

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

        for player in self.playerlist:
            player.sort_hand()
            print(player.name, ":", player.hand)

    def play(self):
        # play the game
        self.init_game()

        while not self.game_end:
            while not self.round_end:
                self.play_round()
                break

            break
        print("Game End")

    def play_round(self):
        # call each player's play() method
        for player in self.playerlist:
            move = player.play(
                self.data["is_start_of_round"],
                self.data["play_to_beat"],
                self.data["round_history"],
                self.data["hand_sizes"],
                self.data["scores"],
                self.data["round_no"],
            )
            print("Player", player.name, "played", " ".join(move))

            if self.data["is_start_of_round"]:
                if move is None:
                    raise InvalidMoveError("Must play a card on round start")

                if "3D" not in move:
                    raise InvalidMoveError("Must play 3D on round start")

            for card in move:
                player.hand.remove(card)

            self.data["is_start_of_round"] = False
            self.data["play_to_beat"] = move
            self.data["round_history"].append(move)
            self.data["hand_sizes"] = [len(player.hand) for player in self.playerlist]


if __name__ == "__main__":
    # test
    player1 = Player("A")
    player2 = Player("B")
    player3 = Player("C")
    player4 = Player("D")

    playerlist = [player1, player2, player3, player4]

    game = Game(playerlist)
    game.play()
