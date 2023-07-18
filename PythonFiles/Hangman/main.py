import word
import InputChecker
import draw

# the current word of the game
controllerClass = word.WordsController
# drawClass = draw.WordsController

# get random word for the game
currentWord = controllerClass.getStartWord().upper()

# convert word to _ _ _ _ _
currentGuessed = controllerClass.createGuesser(currentWord)

turns = 0
health = len(draw.hangMan)

print(currentGuessed)
# print(test.isalpha())
# print(draw.hangMan[1])

def startGame():
    print("Welcome to Hangman Try guessing the right word by giving a letter each turn")

    while(checkNext()):
        letter = input("Guess a letter :")
        # turns += 1 
        print("da")


# Checks if the player can gues againn
def checkNext():
    if(turns >= health): # if ran out of turns
        print("Lost game")
        return False
    if(currentGuessed == currentWord):# if word is guesed or not
        print("Won game")
        print("Want to play again?")
        return False
    
    return True

def updateWord(char):
    print()

# startGame()

