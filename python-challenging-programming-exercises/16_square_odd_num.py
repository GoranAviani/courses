# Question 16
# Level 2
# Question:
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9 and 1,9,25,49,81

def main():

    while True:
        result = []
        userInput = input("Ener numbers in list: ")

        if userInput.upper() == "X":
            print("Good bye")
            break

        for x in userInput.split(','):
            if int(x)%2 != 0:
                numSquare = (int(x) ** 2)
                result.append(str(numSquare))
        print(result)
        print(",".join(result))

if __name__ == "__main__":
    main()
