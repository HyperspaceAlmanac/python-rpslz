from player import Player

class HumanPlayer(Player):
	def __init__(self, num):
		super().__init__(num)
	
	@staticmethod
	def validResponse(val):
		valid = list("12345")
		return val in valid
	def takeAction(self):
		value = input("player" + str(self.player_num) + ": Please press 1 for rock, 2 for paper, 3 for scissors, 4 for lizard, 5 for Spock\n")
		while not HumanPlayer.validResponse(value):
			value = input("Invalid input. Please press 1 for rock, 2 for paper, 3 for scissors, 4 for lizard, 5 for Spock\n")
		return self.moves[int(value) - 1]