# Setting up a deck of cards
from Objects.exceptions import *
from Objects.deck import Deck
from Objects.player import Player
from Objects.consts import MAX_ROUNDS

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
            "hand_sizes": [0, 0, 0, 0],
            "scores": [0, 0, 0, 0],
            "round_no": 0,
        }
        self.trick_end = False
        self.round_end = False
        self.game_end = False
        self.last_round_victor = None

        self.playerlist = playerlist  # 4 players always

    def deal(self):
        # empty all hands
        for idx, player in enumerate(self.playerlist):
            player.hand = []
            self.data["hand_sizes"][idx] = 0

        # deal 13 cards each to 4 players
        for _ in range(13):
            for idx, player in enumerate(self.playerlist):
                card = self.deck.deal()
                player.hand.append(card)
                self.data["hand_sizes"][idx] += 1

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

    def play(self):
        # play the game
        self.init_game()

        while not self.game_end:
            if (self.data["round_no"] >= MAX_ROUNDS):
                self.game_end = True
                continue
            print()
            print("Beginning Round", self.data["round_no"])

            for player in self.playerlist:
                player.sort_hand()
                print(player.name, ":", player.hand)

            print("---------------")
            self.play_round()
            print("Player", self.last_round_victor, "has won Round", self.data["round_no"])

            self.data["round_no"] += 1
            self.data["is_start_of_round"] = True
            self.data["round_history"].append([])

            for index, value in enumerate(self.data["hand_sizes"]):
                self.data["scores"][index] += value

            self.deck = Deck()
            self.deck.shuffle()
            self.deal()

            for idx, player in enumerate(self.playerlist):
                if "3D" in player.hand:
                    first_player = idx
            self.playerlist = self.playerlist[first_player:] + self.playerlist[:first_player]


        print("Game End")
        print("Scores:", self.data["scores"])

    def play_round(self):

        self.round_end = False

        # Might need better naming
        current_player_index = 0
        last_played_card_index = None
        ltw_index = None # ltw_index -> last trick winner index

        while not self.round_end:
            while not self.trick_end:
                if (current_player_index == last_played_card_index):
                    self.trick_end = True
                    ltw_index = last_played_card_index
                    continue

                player = self.playerlist[current_player_index]
                move = player.play(
                    self.data["is_start_of_round"],
                    self.data["play_to_beat"],
                    self.data["round_history"],
                    self.data["hand_sizes"],
                    self.data["scores"],
                    self.data["round_no"],
                )

                # Error checking moves
                if self.data["is_start_of_round"]:
                    if move == []:
                        raise NotAValidPlayError("Must play a card on round start")

                    if "3D" not in move:
                        print(move)
                        print(" ".join(player.hand))
                        raise NotAValidPlayError("Must play 3D on round start")

                # Move is registered as either pass or valid play
                if move == []:
                    print("Player", player.name, "passed")

                else:
                    for card in move:
                        player.hand.remove(card)
                        
                    print("Player", player.name, "played", " ".join(move))
                    self.data["play_to_beat"] = move
                    last_played_card_index = current_player_index

                # End current round if any play makes an empty hand
                if len(player.hand) == 0:
                    self.trick_end = True
                    self.round_end = True
                    self.last_round_victor = player.name
                    continue

                # Updating round information
                self.data["is_start_of_round"] = False
                round_no = self.data["round_no"]
                self.data["round_history"][round_no].append(move)
                self.data["hand_sizes"] = [len(player.hand) for player in self.playerlist]
                current_player_index += 1
                if current_player_index == 4:
                    current_player_index = 0

            # Perform this after a trick ends
            trick_winner = self.playerlist[last_played_card_index]
            print("Player", trick_winner.name, "has won current Trick")
            print()
            
            # Reset order of play
            self.playerlist = self.playerlist[ltw_index:] + self.playerlist[:ltw_index]
            self.trick_end = False

            # Reset trick information
            current_player_index = 0
            last_played_card_index = None
            self.data["play_to_beat"] = []



if __name__ == "__main__":
    # test
    player1 = Player("A")
    player2 = Player("B")
    player3 = Player("C")
    player4 = Player("D")

    playerlist = [player1, player2, player3, player4]

    game = Game(playerlist)
    game.play()
