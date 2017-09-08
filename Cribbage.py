# This script is designed to score a hand in cribbage.
# It should be used as such:
# The python script will be ran from the command line, like: python3.5 cribbage.py
# The cut card must be set so that a hand can be scored. like: ccard qh
# The cut card would now be the queen of Hearts.
# A hand can now be scored using the 'score' command:
# score as,3h,10c,jd
# where the hand would be: ace of Spades, 3 of Hearts, 10 of Clubs, and a jack of Diamonds.

# Some personal notes:
# - It would be nice to set the flop once for a round. If many people are having their hands scored
#   then it would be nice to not have to input the cut card every time.
# - The app could then be a command line application where it runs and inputs are interpretted.
# - Types of input:
#   ccard [cut card] - displays current cut card or if a card is provided, sets the
#   score <comma delimited hand> - scores a particular hand using the inputted cut card.
#   help - displays usage.
#   quit - exits the application.
# - Any unrecognized input will display the usage.

import sys
from Card.Card import Card
from Card.CardHand import CardHand
from Card.HandScorer import HandScorer
from Misc.OutputScore import *
from Misc.Utils import *
from Misc.PrintCribbage import *

#CONSTANTS
CUT_CARD = "ccard"
QUIT = "quit"
HELP = "help"
SCORE = "score"
INPUT_STR = ">>>"
DEBUG_PARAM_STR = "--debug"

#TESTING
TESTING = False

def handle_cut_card(cut_card_input, cut_card):
    """Handles user input to view and set the cut card
    E.g., ccard jh"""
    Debug.Print("Handling cut card...")
    cut_card_partition = cut_card_input.rpartition(" ")
    cut_card_input = cut_card_partition[2]
    if len(cut_card_input) > 0 and len(cut_card_partition[0]) > 0:
        Debug.Print(cut_card_input)
        new_cut_card = Card.create_card(cut_card_input)
        if new_cut_card.is_valid():
            Debug.Print("Changing cut card...")
            if cut_card != None:
                Debug.Print("Old cut card:\n", cut_card.toString())
            cut_card = new_cut_card
            print("New cut card:\n", cut_card.toString())
        else:
            print("Cut card input is invalid: ", cut_card_input)
    elif cut_card is None:
        print("There is no current cut card.")
    else:
        print("The current cut card: ", cut_card.toString())
    return cut_card

def handle_score(score_input, cut_card):
    """Handles user input to score a cribbage hand
    E.g., score as,2c,3d,4h"""
    if cut_card is None:
        print("Cut card has not been set. See help for usage details.")
        return None
    # Parse hand
    hand = CardHand.create_hand(score_input.rpartition(" ")[2], cut_card)
    # Check hand
    if hand.isValid():
        print("Scoring hand...")
        scorer = HandScorer(hand)
        scorer.score_hand()
        print("Total score: ", scorer.score)
        if not TESTING:
            OutputScore.Output(hand, scorer.score)
        return scorer.score

def assign_debug(bool_val):
    """encapsulates setting testing and debug"""
    global TESTING
    TESTING = bool_val
    Debug.set_debugging(bool_val)

def param_exists(arg_str):
    """Checks command line args for existence of an argument"""
    for arg in sys.argv:
        if arg_str.lower() == arg.lower():
            return True
    return False

def handle_params():
    """Called by main to handle command line arguments passed in by user."""
    if len(sys.argv) > 1:
        # Check for debug command line param.
        assign_debug(param_exists(DEBUG_PARAM_STR))

def main():
    """Main loop for application, continually asks for and handles input."""
    cut_card = None
    print_usage()
    print_examples()
    handle_params()
    while 1:
        user_input = input(INPUT_STR).lower()
        if user_input.startswith("q"):
            print("Exiting the application.")
            exit(0)
        elif user_input.startswith("c"):
            cut_card = handle_cut_card(user_input, cut_card)
        elif user_input.startswith("h"):
            print_usage()
            print_examples()
        elif user_input.startswith("s"):
            handle_score(user_input, cut_card)

if __name__ == "__main__":
    assign_debug(False)
    main()
