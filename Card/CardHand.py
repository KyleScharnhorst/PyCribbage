from Card.Card import *

# This class encapsulates all functionality applied to a cribbage hand
class CardHand(object):
    card_hand = None
    cut_card = None
    validity_checked = False
    validity = False
    type_list = None

    # Initializer
    def __init__(self, card_hand, cut_card):
        self.card_hand = card_hand
        self.cut_card = cut_card
        self.init_type_list()
        self.isValid()

    # Initializes a bucket list used for scoring multiples and pairs
    def init_type_list(self):
            self.type_list = list([0] * CardType.__len__())
            for card in self.card_hand:
                self.type_list[card.card_type.value] += 1
            # Add cut card card into type list to check multiples
            self.type_list[self.cut_card.card_type.value] += 1

    # Takes a string like 1s,jh,3c,6d and builds and returns a hand object.
    def create_hand(hand_str, cut_card):
        if hand_str != None and len(hand_str) > 0:
            hand_str = hand_str.split(",")
            if len(hand_str) != 4:
                print("Card hand does not have enough cards.")
                return CardHand()
            else:
                card_hand = list()
                for card in hand_str:
                    card_hand.append(Card.create_card(card))
                return CardHand(card_hand, cut_card)
        else: 
            print("Scoring hand is invalid.")
            return CardHand()
                 
    # Determines if the hand is valid for processing
    def isValid(self):
        if self.validity_checked:
            return self.validity;
        else:
            self.validity_checked = True;
            if self.card_hand == None:
                print("Error: Card Hand has no cards.")
                self.validity = False;
                return validity;
            elif self.cut_card == None:
                print("Error: Card Hand has no cut card.")
                self.validity = False;
                return self.validity;
            elif len(self.card_hand) != 4:
                print("Error: Hand has more than 4 cards.")
                self.validity = False;
                return self.validity;
            elif self.type_list == None:
                print("Error: Type list is not initialized.")
                self.validity = False;
                return self.validity;
            else:
                self.validity = True;
                return self.validity;