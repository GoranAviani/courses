#Count Vowels - Enter a string and the program counts the number of vowels in the text.
# For added complexity have it report a sum of each vowel found.

#count the number of vowels
def counting(userInput):
    vowels = {"A": 0, "E": 0, "I": 0, "O": 0, "U":0}

    for letter in userInput.upper():
        if letter in vowels:
            vowels[letter] += 1

    return vowels

def main():


    while True:
        userInput = input("Please enter word so I can count vowels, or just [x] to E[x]it: ")

        voewls = (counting(userInput))

        #print the count of voewls
        for k,v in voewls.items():
            print("{} : {}".format(k, v))


        if userInput.upper() == "X":
            print("Good bye!")
            break

if __name__ == "__main__":
    main()