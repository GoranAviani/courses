import random

print('---------------------------------')
print(' GUESS THAT NUMBER GAME  ')
print('---------------------------------')

theNumber = random.randint(0,100)
guess = 0
userName = input("Enter your name: ")
while guess != theNumber:
    guessText = input('Guess a number between 0 and 100: ')
    guess = int(guessText)

    if guess < theNumber:
        print("Sorry {1}, your guess of {0} was to low.".format(guess, userName))
    elif guess > theNumber:
        print("Sorry {1}, your guess of {0} was to high." .format(guess, userName))
    else:
        print("You got it {0}!".format(userName))