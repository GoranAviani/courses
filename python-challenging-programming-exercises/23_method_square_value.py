# Question 23
# level 1
# Question:
#    Write a method which can calculate square value of number

# Hints:
# Using the ** operator

class Calculation():

    def __init__(self, ):
        pass

    def square_of_number(self, number):
        number = float(number) ** 2
        self.result(number)

    # print without dot if number is integer, else print as float
    def result(self, squareOfNumber):
        if squareOfNumber.is_integer():
            print(int(squareOfNumber))
        else:
            print(squareOfNumber)


def main():
    number = Calculation()

    while True:
        userInput = input("Enter number: ")
        if userInput.upper() == "X":
            print("Good bye!")
            break
        number.square_of_number(userInput)


if __name__ == "__main__":
    main()
