# This module contains all of the large print functions.
# I.e., for displaying the usage and examples.

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
