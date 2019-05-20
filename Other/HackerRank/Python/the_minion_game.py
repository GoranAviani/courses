#Kevin and Stuart want to play the 'The Minion Game'.
#Game Rules
#Both players are given the same string, .
#Both players have to make substrings using the letters of the string .
#Stuart has to make words starting with consonants.
#Kevin has to make words starting with vowels.
#The game ends when both players have made all possible substrings.
#Scoring
#A player gets +1 point for each occurrence of the substring in the string .
#For Example:
#String = BANANA
#Kevin's vowel beginning word = ANA
#Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.


userInput = "BANANA"

def minionGame(userInput):

    vowels = "AEIOU"
    kevin = 0
    stuard = 0


    for i in range(len(userInput)):
        print("number " +str(i))
        if userInput[i] in vowels:
            print("kevin: "+ userInput[i])
            kevin += (len(userInput) - i)
            print("kevin has "+ str(kevin))
        else:
            print("stuard: " +userInput[i])
            stuard += (len(userInput) - i)
            print("stuard has: " + str(stuard))

    if kevin > stuard:
        print ("Kevin has total " + str(kevin))
    elif kevin < stuard:
        print("Stuart has total " + str(stuard))
    else:
        print("Draw")





if __name__ == "__main__":
    minionGame(userInput)
