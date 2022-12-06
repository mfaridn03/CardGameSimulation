from Objects.utils import sort_hand
from typing import Optional, List


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.order = -1

    def sort_hand(self) -> None:
        # Sort the cards in the hand
        # Suit order: D C H S
        # Rank order: 3 4 5 6 7 8 9 10 J Q K A 2
        sort_hand(self.hand)

    def play(self, data: dict) -> Optional[List]:
        pass
    
    def choose_play_direction(self, data: dict) -> bool:
        """
        The 2nd last player must choose whether play is clockwise or counter-clockwise
        
        result of True means keep default direction
        result of False means change to opposite direction
        """
        return True
