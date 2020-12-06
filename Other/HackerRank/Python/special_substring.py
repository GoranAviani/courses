#Sample Input
#AABCAAADA
#3
#Sample Output
#AB
#CA
#AD

#test: if the first 2 letter are the same print 2 and 3 letter.
#harcoded for every 3
def findSubstring(userInput):
    i = 0
    n = len(userInput) - 2
    for x in range(n):

        print(userInput[i:i+3:1])
        if userInput[i:i+1:1] == userInput[i+1:i+2:1]:
            print(userInput[i+1:i+3:1])
        i += 1


if __name__ == "__main__":
    findSubstring("AABCAAADA")