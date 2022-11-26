import unittest

from Objects.utils import *
from Objects.deck import *

class TestDeck(unittest.TestCase):
    def test_is_triple(self):
        """
        Testing the is_triple function
        """
        card_list = ["KS", "KH", "KD"]
        self.assertTrue(is_triple(card_list))

        card_list = ["ZR", "KH", "KD"]
        self.assertTrue(is_triple(card_list))

        card_list = ["ZR", "ZB", "KD"]
        self.assertTrue(is_triple(card_list))

        card_list = ["ZR", "AS", "KD"]
        self.assertFalse(is_triple(card_list))

    def test_deck_shuffle(self):
        """
        Testing the shuffle function
        """
        deck = Deck()
        # print(deck)
        self.assertEqual(len(deck.cards), 54)

        # copy deck into deck2
        deck2 = Deck()
        deck2.cards = deck.cards.copy()
        deck2.shuffle()
        self.assertNotEqual(deck.cards, deck2.cards)

    def test_deck_sort(self):
        """
        Check sorting functionality
        """
        original_deck = Deck()
        new_deck = Deck()

        # shuffle
        new_deck.shuffle()
        self.assertNotEqual(original_deck.cards, new_deck.cards)

        # sort
        sort_hand(new_deck.cards)
        self.assertEqual(original_deck.cards, new_deck.cards)

if __name__ == "__main__":
    unittest.main()
