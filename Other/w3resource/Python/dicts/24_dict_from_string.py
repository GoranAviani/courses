

#24. Write a Python program to create a dictionary from a string. Go to the editor
#Note: Track the count of the letters from the string.
#Sample string : 'w3resource'
#Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

userInput = "w3resource"
result ={}
for x in userInput:
    if x not in result:
        result[x] = 1
    else:
        result[x] +=1

print("{}".format(result))
