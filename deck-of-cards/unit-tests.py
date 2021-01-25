from cards import Card
from cards import Deck
import unittest

class CardTest(unittest.TestCase):
	def setUp(self):
		self.card=Card('Hearts', '5')

	def test_init(self):
		self.assertEqual(self.card.suit, 'Hearts')
		self.assertEqual(self.card.value, '5')

	def test_repr(self):
		self.assertEqual(self.card.__repr__(), '5 of Hearts')

class DeckTest(unittest.TestCase):

	def setUp(self):
		self.deck=Deck()

	def test_first_card_after_shuffle(self):
		self.deck.shuffle()
		first_card=self.deck.full_deck[0]
		self.assertEqual(self.deck.first_card(), first_card)

	def test_last_two_card(self):
		last_cards=self.deck.full_deck[-2:][::-1]
		self.assertEqual(self.deck.deal_hand(2), last_cards)

	def test_last_two_card_after_shuffle(self):
		self.deck.shuffle()
		last_cards=self.deck.full_deck[-2:][::-1]
		self.assertEqual(self.deck.deal_hand(2), last_cards)

	def test_first_card(self):
		first_card=self.deck.full_deck[0]
		self.assertEqual(self.deck.first_card(), first_card)

	def 



	def test_full_length(self):
		self.assertEqual(self.deck.count(), 52)

	def test_deal_hand(self):
		self.assertEqual(len(self.deck.deal_hand(10)), 10)

	# def test_deal_card(self):
	# 	self.assertEqual()

	def test_lenght_deal_card(self):
		self.deck.deal_card()
		self.assertEqual(self.deck.count(), 51)

	def test_length_deal_hand(self):
		self.deck.deal_hand(10)
		self.assertEqual(self.deck.count(), 42)

	def test_shuffle_lenth(self):
		self.deck.shuffle()
		self.assertEqual(self.deck.count(), 52)

	def test_not_full_deck_shuffle(self):
		self.deck.deal_hand(10)
		with self.assertRaises(ValueError):
			self.deck.shuffle()




if __name__=='__main__':
	unittest.main()