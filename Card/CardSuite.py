from enum import Enum

# Card suite class encapsulates suite functionality.
class CardSuite(Enum):
	no_type = 0
	heart = 1
	diamond = 2
	club = 3
	spade = 4

	# Identifies a card's suite from its card string
	# E.g., 10c -> club
	def get_suite(card_str):
		result = CardSuite.no_type;
		suite_char = card_str[len(card_str) - 1]; 
		if suite_char == 'h':
			result = CardSuite.heart;
		elif suite_char == 'd':
			result = CardSuite.diamond;
		elif suite_char == 'c':
			result = CardSuite.club;
		elif suite_char == 's':
			result = CardSuite.spade;
		return result;
	
	def get_list():
		return [cs for cs in CardSuite]	