#3 rite a function to find out longest palindrome in a given string?
#Not finished

def palindrome(userInput):
    for x in range(len(userInput)):
       print (x)
        #finish this





def mainMenu():

    while True:
        userInput = input ("Please enter a string and I will tell you the longest palindrome, or type X for E(X)it. ")
        if userInput.upper() == "X":
            print("Good bye!")
            break
        elif len(userInput) < 5:
            print("You can do better than that, make it longer!")
        else:
            palindrome(userInput)

if __name__ == "__main__":
    mainMenu()