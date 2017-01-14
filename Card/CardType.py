from enum import Enum
from Misc.Utils import atoi

# CardType class encapsulates card type functionality.
class CardType(Enum):
	no_type = 0
	ace = 1
	two = 2
	three = 3
	four = 4
	five = 5
	six = 6
	seven = 7
	eight = 8
	nine = 9
	ten = 10
	jack = 11
	queen = 12
	king = 13

	# Determines the card's type based off its card string
	# E.g., qs -> queen
	def get_card_type(card_str):
		atoi_result = atoi(card_str);
		if atoi_result > 0:
			return CardType(atoi_result);
		elif card_str[0] == 'a':
			return CardType.ace
		elif card_str[0] == 'j':
			return CardType.jack
		elif card_str[0] == 'q':
			return CardType.queen
		elif card_str[0] == 'k':
			return CardType.king
		else:
			return CardType.no_type
	
	def get_card_value(self):
		card_val = 0
		if self.value > 10:
			card_val = 10;
		else:
			card_val = self.value
		return card_val
	
	def get_list():
		return [ct for ct in CardType]