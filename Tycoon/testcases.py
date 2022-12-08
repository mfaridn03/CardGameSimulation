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

    def test_get_card_score(self):
        """
        Testing the get_card_score function
        """
        card_list = ["KS"]
        self.assertEqual(get_card_score(card_list), 10)

        card_list = ["ZR"]
        self.assertEqual(get_card_score(card_list), 13)

        card_list = ["ZR"]
        self.assertEqual(get_card_score(card_list, is_rev=True), 13)

        card_list = ["3S"]
        self.assertEqual(get_card_score(card_list), 0)

        card_list = ["3S"]
        self.assertEqual(get_card_score(card_list, is_rev=True), 12)

    def test_get_pair_score(self):
        """
        Testing the get_pair_score function
        """
        card_list = ["KS", "KD"]
        self.assertEqual(get_pair_score(card_list), 10)

        card_list = ["ZB", "KD"]
        self.assertEqual(get_pair_score(card_list), 10)

        card_list = ["ZR", "ZB"]
        self.assertEqual(get_pair_score(card_list), 13)

        card_list = ["ZR", "ZB"]
        self.assertEqual(get_pair_score(card_list, is_rev=True), 13)

        card_list = ["3S", "3H"]
        self.assertEqual(get_pair_score(card_list), 0)

        card_list = ["3S", "ZR"]
        self.assertEqual(get_pair_score(card_list, is_rev=True), 12)
        
    def test_is_higher_play(self):
        """
        Testing the is_higher_play function
        """
        is_this_higher = ["3S"]
        than_this = [JOKER_BLACK]
        
        self.assertTrue(is_higher_play(is_this_higher, than_this, is_rev=False))
        
        than_this = [JOKER_RED]
        self.assertTrue(is_higher_play(is_this_higher, than_this, is_rev=False))

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
