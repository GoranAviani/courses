import calculation

def main():
    wordList = ['CAT', 'DOG', 'HOUSE', "STOCKHOLM", "PYTHON"]
    word = calculation.choose_word(wordList)
    word, result = calculation.process_word(word)

    while True:
        userInput = calculation.user_input()

        #Checking if userInput is a letter
        if userInput.isalpha():
            userInput = userInput.upper()
            #check if there is just on letter in userInfo
            if len(userInput) > 1:
                print('Only one letter please!')

            elif userInput in word:
                word, result = (calculation.guess_letter(userInput, word, result))
                word, result = calculation.check_if_solved(word, result)
                if result == 'solved':
                    print("Bravo!, the word was {} and you solved it!". format(''.join(word)))
                    break

                print(word)
                print("Current status: {}".format(' '.join(result)))

            elif userInput not in word:
                print("Good try but {} is not in the word!". format(userInput))
                print("Challenge status: {}".format(' '.join(result)))


        #if letter or letter are not inputed
        else:
            print('Letter only please!')



if __name__ == '__main__':
    main()