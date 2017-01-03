import cribbage
import unittest

card_type_test_types = list(
    [("z", cribbage.CardType.no_type),
    ("a", cribbage.CardType.ace),
    ("1", cribbage.CardType.ace),
    ("2", cribbage.CardType.two),
    ("3", cribbage.CardType.three),
    ("4", cribbage.CardType.four),
    ("5", cribbage.CardType.five),
    ("6", cribbage.CardType.six),
    ("7", cribbage.CardType.seven),
    ("8", cribbage.CardType.eight),
    ("9", cribbage.CardType.nine),
    ("10", cribbage.CardType.ten),
    ("j", cribbage.CardType.jack),
    ("11", cribbage.CardType.jack),
    ("q", cribbage.CardType.queen),
    ("12", cribbage.CardType.queen),
    ("k", cribbage.CardType.king),
    ("13", cribbage.CardType.king)]
);

card_suite_test_types = list(
    [("s", cribbage.CardSuite.spade),
    ("c", cribbage.CardSuite.club),
    ("d", cribbage.CardSuite.diamond),
    ("h", cribbage.CardSuite.heart)]
);

# Generated by helper function. Contains all card type test 
# types combined with all card suite test types.
card_test_list = None

def generate_card_test_list():
    global card_test_list
    card_test_list = list()
    for card_type in card_type_test_types:
        for card_suite in card_suite_test_types:
            card_test_list.append((card_type[0]+card_suite[0], card_type[1], card_suite[1]))

class Test_atoi(unittest.TestCase):
    
    def test_atoi(self):
        self.assertEqual(cribbage.atoi("asd"), 0)
        self.assertEqual(cribbage.atoi("10c"), 10)
        self.assertEqual(cribbage.atoi("11c1"), 11)
        self.assertEqual(cribbage.atoi("765"), 765)
        
class Test_CardType(unittest.TestCase):
    
    def test_get_card_type(self):
        for card_test_case in card_test_list:
            self.assertEqual(cribbage.CardType.get_card_type(card_test_case[0]), card_test_case[1])
            
class Test_CardSuite(unittest.TestCase):
    
    def test_get_suite(self):
        for card_test_case in card_test_list:
            self.assertEqual(cribbage.CardSuite.get_suite(card_test_case[0]), card_test_case[2])        
    
if __name__ == '__main__':
    generate_card_test_list()
    unittest.main()