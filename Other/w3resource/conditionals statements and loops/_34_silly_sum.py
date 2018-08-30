


#34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

userInput = input(" enter first no: ")
userInput1 = input(" enter second no: ")

sum = int(userInput) + int(userInput1)

if (sum < 21 and sum > 14):
print ("20")
else:
print(str(sum))
