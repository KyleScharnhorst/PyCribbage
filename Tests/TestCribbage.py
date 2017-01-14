from ..Source.Cribbage import *
import unittest


card_type_test_types = list(
    [("z", CardType.no_type),
    ("a", CardType.ace),
    ("1", CardType.ace),
    ("2", CardType.two),
    ("3", CardType.three),
    ("4", CardType.four),
    ("5", CardType.five),
    ("6", CardType.six),
    ("7", CardType.seven),
    ("8", CardType.eight),
    ("9", CardType.nine),
    ("10", CardType.ten),
    ("j", CardType.jack),
    ("11", CardType.jack),
    ("q", CardType.queen),
    ("12", CardType.queen),
    ("k", CardType.king),
    ("13", CardType.king)]
);

card_suite_test_types = list(
    [("x", CardSuite.no_type),
    ("s", CardSuite.spade),
    ("c", CardSuite.club),
    ("d", CardSuite.diamond),
    ("h", CardSuite.heart)]
);

# Generated by helper function. Contains all card type test 
# types combined with all card suite test types.
card_test_list = None

def generate_card_test_list():
    global card_test_list
    card_test_list = list()
    for card_type in card_type_test_types:
        for card_suite in card_suite_test_types:
            card_test_list.append( (card_type[0]+card_suite[0], 
                                    Card(card_type[1], card_type[1].get_card_value(), card_suite[1]) ) 
                                 )

class Test_atoi(unittest.TestCase):
    
    def test_atoi(self):
        self.assertEqual(atoi("asd"), 0)
        self.assertEqual(atoi("10c"), 10)
        self.assertEqual(atoi("11c1"), 11)
        self.assertEqual(atoi("765"), 765)
        
class Test_CardType(unittest.TestCase):
    
    def test_get_card_type(self):
        for card_test_case in card_test_list:
            self.assertEqual(CardType.get_card_type(card_test_case[0]), card_test_case[1].card_type)
            
    def test_get_card_value(self):
        for card_type in CardType.get_list():
            if card_type.value < 10:
                self.assertEqual(card_type.get_card_value(), card_type.value)
            else:
                self.assertEqual(card_type.get_card_value(), 10)
                
class Test_CardSuite(unittest.TestCase):
    
    def test_get_suite(self):
        for card_test_case in card_test_list:
            self.assertEqual(CardSuite.get_suite(card_test_case[0]), card_test_case[1].suite)
            
class Test_Card(unittest.TestCase):
    invalid_cards = list(
        [Card(CardType.no_type, 1, CardSuite.diamond),
         Card(CardType.ace, 0, CardSuite.diamond),
         Card(CardType.ace, 1, CardSuite.no_type)]
    );
    
    def test_is_valid_invalid_cards(self):
        for invalid_card in self.invalid_cards:
            self.assertFalse(invalid_card.is_valid())
            
    def test_create_card(self):
        for card_test in card_test_list:
            card = Card.create_card(card_test[0]);
            if card_test[1].card_type != CardType.no_type and card_test[1].suite != CardSuite.no_type:
                self.assertTrue(card.is_valid())
            else:
                self.assertFalse(card.is_valid())
            # Ensure type is correct
            self.assertEqual(card.card_type, card_test[1].card_type)
            # Ensure value is correct
            self.assertEqual(card.value, card_test[1].value)
            # Ensure suite is correct
            self.assertEqual(card.suite, card_test[1].suite)
    
#class Test_CardHand(unittest.TestCase):
    
#    def test_create_hand(self):
#        raise NotImplementedError
    
#    def test_score_flush(self):
#        raise NotImplementedError 
    
#    def test_score_multiples(self):
#        raise NotImplementedError   
    
#    def test_score_runs(self):
#        raise NotImplementedError
    
#    def test_score_fifteens(self):
#        raise NotImplementedError
    
#    def test_isValid(self):
#        raise NotImplementedError

if __name__ == '__main__':
    generate_card_test_list()
    unittest.main()