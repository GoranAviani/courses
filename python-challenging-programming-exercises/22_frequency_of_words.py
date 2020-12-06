# Question 22
# Level 3
# Question:
# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1
# Hints
# In case of input data being supplied to the question, it should be assumed to be a console input.

import operator

def frequency_of_words(sentence):
    listSentence = sentence.split(' ')
    resultDict = {}
    for x in listSentence:
        if x in listSentence and x not in resultDict:
            count = listSentence.count(x)
            resultDict[x] = count

    # original answer:
    # for key in sorted(resultDict):
    #    print("{0}:{1}".format(key,resultDict[key]))

    # TODO: sort by dict value - descending
    for key in sorted(resultDict.items(), key=operator.itemgetter(1), reverse=True):
        print("{0}:{1}".format(key[0], key[1]))


def main():
    userInput = ""
    while userInput.upper() != "X":
        userInput = input("Enter sentence or E[x]it: ")
        frequency_of_words(userInput)

    print("Good bye!")


if __name__ == "__main__":
    main()
