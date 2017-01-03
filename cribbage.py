from enum import Enum
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

#
# Print Functions Following This Comment Block.
#

# Prints an example of how to score a hand of cribbage.
def print_example_score():
	print(
"Score Example:\n\
# The cut card must be set so that a hand can be scored. like: ccard qh\n\
# The cut card would now be the queen of Hearts.\n\
# A hand can now be scored using the 'score' command:\n\
# score as,3h,10c,jd\n\
# where the hand would be: Ace of Spades, 3 of Hearts, 10 of Clubs, and a Jack of Diamonds.\n"
	);

# Prints a card string example for each card type.
def print_card_input_examples():
	print(
"Card Input Examples:\n\
Ace of Hearts -> ah\n\
2 of Clubs -> 2c\n\
3 of Spades -> 3s\n\
4 of Diamonds -> 4d\n\
5 of Hearts -> 5h\n\
6 of Clubs -> 6c\n\
7 of Spades -> 7s\n\
8 of Diamonds -> 8d\n\
9 of Hearts -> 9h\n\
10 of Clubs -> 10c\n\
Jack of Spades -> js\n\
Queen of Diamonds -> qd\n\
King of Hearts -> kh\n"	
	);

# Prints all application examples.
def print_examples():
	print_example_score();
	print_card_input_examples();

# Prints the applications usage documentation
def print_usage():
	print(
"Usage:\n\
ccard [cut card] - displays current cut card or if a card is provided, sets the cut card\n\
score <comma delimited hand> - scores a particular hand using the inputted cut card.\n\
help - displays usage.\n\
quit - exits the application.\n"
	);

#
# End of print functions.
#

#CONSTANTS
CUT_CARD = "ccard"
QUIT = "quit"
HELP = "help"
SCORE = "score"
INPUT_STR = ">>>"

# Recreation of ANSII C's atoi function.
# Will create an int from a string even if there are is alpha characters in the string.
# E.g.:
# asd -> 0
# 10c -> 10
# 10c1 -> 10
# 765 -> 765
def atoi(a_str):
	result = ""
	for i in range(len(a_str)):
		a_char = a_str[i]
		if a_char >= '0' and a_char <= '9':
			result = result + a_char
		else:
			break;
	if len(result) > 0:
		return int(result)
	else:
		return 0	 

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

# Card object encapsulates card related data and functionality.
class Card(object):
	card_type = CardType.no_type;
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
		print("suite value: ", suite);
		#get card type and value
		card_type = CardType.get_card_type(card_str)
		print("card type: ", card_type)
		card_val = card_type.value
		if card_type.value > 10:
			card_val = 10;
		print("card value: ", card_val)
		#call card initializer and return
		return Card(card_type, card_val, suite)

	# Returns a string representation of this object
	def toString(self):
		return self.card_type.name + " of " + self.suite.name

class CardHand(object):
	card_hand = None;
	cut_card = None;
	validity_checked = False;
	validity = False;	

	# Initializer
	def __init__(self, card_hand, cut_card):
		self.card_hand = card_hand;
		self.cut_card = cut_card;

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
			type_list = list([0] * CardType.__len__())
			for card in self.card_hand:
				type_list[card.card_type.value] += 1
			# Add cut card card into type list to check multiples
			type_list[self.cut_card.card_type.value] += 1
			for ctype in range(len(type_list)):
				if type_list[ctype] > 1:
					# Have at least a pair, score
					if type_list[ctype] == 2:
						print("Pair for 2.")
						score += 2
					elif type_list[ctype] == 3:
						print("Three of a kind for 6.")
						score += 6
					elif type_list[ctype] == 4:
						print("Four of a kind for 12.")
						score += 12
					else:
						print("Error: Card count was far too large.")
						return 0
			return score;
		else:
			print("Unexpecred multiples result, returning score of 0.")
		return 0

	def score_runs(self):
		if self.isValid():
			score = 0
			
					
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
			else:
				self.validity = True;
				return self.validity;
			
# Handles user input to view and set the cut card
# E.g., ccard jh
def handle_cut_card(cut_card_input, cut_card):
	print("Handling cut card...");
	cut_card_partition = cut_card_input.rpartition(" ")
	cut_card_input = cut_card_partition[2]
	if len(cut_card_input) > 0 and len(cut_card_partition[0]) > 0:
		print(cut_card_input);
		new_cut_card = Card.create_card(cut_card_input);
		if new_cut_card.is_valid():
			print("Changing cut card...")
			if cut_card != None:
				print("Old cut card:\n", cut_card.toString())
			cut_card = new_cut_card;
			print("New cut card:\n", cut_card.toString())
		else:
			print("Cut card input is invalid: ", cut_card_input)
	elif cut_card == None:
		print("There is no current cut card.")
	else:
		print("The current cut card: ", cut_card.toString())
	return cut_card;

# Handles user input to score a cribbage hand
# E.g., score as,2c,3d,4h
def handle_score(score_input, cut_card):
	print("Scoring hand...");
	if cut_card == None:
		print("Cut card has not been set. See help for usage details.")
		return
	# Parse hand
	hand = CardHand.create_hand(score_input.rpartition(" ")[2], cut_card)
	# Check hand
	if hand.isValid():
		print("Scoring hand...");
		score = 0;
		# Score multiples (pairs, three of a kind, four of a kind)
		score += hand.score_multiples()
		# Score flush - is this a crib hand? (only if cut card doesn't match a hand that is a flush)
		score += hand.score_flush()
		# Score runs - min of three cards
		# Score fifteens
		
		print("Total score: ", score)

# Main loop for application, continually asks for and handles input.
def main():
	cut_card = None;
	print_usage();
	print_examples();
	while 1:
		user_input = input(INPUT_STR).lower()
		if user_input.startswith("q"):
			print("Exiting the application.");		
			exit(0);
		elif user_input.startswith("c"):
			cut_card = handle_cut_card(user_input, cut_card);
		elif user_input.startswith("h"):
			print_usage();
			print_examples();
		elif user_input.startswith("s"):
			handle_score(user_input, cut_card);

if __name__ == "__main__":
	main();
