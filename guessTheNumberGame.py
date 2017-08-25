#"Guess The Number" Game

import random5

number = random.randint(1,50)

numberOfGuesses = 0

print('Hello! What is your name?')

playerName = input()

print('Well, '+ playerName + ' I am thinking of a number between 1 and 50, Can you guess it?')

while (numberOfGuesses < 8):
    print('Your Guess: ')
    guess = input()
    numberOfGuesses += 1
    guess = int(guess)

    if (guess < number):
        print('Your guess is too low')

    elif (guess > number):
        print('Your guess is too high')

    elif(guess == number):
        break

if (guess != number):
    number = str(number)
    print('Sorry... You lost, The number is ' + number )

elif (guess == number):
    numberOfGuesses = str(numberOfGuesses)
    print('Congratulations ' + playerName + '! You got it right after ' + numberOfGuesses + ' guesses.')
