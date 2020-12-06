#Count Words in a String - Counts the number of individual words in a string.
#  For added complexity read these strings in from a text file and generate a summary

def counter(userInput):
    userInput = userInput.split(" ")
    result = {}
    for x in userInput:
        if x in result:
            result[x] += 1
        else:
            result[x] = 1

    return result

def total_words(result):

    sums = 0
    for x in result:
        sums += result[x]

    return sums

def main():

    while True:
        userInput = input ("Enter sentence so I can count words: ")
        if userInput.upper() == "X":
            print("Good bye!")
            break

        else:
            result = counter(userInput)
            sums = total_words(result)

        print(result)
        print("Total number of words: " + str(sums))


if __name__ == "__main__":
    main()