#13. Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its
#input and print the numbers that are divisible by 5 in a comma separated sequence.


userInput = "0100, 0011, 1010, 1001, 1100, 1001"
userInput = userInput.split(", ")
print(userInput)

for bin in userInput:
    #print(int(bin, 2))

    if ((int(bin, 2)) % 5 == 0):

        print(bin)

