import random

HANGMANPICS = ['''
 +---+
 |   |
     |
     |
     |
     |
========''', '''
 +---+
 |   |
 O   |
     |
     |
     |
========''', '''
 +---+
 |   |
 O   |
 |   |
     |
     |
========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
========''']

words = 'ant baboon linux ice blender java android apache server bat bear camel cat crew dog donkey duck eagle fox frog goat lion lizard monkey mouse owl panda parrot python rabbit ram rat salmon shark snake spider swan tiger turkey turtle whale zebra'.split()

def getRandomWord(wordlist):
    wordIndex = random.randint(0, len(wordlist)-1)
    return wordlist[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)
    
    # replace blanks with correctly guessed letters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    #show the secret word with spaces in between each letter
    for letter in blanks:
        print(letter, end=' ')
    print()





# Retuens the letter the player entered. This function makes sure
# the player entered a single letter, and nnot something else.

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter : ')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1 :
            print('Please enter a single letter.')
        elif guess in alreadyGuessed :
            print('You have already guessed that letter. Choose again : ')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess



def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')





print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False


while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    # Let the player type in a letter.
    guess = getGuess(missedLetters + correctLetters)


    if guess in secretWord:
        correctLetters = correctLetters + guess

         # Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters :
            print('YES! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess


        # Check if player has guessed too many times and lost
        if len(missedLetters) == len(HANGMANPICS) - 1:
             
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of gusses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters))
            + ' correct gusses, the word was "' + secretWord + '"')
            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break;




    




