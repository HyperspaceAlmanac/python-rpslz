import os
from gesture import Gesture
from human_player import HumanPlayer
from npc import NPC

class Game:
	def __init__(self):
		self.gesture = Gesture()
		self.run()
	def run(self):
		done = False
		while not done:
			self.takeTurn()
			if self.gameOver():
				value = prompt("Would you like to play again? y/n")
				while value != "y" and value != "n":
					os.system('cls')
					value = prompt("Would you like to play again? y/n")
				if value == 'n':
					done = True
				else:
					self.reset()
			else:
				print(f"Player1: {self.p1}, Player2: {self.p2}. {self.roundsToWin} points to win")
	def gameOver(self):
		os.system('cls')
		if self.p1 == self.roundsToWin:
			print("Player 1 is the winner!")
			return True
		elif self.p2 == self.roundsToWin:
			print("Player 2 is the winner!")
			return True
		return False
	def reset(self):
		os.system('cls')
		self.welcome()
		self.vsNPC = self.selectMode()
		self.roundsToWin = self.selectRounds()
		self.p1 = 0
		self.p2 = 0
	def takeTurn(self):
		os.system('cls')
		p1_action = self.player1.takeTurn()
		os.system('cls')
		p2_action = self.player2.takeTurn()
		os.system('cls')
		print(f"player{num} chose {p1_action}, player{num} chose {p2_action}.")
		result = gesture.compare_value(p1_action, p2_action)
		print(result[1])
		if result[0] == -1:
			self.p1 += 1
		elif result[0] == 1:
			self.p2 += 1
		
	def roundsToWin():
		os.system('cls')
		value = input("Please enter a number 2-9 for number of rounds to win")
		valid = set(list("23456789"))
		while (value not in valid):
			os.system('cls')
			value = input("Invalid input: Please enter a number 2-9 for number of rounds to win")
		return int(value)
		
	def selectMode(self):
		value = input("Please enter 1 for vs npc, or 2 for player vs player")
		while value != "1" and value != "2":
		os.system('cls')
			value = input("Invalid input. Please enter 1 for vs npc, or 2 for player vs player")
		self.vsNPC = value == "1"
		self.player1 = HumanPlayer(1)
		if self.vsNPC:
			self.player2 = NPC(2)
		else:
			self.player2 = HumanPlayer(2)
			
	def welcome(self):
		print("Welcome to Rock Paper Scissors Lizard Spock!")
		print("Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock")
		print("Rock rushes Lizard, Lizard poisons Spock, Spock smashes Scissors")
		print("Scissors decapitates Lizard, Lizard eats paper, Paper disproves Spock,")
		print("and Spock vaporizes rock")
		print()
		
if __name__ == "__main__":
	game = Game();