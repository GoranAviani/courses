import random

def user_input():
    userInput = input('I made a word for you, try to guess it by entering one letter: ')
    userInput = userInput.upper()
    return userInput

#Processes the word to a list for further use, and make result list
def process_word(word):
    processedWord =[]
    result = []

    for x in word:
        processedWord.append(x)
        result.append('*')

    return (processedWord, result)

#Randomly choose one word from the list of words
def choose_word(wordList):
    return(random.choice(wordList))


#If the given letter is in the word , result is returned in format ex. ***A*
def guess_letter(userInput, word, result):


    for pos, x in enumerate(word):
        if x == userInput:
            result[pos] = x

    return(word, result)

#Check if the word is solved, if there are still '*' in the result that means it is not,
# but if there are no '*' then return result = 'solved'
def check_if_solved(word, result):
    if '*' in result:
        return(word, result)
    else:
        result = 'solved'
        return(word, result)
