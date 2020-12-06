import random

def dice(sides):
    return random.randint(1, sides)

def choose_sides():
    userSides = input("How many sides do you want your dice to have?")
    userSides = int(userSides)
    return userSides

def main():
    sides = choose_sides()

    while True:
        userInput = input("[R] for roll the dice\n[S] Choose dice with different number of sides\n[X] for Exit")
        userInput = userInput.upper()

        if userInput == "X":
            print("Thank you for playing!")
            break

        elif userInput == "R":
            print("You rolled: {}".format((dice(sides))))

        elif userInput == "S":
            sides = choose_sides()

        else:
            print("I don't understand the command")



if __name__ == "__main__":
    main()