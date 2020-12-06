# Question 13
# Level 2
# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

numbers={'LETTERS':0, 'DIGITS':0}
userInput = input("Enter sentence: ")
for x in str(userInput):
    if x.isdigit():
        numbers['DIGITS'] +=1
    elif x.isalpha():
        numbers['LETTERS'] +=1
print('LETTERS {0} \nDIGITS {1}'.format(numbers['LETTERS'],numbers['DIGITS']))
"""
"""
def number_of_letters_and_digits(userInput):
    number, letter = 0, 0
    for x in str(userInput):
        if x.isdigit():
            number += 1
        elif x.isalpha():
            letter += 1
    return(letter,number)

def main():
    while True:
        userInput = input("Enter sentence: ")
        if userInput.upper() == "X":
            print("Good bye!")
            break

        letters,digits = number_of_letters_and_digits(userInput)
        print('LETTERS {0} \nDIGITS {1}'.format(letters,digits))

if __name__ == "__main__":
    main()
