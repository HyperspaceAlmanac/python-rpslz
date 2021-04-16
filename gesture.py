class Gesture:
	results = {}
	def __init__(self, value):
		self.value = value
		if not Gesture.results:
			self.populate();
		
	def compare_value(self, left, right):
		result = Gesture.results[left][right]
		if result[0] == 0:
			return (0, "It was a draw")
		elif result[0] == 1:
			return result
		else:
			return (-1, Gesture.results[right][left][1])
	
	def populate(self):
		values = Gesture.results
		values["rock"] = {}
		values["rock"]["rock"] = (0, "")
		values["rock"]["paper"] = (-1, "")
		values["rock"]["scissors"] = (1, "Rock crushes scissors.")
		values["rock"]["lizard"] = (1, "Rock crushes lizard.")
		values["rock"]["spock"] = (-1, "")
		values["paper"] = {}
		values["paper"]["rock"] = (1, "Paper covers rock.")
		values["paper"]["paper"] = (0, "")
		values["paper"]["scissors"] = (-1, "")
		values["paper"]["lizard"] = (-1, "")
		values["paper"]["spock"] = (1, "Paper disproves Spock.")
		values["scissors"] = {}
		values["scissors"]["rock"] = (-1, "")
		values["scissors"]["paper"] = (1, "Scissors cuts paper.")
		values["scissors"]["scissors"] = (0, "")
		values["scissors"]["lizard"] = (1, "Scissors decapitates lizard.")
		values["scissors"]["spock"] = (-1, "")	
		values["lizard"] = {}
		values["lizard"]["rock"] = (-1, "")
		values["lizard"]["paper"] = (1, "Lizard eats paper")
		values["lizard"]["scissors"] = (-1, "")
		values["lizard"]["lizard"] = (0, "")
		values["lizard"]["spock"] = (1, "Lizard poisons Spock")	
		values["spock"] = {}
		values["spock"]["rock"] = (1, "Spock vaporizes rock")
		values["spock"]["paper"] = (-1, "")
		values["spock"]["scissors"] = (1, "Spock smashes scissors")
		values["spock"]["lizard"] = (-1, "")
		values["spock"]["spock"] = (0, "")	
			
		