from Card.Card import *
class CardHand(object):
	card_hand = None;
	cut_card = None;
	validity_checked = False;
	validity = False;
	type_list = None;
	score = 0	

	# Initializer
	def __init__(self, card_hand, cut_card):
		self.card_hand = card_hand;
		self.cut_card = cut_card;
		self.init_type_list()
		self.isValid()

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

	def init_type_list(self):
			self.type_list = list([0] * CardType.__len__())
			for card in self.card_hand:
				self.type_list[card.card_type.value] += 1
			# Add cut card card into type list to check multiples
			self.type_list[self.cut_card.card_type.value] += 1
	
	# Scores a hand for multiples (pairs, three of a kind, four of a kind)
	# Returns the score from multiples or zero if no score.
	def score_multiples(self):
		if self.isValid():
			score = 0
			for ctype in range(len(self.type_list)):
				if self.type_list[ctype] > 1:
					# Have at least a pair, score
					if self.type_list[ctype] == 2:
						print("Pair for 2.")
						score += 2
					elif self.type_list[ctype] == 3:
						print("Three of a kind for 6.")
						score += 6
					elif self.type_list[ctype] == 4:
						print("Four of a kind for 12.")
						score += 12
					else:
						print("Error: Card count was far too large.")
						return 0
			return score;
		else:
			print("Unexpecred multiples result, returning score of 0.")
		return 0

	#def score_runs(self):
	#	if self.isValid():
	#		score = 0
	#		raise NotImplementedError
	
	#def score_fifteens(self):
	#	raise NotImplementedError

	## Checks the hand for jacks of the same suit as the cut card.
	#def score_nobs(self):
	#	if self.isValid():
	#		raise NotImplementedError

	def score_hand(self):
		self.score = 0
		# Score knobs
		#self.score += self.score_nobs()
		# Score multiples (pairs, three of a kind, four of a kind)
		self.score += self.score_multiples()
		# Score runs - min of three cards
		#self.score += self.score_runs()
		# Score flush - is this a crib hand? (only if cut card doesn't match a hand that is a flush)
		self.score += self.score_flush()
		# Score fifteens
		#self.score += self.score_fifteens()
					
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