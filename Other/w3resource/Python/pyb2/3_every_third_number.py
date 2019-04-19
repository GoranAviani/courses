#3. Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.

def everyThird(userInput):
 counter = 0

 for x in userInput:
     counter += 1
     if counter % 3 == 0:
         print(x)


while True:
   userInput = input("Enter a list of numbers")
   userInput = userInput.split(',')
   everyThird(userInput)




