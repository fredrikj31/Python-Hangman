class Levels:

    Level1 = """
      ______
      |    |      
      |    o      Guessed : {}
      |           Guesses left : {}
      |           Average :  50%
      |   
     _|_
    |   |______
    |          |
    |__________|
 
       Phrase: {}
    """

    #FINAL LEVEL
    Level7 = """
      ______
      |    |      Phrase #: {}
      |    o      Guessed : {}
      |   /|\     Average :  50%
      |    |
      |  _/ \_
     _|_
    |   |______
    |          |
    |__________|
 
       Phrase: {}
    """

    def printLevel(self, levelNr, guesses, word):
        if levelNr == 1:
            print(self.Level1.format(12, 0, "Hej med dig"))