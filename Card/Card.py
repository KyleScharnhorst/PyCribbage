from Card.CardType import *
from Card.CardSuite import *
from Misc.Utils import *

# Card object encapsulates card related data and functionality.
class Card(object):
    card_type = CardType.no_type;
    value = 0; # necessary because jack, queen, king are actually equal to 10.
    suite = CardSuite.no_type;

    # Initializer
    def __init__(self, card_type, value, suite):
        self.card_type = card_type;
        self.value = value;
        self.suite = suite;

    # Determines if this card is valid for processing
    # True if valid, false otherwise
    def is_valid(self):
        if self.card_type == CardType.no_type:
            return False;
        if self.value == 0:
            return False;
        if self.suite == CardSuite.no_type:
            return False;
        # object is valid		
        return True;

    # Creates a card object using a card string
    # E.g., qs
    def create_card(card_str):
        card_str = card_str.strip()
        #get suite
        suite = CardSuite.get_suite(card_str);
        Debug.Print("suite value: ", suite);
        #get card type and value
        card_type = CardType.get_card_type(card_str)
        Debug.Print("card type: ", card_type)
        card_val = card_type.get_card_value()
        Debug.Print("card value: ", card_val)
        #call card initializer and return
        return Card(card_type, card_val, suite)

    def toShortString(self):
        result = ""
        if self.card_type.value < 11:
            result += str(self.card_type.value)
        else:
            result += self.card_type.name[0]
        result += self.suite.name[0]
        return result

    # Returns a string representation of this object
    def toString(self):
        return self.card_type.name + " of " + self.suite.name