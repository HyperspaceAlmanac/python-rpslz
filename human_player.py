from player import Player

class HumanPlayer(Player):
	def __init__(self, num):
		super(num)
	
	@staticmethod
	def validResponse(val):
		valid = list("12345")
		return val in valid
	def takeAction():
		value = input("player" + str(num) + ": Please press 1 for rock, 2 for paper, 3 for scissors, 4 for lizard, 5 for Spock")
		while (!validResponse(value)):
			value = input("Invalid input. Please press 1 for rock, 2 for paper, 3 for scissors, 4 for lizard, 5 for Spock")
		return moves[int(value) - 1]