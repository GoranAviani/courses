#Check if Palindrome - Checks if the string entered by the user is a palindrome.
# That is that it reads the same forwards as backwards like “racecar”


def main():

    while True:
        userInput = input("Enter word to check if it's palindrome or [x] to E[x]it: ")

        if userInput.upper() == "X":
            print("Good bye!")
            break
            #palindrome check
        elif userInput.upper() == (userInput.upper()[::-1]):
            #Print first letter of the work uppercase so it looks better
            print("{} is a palindrome".format(userInput[:1].upper() + userInput[1::]))

        else:
            #Print first letter of the work uppercase so it looks better
            print("{} is not a palindrome".format(userInput[:1].upper() + userInput[1::]))


if __name__ == "__main__":
    main()