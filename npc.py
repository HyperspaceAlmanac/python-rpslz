import random
from player import Player

class NPC(Player):
	def __init__(self, num):
		super().__init__(num)
	
	def takeAction(self):
		return random.choice(self.moves)