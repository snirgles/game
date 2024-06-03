import random

#counter

guessesLeft = 10

#list of words

words = ["cards", "plaid", "gross", "howdy", "wipeout", "lemon", "fry", "bold", "cat", "website", "merge"]

secretWord = random.choice(words)

clue = len(secretWord) * "?"

symbol = "✨"

guessedWordCorrectly = False

def updateClue(guessedLetter, secretWord, clue):
    index = 0
    while index < len(secretWord):
        if guessedLetter == secretWord[index]:
            # print(index)


            clue[index] = guessedLetter
        index += 1

def listToString(myList):
    clueString = " "
    return (clueString.join(myList))

#script of actual gameplay

print("Guess the word related with cowboys!")

while guessesLeft > 0:
    print(listToString(clue))
    print("Guesses left: " + symbol * guessesLeft)
    guess = input("Guess a letter or the whole word: ")

    if guess == secretWord:
        guessedWordCorrectly = True
        break

    if guess in secretWord:
        updateClue(guess, secretWord, clue)

    else:
        print("Incorrect guess, you lost a life!")
        guessesLeft -= 1

if guessedWordCorrectly:
    print("You win! The seret word was: " + secretWord)
else:
    print("Yikes! You lost, the secret word was " + secretWord)