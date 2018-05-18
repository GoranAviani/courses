# Question 15
# Level 2
# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

class Femton(object):

    def __init__(self):
        pass

    def calculate(self, userInput):
        result = int(userInput) + int(str(userInput + userInput)) + int(str(userInput + userInput + userInput)) + int(
            str(userInput + userInput + userInput + userInput))
        return(result)

def main():
    first = Femton()

    while True:
        userInput = input("Enter number: ")
        if userInput.upper() == "X":
            break
        print(first.calculate(userInput))

if __name__ == "__main__":
    main()