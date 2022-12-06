# Setting up a deck of cards
from Objects.exceptions import *
from Objects.utils import *
from Objects.deck import Deck
from Objects.player import Player
from Objects.consts import MAX_ROUNDS

import random
import typing


class Game:
    def __init__(self, playerlist: typing.List[Player]):
        if len(playerlist) < 3 or len(playerlist) > 54:
            raise NotEnoughPlayersError("Require 2-54 players for a valid game")
        
        namelist = [p.name for p in playerlist]
        if len(set(namelist)) < len(playerlist):
            raise DuplicatePlayerNamesError("Can't have duplicate player names")
        
        self.num_players = len(playerlist)
        self.deck = Deck()
        self.data = {
            "playerlist": [],           # Contains names, current order
            "playerlist_orig": [],      # Contains names, original order
            
            "is_start_of_round": True,
            "is_start_of_game": True,
            "play_to_beat": [],
            "round_history": [[]],      # First inner lists are per round, second inner lists are per trick, within trick lists are tuples containing player name and card played
            "round_end_history": [[]],  # First inner lists are per round, containing info from self.end_of_round_order
            "hand_sizes": [],
            "scores": [],               # Score array reflects player order in player_list_original
            "score_history": [],      # Each inner list corresponds to player in playerlist_orig
            "round_no": 0,
            "trick_no": 0,
            "is_rev": False,
        }
        self.trick_end = False
        self.round_end = False
        self.game_end = False
        
        self.data["hand_sizes"] = [0] * self.num_players
        self.data["scores"]     = [0] * self.num_players
        
        self.playerlist = []                # Contains names, current order
        self.playerlist_orig = []           # Contains names, original order
        self.playerobjects = playerlist    # Contains player objects, original order

        self.end_of_round_order = []    # 0th index means tycoon, last index means beggar

    def deal(self):
        # Reset and shuffle the deck
        self.deck.reset()
        self.deck.shuffle()
        
        # Empty all hands
        for idx, player in enumerate(self.playerobjects):
            player.hand = []
            self.data["hand_sizes"][idx] = 0

        # Randomise starting player
        offset = random.randint(0, self.num_players - 1)

        # Deal cards to each player until deck is empty; deck size is fixed at 54
        for i in range(54):
            card = self.deck.deal()
            curr_player = (i + offset) % self.num_players
            self.playerobjects[curr_player].hand.append(card)
            self.data["hand_sizes"][curr_player] += 1

    def init_game(self): 
        self.deal()
        # Player that has 3D will start the game
        other_player_names = []
        firstplayer = None

        for player in self.playerobjects:
            if "3D" in player.hand:
                firstplayer = player
            else:
                other_player_names.append(player.name)

        # Randomise the order of the other players
        random.shuffle(other_player_names)
        self.playerlist = [firstplayer.name] + other_player_names
        self.data["playerlist"] = [name for name in self.playerlist]
        
        # Store original player order
        self.playerlist_orig = [name for name in self.playerlist]
        self.data["playerlist_orig"] = [name for name in self.playerlist_orig]
        
        # Resetting all game data
        self.data = {
            "is_start_of_round": True,
            "is_start_of_game": True,
            "play_to_beat": [],
            "round_history": [[]],
            "hand_sizes": [],
            "scores": [],
            "round_no": 0,
            "trick_no": 0,
            "is_rev": False,
        }
        self.trick_end = False
        self.round_end = False
        self.game_end = False
        self.data["hand_sizes"] = [0] * self.num_players
        self.data["scores"]     = [0] * self.num_players

    def play_text_based(self):
        self.init_game()
        print("Game Starting")

        while not self.game_end:
            if (self.data["round_no"] >= MAX_ROUNDS):
                self.game_end = True
                continue

            # Commence round
            self.print_start_of_round_info()
            self.play_round()
            
            # Round has ended, give scores and print winner info
            self.score_players()
            print("Player", self.end_of_round_order[0], "has won Round", self.data["round_no"])

            # Reset data at round end
            self.data["round_no"] += 1
            self.data["trick_no"] = 0
            self.data["is_start_of_round"] = True
            self.data["play_to_beat"] = []
            self.data["round_history"].append([])
            self.data["is_rev"] = False

            self.deal()

            # Setup next round player order
            self.reset_player_order()

        # Game has ended, print game status and final scores
        print("Game End")
        print("Scores:", self.data["scores"])
        pass
    
    def print_start_of_round_info(self):
        """
        Print start of round info including round number and player hands
        """
        print("\nBeginning Round", self.data["round_no"])
        print("Player hands are:")
        for name in self.playerlist:
            idx = self.playerlist_orig.index(name)
            playerobj = self.playerobjects[idx]
            playerobj.sort_hand()
            print(playerobj.name, ":", playerobj.hand)
        print("-----------------")
        pass
    
    def score_players(self):
        """
        Players are given scores for a round based on the following rules:
        First place       - 20 points
        Second place      - 15 points
        Second last place - 5 points
        Last place        - 0 points
        Other places      - 10 points
        
        Since player counts of less than 4 do not allow for this division of scoring,
        only first place and last place are considered as special cases
        """
        this_round_scores = [0] * self.num_players
        if self.num_players <= 3:
            # Fuck you, why would you do this
            for playername in self.playerlist_orig:
                idx = self.end_of_round_order.index(playername)
                score = 10
                if idx == 0:                      score = 20
                elif idx == self.num_players - 1: score = 0
                
                this_round_scores[idx] += score
                self.data["scores"][idx] += score
        else:
            for playername in self.playerlist_orig:
                idx = self.end_of_round_order.index(playername)
                score = 10
                if idx == 0:                      score = 20
                elif idx == 1:                    score = 15
                elif idx == self.num_players - 2: score = 5
                elif idx == self.num_players - 1: score = 0
                
                this_round_scores[idx] += score
                self.data["scores"][idx] += score
        self.data["score_history"].append(this_round_scores)
        pass
                
    def reset_player_order(self):
        """
        Player order is reset for a new round, keeping players in their original seating
        2nd last place of previous round decides whether play is clockwise or anticlockwise
        Last place of previous round is first player in current round
        """
        loser = self.end_of_round_order[-1]
        second_loser = self.end_of_round_order[-2]
        sl_idx = self.playerlist_orig.index(second_loser)
        clockwise = self.playerobjects[sl_idx].choose_play_direction(self.data)
        
        # Reverse player order if 2nd loser chooses anticlockwise
        self.playerlist = self.playerlist_orig
        if not clockwise:
            self.playerlist.reverse()
        
        # Rearrange playerlist to start with loser 
        first_idx = self.playerlist_orig.index(loser)
        self.playerlist = self.playerlist[first_idx:] + self.playerlist[:first_idx]
        self.data["playerlist"] = [name for name in self.playerlist]
        pass

    def play_round(self):
        
        # Resetting variables
        self.round_end = False
        current_player_index = 0        # Index of current player
        last_played_card_index = None   # Index of the player who last played a card (not pass)
        ltw_index = None                # ltw_index -> last trick winner index

        while not self.round_end:
            while not self.trick_end:
                
                # Check if trick should end
                if (current_player_index == last_played_card_index \
                    or is_eight_stop(self.data["play_to_beat"])
                    or):           
                    pass 
                
                # Current player makes a move
                player = self.playerlist[current_player_index]
                move = player.play(self.data)

                # Error checking moves
                if self.data["is_start_of_round"]:
                    if move == []:
                        raise InvalidMoveError("Must play a card on round start")

                    if "3D" not in move:
                        print(move)
                        print(" ".join(player.hand))
                        raise InvalidMoveError("Must play 3D on round start")

                # Move is registered as either pass or valid play
                if move == []:
                    print("Player", player.name, "passed")

                else:
                    for card in move:
                        player.hand.remove(card)
                        
                    print("Player", player.name, "played", " ".join(move))
                    self.data["play_to_beat"] = move
                    last_played_card_index = current_player_index

                # # End current round if any play makes an empty hand
                # if len(player.hand) == 0:
                #     self.trick_end = True
                #     self.round_end = True
                #     self.last_round_victor = player.name
                #     continue

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
        pass



if __name__ == "__main__":
    player1 = Player("A")
    player2 = Player("B")
    player3 = Player("C")
    player4 = Player("D")

    playerlist = [player1, player2, player3, player4]
    
    game = Game(playerlist)
    game.init_game()
    game.play_text_based()
    
    pass