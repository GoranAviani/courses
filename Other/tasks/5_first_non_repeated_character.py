#5) How to find first non repeated character of a given String


def firstNonRepeatedChar():
    userInput = input("Enter a word: ")
    for x in userInput:
        if userInput.count(x) == 1:
            print(x)
            break


if __name__ == "__main__":
    firstNonRepeatedChar()