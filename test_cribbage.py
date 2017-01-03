import cribbage
import unittest

class Test_atoi(unittest.TestCase):
    
    def test_atoi(self):
        self.assertEqual(cribbage.atoi("asd"), 0)
        self.assertEqual(cribbage.atoi("10c"), 10)
        self.assertEqual(cribbage.atoi("11c1"), 11)
        self.assertEqual(cribbage.atoi("765"), 765)
        
class Test_CardType(unittest.TestCase):
    
    def test_get_card_type(self):
        self.assertEqual(cribbage.CardType.get_card_type("zzz"), cribbage.CardType.no_type)
        self.assertEqual(cribbage.CardType.get_card_type("as"), cribbage.CardType.ace)
        self.assertEqual(cribbage.CardType.get_card_type("1s"), cribbage.CardType.ace)
        self.assertEqual(cribbage.CardType.get_card_type("2s"), cribbage.CardType.two)
        self.assertEqual(cribbage.CardType.get_card_type("3s"), cribbage.CardType.three)
        self.assertEqual(cribbage.CardType.get_card_type("4s"), cribbage.CardType.four)
        self.assertEqual(cribbage.CardType.get_card_type("5s"), cribbage.CardType.five)
        self.assertEqual(cribbage.CardType.get_card_type("6s"), cribbage.CardType.six)
        self.assertEqual(cribbage.CardType.get_card_type("7s"), cribbage.CardType.seven)
        self.assertEqual(cribbage.CardType.get_card_type("8s"), cribbage.CardType.eight)
        self.assertEqual(cribbage.CardType.get_card_type("9s"), cribbage.CardType.nine)
        self.assertEqual(cribbage.CardType.get_card_type("10s"), cribbage.CardType.ten)
        self.assertEqual(cribbage.CardType.get_card_type("js"), cribbage.CardType.jack)
        self.assertEqual(cribbage.CardType.get_card_type("11s"), cribbage.CardType.jack)
        self.assertEqual(cribbage.CardType.get_card_type("qs"), cribbage.CardType.queen)
        self.assertEqual(cribbage.CardType.get_card_type("12s"), cribbage.CardType.queen)
        self.assertEqual(cribbage.CardType.get_card_type("ks"), cribbage.CardType.king)   
        self.assertEqual(cribbage.CardType.get_card_type("13s"), cribbage.CardType.king)
    
if __name__ == '__main__':
    unittest.main()