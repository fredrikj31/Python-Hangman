from levels import Levels

levels = Levels()

class Hangman:

	def startGame(self, Word):
		self.clearBoard()
		levels.printLevel(1, 0, "Houses")

	def pickWordFromList(self):
		pass

	def detectWon(self):
		pass

	def splitWord(self):
		pass

	def clearBoard(self):
		i = 0
		while i < 101:
			print(" ")
			i += 1