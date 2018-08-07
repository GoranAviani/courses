#2) Write a method which will remove any given character from a String?

def start():

    while True:
        userInput = input ("Input a string and a comma and a character to be removed. X to E(X)it.")
        if userInput.upper() == "X":
            print("Good bye")
            break
        else:
            userInput = userInput.split(",")
            result = removal(userInput[0], userInput[1])
            print("word {0} is {1} without {2}".format( userInput[0],result, userInput[1]))


def removal(word, letter):
    removed = ""
    for x in word:
        if x == letter:
            continue
        else:
            removed = removed + x

    print (removed)
    return removed





if __name__ == "__main__":
    start()
