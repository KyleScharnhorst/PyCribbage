import json
from Cribbage import CardHand

# This class contains functionality for outputting 
# the scoring of cribbage hands to an output file.
# Can be useful for reviewing past hands and creating
# human verified test data.
# Example JSON output
# {"hand":["js","jh","jd","jc"],"cut_card":"ah","score":13}
class OutputScore(object):
    OUT_FILE_NAME = "OutputScores.txt"
    HAND_STR = "hand"
    CUT_CARD_STR = "cut_card"
    SCORE_STR = "score"
    
    def Output(hand, score):
        with open(OutputScore.OUT_FILE_NAME, "a") as out_file:
            data = {}
            # create card list that can be serialized
            serializable_hand = list()
            for card in hand.card_hand:
                serializable_hand.append(card.toShortString())
            data[OutputScore.HAND_STR] = serializable_hand
            data[OutputScore.CUT_CARD_STR] = hand.cut_card.toShortString()
            data[OutputScore.SCORE_STR] = score
            json_result = json.dump(data, out_file)
            out_file.write("\n")

