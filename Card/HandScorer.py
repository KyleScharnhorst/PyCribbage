from Card import *

# This class encapsulates scoring functionality.
class HandScorer(object):
    score = 0
    
    # Scores a hand for a flush
    # Returns the score value. 4/5 if flush or 0 for no flush.
    def score_flush(self):
        if self.isValid():
            suite_list = list([0] * CardSuite.__len__())
            for card in self.card_hand:
                suite_list[card.suite.value] += 1
            for suite in range(len(suite_list)):
                if suite_list[suite] == 4 and suite != 0:
                    isCCardSameSuite = self.cut_card.suite.value == suite
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
        if self.isValid():
            score = 0
            for ctype in range(len(self.type_list)):
                if self.type_list[ctype] > 1:
                    # Have at least a pair, score
                    if self.type_list[ctype] == 2:
                        print("Pair for 2.")
                        score += 2
                    elif self.type_list[ctype] == 3:
                        print("Three of a kind for 6.")
                        score += 6
                    elif self.type_list[ctype] == 4:
                        print("Four of a kind for 12.")
                        score += 12
                    else:
                        print("Error: Card count was far too large.")
                        return 0
            return score;
        else:
            print("Unexpecred multiples result, returning score of 0.")
        return 0

    #def score_runs(self):
    #	if self.isValid():
    #		score = 0
    #		raise NotImplementedError
    
    #def score_fifteens(self):
    #	raise NotImplementedError

    ## Checks the hand for jacks of the same suit as the cut card.
    #def score_nobs(self):
    #	if self.isValid():
    #		raise NotImplementedError