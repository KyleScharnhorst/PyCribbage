from Card.CardHand import *
from itertools import combinations

# This class encapsulates scoring functionality.
class HandScorer(object):
    score = 0
    hand = None

    def __init__(self, a_card_hand):
        self.hand = a_card_hand

    # Scores this hand of cribbage
    def score_hand(self):
        self.score = 0
        # Score knobs
        self.score += self.score_nobs()
        # Score multiples (pairs, three of a kind, four of a kind)
        self.score += self.score_multiples()
        #Score runs - min of three cards
        self.score += self.score_runs()
        # Score flush - is this a crib hand?  (only if cut card doesn't match a
        # hand that is a flush)
        self.score += self.score_flush()
        # Score fifteens
        #self.score += self.score_fifteens()
    
    # Scores a hand for a flush
    # Returns the score value. 4/5 if flush or 0 for no flush.
    def score_flush(self):
        if self.hand.isValid():
            suite_list = list([0] * CardSuite.__len__())
            for card in self.hand.card_hand:
                suite_list[card.suite.value] += 1
            for suite in range(len(suite_list)):
                if suite_list[suite] == 4 and suite != 0:
                    isCCardSameSuite = self.hand.cut_card.suite.value == suite
                    if isCCardSameSuite:
                        print("5 points from flush.")
                        return 5;
                    else:
                        # Have hand flush and cut card is not same, determine if crib
                        while 1:
                            user_input = input("Is this hand the crib? (y/n): ").lower()
                            if user_input.startswith("y"):
                                return 0;
                            elif user_input.startswith("n"):
                                print("4 points from flush.")
                                return 4;
        else:
            print("Unexpected flush result, returning score of 0.")		
        return 0;

    # Scores a hand for multiples (pairs, three of a kind, four of a kind)
    # Returns the score from multiples or zero if no score.
    def score_multiples(self):
        if self.hand.isValid():
            score = 0
            for ctype in range(len(self.hand.type_list)):
                if self.hand.type_list[ctype] > 1:
                    # Have at least a pair, score
                    if self.hand.type_list[ctype] == 2:
                        print("Pair for 2.")
                        score += 2
                    elif self.hand.type_list[ctype] == 3:
                        print("Three of a kind for 6.")
                        score += 6
                    elif self.hand.type_list[ctype] == 4:
                        print("Four of a kind for 12.")
                        score += 12
                    else:
                        print("Error: Card count was far too large.")
                        return 0
            return score;
        else:
            print("Unexpecred multiples result, returning score of 0.")
        return 0

    def score_runs(self):
        score = 0
        if self.hand.isValid():
            start_of_run = 0
            consecutive_count = 0
            # Traverse over all card buckets
            for ctype in range(len(self.hand.type_list)):
                # If we have a card start prepping for a run
                if self.hand.type_list[ctype] > 0:
                    # If we are not already in a run start
                    if consecutive_count == 0:
                        start_of_run = ctype
                    # Increment run count
                    consecutive_count += 1
                # else did we reach a run count (3)?  
                elif consecutive_count >= 3:
                    # score the run
                    score = consecutive_count
                    run_index = start_of_run
                    # Go through run multiply score if greater than 1
                    while run_index < consecutive_count+start_of_run:
                        card_count = self.hand.type_list[run_index]
                        if card_count > 1:
                            score *= card_count
                        run_index += 1
                    break # no more runs can be encountered.
                # a run was not encounterd, reset vars.
                else:
                    start_of_run = 0
                    consecutive_count = 0
        if score > 0:
            print("Score from run: {}".format(score))
        return score

    # Prints the output for a tuple that scored fifteen.
    def print_scoring_fifteen(tuple, score):
        print_str = ""
        for card in tuple:
            print_str += card.toString() + ", "
        print_str += " for fifteen {}.".format(score)
        print(print_str)

    # This functions scores the hand for combinations of 15. 
    def score_fifteens(self):
        score = 0
        if self.hand.isValid():
            cards = self.hand.card_hand.copy()
            cards.append(self.hand.cut_card)
            for i in range(2,4):
                card_combos = combinations(cards, i)
                # for each tuple, see if their total adds to 15
                for card_tuple in card_combos:
                    tuple_value = 0
                    for card in card_tuple:
                        tuple_value += card.value
                    if tuple_value == 15:
                        score += 2
                        HandScorer.print_scoring_fifteen(card_tuple, score)                  
        return score

    # Checks the hand for jacks of the same suit as the cut card.
    def score_nobs(self):
        if self.hand.isValid():
            for card in self.hand.card_hand:
                if card.card_type == CardType.jack and card.suite == self.hand.cut_card.suite:
                    print("1 point for his nobs.")
                    return 1
        return 0


