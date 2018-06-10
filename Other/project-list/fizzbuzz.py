#Fizz Buzz - Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz”
# instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

#To make sure users didnt enter something else than a full positive number
def user_input():

    while True:
        userInput =  input("Please enter upper range limit for this task or [x] to E[x]it: ")

        print(userInput)
        #If input is digit and posivtive integer call main
        if userInput.isdigit():
            if int(userInput) > 1:
                main(userInput)
            else:
                print("Please input positive number thats freather than 1")

        elif userInput.upper() == "X":
            print("Good bye! ")
            break

        else:
            print("Please enter a full int number")

def main(userInput):
    userInput = int(userInput)
    print("main {}" .format(userInput))

    for x in range(1, userInput+1):
        if (x % 3 == 0) and (x % 5 == 0):
            print("FizzBuzz")

        elif (x % 3 == 0):
            print("Fizz")

        elif (x % 5 == 0):
            print("Buzz")

        else:
            print(x)


if __name__ == "__main__":
    user_input()
