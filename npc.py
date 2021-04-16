import random
from player import Player

class NPC(Player):
	def __init__(self, num):
		super.__init__('NPC', num)
	
	def takeAction():
		return random.choice(moves)