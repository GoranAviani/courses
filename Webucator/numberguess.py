import random

def num_generator():
    return(random.randint(1,100))


def main():
    isGuessed = False
    number = num_generator()


    while not isGuessed:
        userInput = input("Try to guess the number between 1 and 100")

        #Checking if the userInput is a digit
        if userInput.isdigit():
            userInput = int(userInput)
            if userInput == number:
                print("Bravo! you gessed the number! ")
                isGuessed = True

            elif userInput < number:
                print("Number you are looking for is BIGGER that that!")

            elif userInput > number:
                print("Number you are looking for is SMALLER that that!")
        #if userInput is not a digit
        else:
            print("I don't understand that, please try again")


if __name__ == "__main__":
    main()