import unittest
from unittest.mock import patch
from Cribbage import *
from Card.CardType import CardType
from Card.CardSuite import CardSuite

class Test_HandScorer(unittest.TestCase):
    
    # Using unittest.mock.patch to mock user input for determining if crib hand.
    @patch('Card.HandScorer.get_is_crib_input', return_value=True)
    def test_score_flush_crib_hand(self, mock_method):
        cut_card = None
        cut_card = handle_cut_card("ccard 6s", cut_card)
        self.assertEquals(handle_score("score as,qs,10s,ks", cut_card), 5)
        # Crib Hand (Must have all 5 cards of the same suit to be a flush).
        cut_card = handle_cut_card("ccard 6d", cut_card)
        self.assertEquals(handle_score("score as,qs,10s,ks", cut_card), 0)

    # Using unittest.mock.patch to mock user input for determining if crib hand.
    @patch('Card.HandScorer.get_is_crib_input', return_value=False)
    def test_score_flush_non_crib(self, mock_method):
        cut_card = None
        cut_card = handle_cut_card("ccard 6s", cut_card)
        self.assertEquals(handle_score("score as,qs,10s,ks", cut_card), 5)
        # Non-Crib Hand
        cut_card = handle_cut_card("ccard 6d", cut_card)
        self.assertEquals(handle_score("score as,qs,10s,ks", cut_card), 4)
        # Other non-flush hands
        cut_card = handle_cut_card("ccard 6s", cut_card)
        self.assertEquals(handle_score("score as,qs,10s,kd", cut_card), 0)
        cut_card = handle_cut_card("ccard 6s", cut_card)
        self.assertEquals(handle_score("score as,qs,10d,kd", cut_card), 0)
        cut_card = handle_cut_card("ccard 6s", cut_card)
        self.assertEquals(handle_score("score as,qd,10d,kd", cut_card), 0)
        cut_card = handle_cut_card("ccard 6d", cut_card)
        self.assertEquals(handle_score("score as,qd,10d,kd", cut_card), 0)
    
    def test_score_multiples(self):
        cut_card = None
        # Four of a kind
        cut_card = handle_cut_card("ccard 2h", cut_card)
        self.assertEquals(handle_score("score 2s,2c,2d,ad", cut_card), 12)
        # Four of a kind
        cut_card = handle_cut_card("ccard ah", cut_card)
        self.assertEquals(handle_score("score ks,kc,kd,kh", cut_card), 12)
        # Full House
        cut_card = handle_cut_card("ccard ah", cut_card)
        self.assertEquals(handle_score("score ks,kc,kd,as", cut_card), 8)
        # Three of a kind
        cut_card = handle_cut_card("ccard js", cut_card)
        self.assertEquals(handle_score("score jd,qc,kd,jh", cut_card), 15)
        # Two pair
        cut_card = handle_cut_card("ccard js", cut_card)
        self.assertEquals(handle_score("score jd,qc,kd,kh", cut_card), 16)
        # Pair
        cut_card = handle_cut_card("ccard 6s", cut_card)
        self.assertEquals(handle_score("score ad,qc,6d,kh", cut_card), 2)
        # No Pairs
        cut_card = handle_cut_card("ccard 6s", cut_card)
        self.assertEquals(handle_score("score ad,qc,10d,kh", cut_card), 0)

    
    def test_score_runs(self):
        cut_card = None
        cut_card = handle_cut_card("ccard ah", cut_card)
        self.assertEquals(handle_score("score as,ac,2s,3d", cut_card), 15)
        cut_card = handle_cut_card("ccard ah", cut_card)
        self.assertEquals(handle_score("score as,2c,2s,3d", cut_card), 16)
        cut_card = handle_cut_card("ccard ah", cut_card)
        self.assertEquals(handle_score("score as,2c,3s,4d", cut_card), 10)
        cut_card = handle_cut_card("ccard ah", cut_card)
        self.assertEquals(handle_score("score 2s,3c,4s,5d", cut_card), 7)
        cut_card = handle_cut_card("ccard ah", cut_card)
        self.assertEquals(handle_score("score 2s,3c,8s,6d", cut_card), 5)
    
    def test_score_fifteens(self):
        hand = CardHand([
            Card(CardType.five, 5, CardSuite.spade),
            Card(CardType.five, 5, CardSuite.diamond),
            Card(CardType.five, 5, CardSuite.heart),
            Card(CardType.jack, 10, CardSuite.spade)
            ], Card(CardType.five, 5, CardSuite.spade))# cut card

        hand_scorer = HandScorer(hand)
        score = hand_scorer.score_fifteens()
        self.assertEqual(score, 16)

        cut_card = None
        cut_card = handle_cut_card("ccard 3h", cut_card)
        self.assertEquals(handle_score("score 3s,3c,2s,4d", cut_card), 17)

    def test_basic_score(self):
        cut_card = None
        cut_card = handle_cut_card("ccard js", cut_card)
        self.assertEquals(handle_score("score jh,jd,jc,7c", cut_card), 12)

    def test_score_nobs(self):
        cut_card = None
        cut_card = handle_cut_card("ccard 4c", cut_card)
        self.assertEquals(handle_score("score 2h,kd,7c,jc", cut_card), 1)
        cut_card = handle_cut_card("ccard qs", cut_card)
        self.assertEquals(handle_score("score js,ad,4c,8s", cut_card), 5)
        cut_card = handle_cut_card("ccard ad", cut_card)
        self.assertEquals(handle_score("score qh,jd,9c,7c", cut_card), 1)
        cut_card = handle_cut_card("ccard 10h", cut_card)
        self.assertEquals(handle_score("score 6h,8s,jh,4c", cut_card), 1)
        cut_card = handle_cut_card("ccard 10h", cut_card)
        self.assertEquals(handle_score("score 2c,4d,6s,8h", cut_card), 0)

if __name__ == '__main__':
    unittest.main()