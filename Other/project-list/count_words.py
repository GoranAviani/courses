
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
        print(int(sums))


if __name__ == "__main__":
    main()