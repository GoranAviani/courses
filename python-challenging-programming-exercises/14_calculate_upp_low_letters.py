# Question 14
# Level 2
# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

def calculate(userInput):
    numbers = {'Upper': 0, 'Lower': 0}
    for x in str(userInput):
        if x.isupper():
            numbers['Upper'] += 1
        elif x.islower():
            numbers['Lower'] += 1

    return (numbers)


def main():
    while True:
        userInput = input("Enter sentence: ")
        if userInput.upper() == "X":
            break
        numbers = calculate(userInput)
        print("UPPER CASE {0}\nLOWER CASE {1}".format(numbers['Upper'],numbers['Lower']))

if __name__ == "__main__":
    main()
