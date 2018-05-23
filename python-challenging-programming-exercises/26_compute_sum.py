# 26
# Question:
# Define a function which can compute the sum of two numbers.
# Hints:
# Define a function with two numbers as arguments. You can compute the sum in the function and return the value.

def sums(userInput):
    numSum = 0
    userInput = userInput.split(',')
    for x in userInput:
        numSum += int(x)
    return (numSum)


def main():
    while True:
        userInput = input("Enter two numbers with ',' between them: ")
        if userInput.upper() == "X":
            break
        print("Sum od given numbers is {0}".format(sums(userInput)))


if __name__ == "__main__":
    main()
