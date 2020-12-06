# Question 5
# Level 1
# Question:
# Define a class which has at least two methods: getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class Fiveone(object):
    def __init__(self):
        pass
    def getString(self):
        self.userInput = input("Type in string: ")
    def printString(self):
        print(self.userInput.upper())
result = Fiveone()
result.getString()
result.printString()

