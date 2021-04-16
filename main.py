import os
from gesture import Gesture
class Game:
	def __init__(self):
		self.reset()
	def run(self):
		print("hello world")
	def reset(self):
		os.system('cls')
		self.welcome()
		self.vsNPC = self.selectMode()
	def selectMode(self):
		value = None
		while (value != "1" and value != "2") or value is None:
			value = input("Please enter 1 for vs npc, or 2 for player vs player")
		self.vsNPC = value == "1"
		self.player1 = HumanPlayer()
		if self.vsNPC:
			
	def welcome(self):
		print("Welcome to Rock Paper Scissors Lizard Spock!")
		print("Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock")
		print("Rock rushes Lizard, Lizard poisons Spock, Spock smashes Scissors")
		print("Scissors decapitates Lizard, Lizard eats paper, Paper disproves Spock,")
		print("and Spock vaporizes rock")
		print()
if __name__ == "__main__":
	game = Game();