#1) Write code to check a String is palindrome or not?


def palindrome():

    while True:
        userInput = input("Write text to check if palindrome or not. X to exit:\n ")
        print(userInput.upper())
        if userInput.upper == "X":
            break
        else:
            if userInput == userInput[::-1]:
                print("{} is a palindrome".format(userInput))
            else:
                print("{} is not a palindrome".format(userInput))




if __name__ == "__main__":
    palindrome()