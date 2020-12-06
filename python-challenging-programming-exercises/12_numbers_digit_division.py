# Question 12
# Level 2
# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an
# even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

def numbers_digit_division():
    resultList = []
    for x in range(1000, 3001):
        isEven = True
        for y in str(x):
            if int(y) % 2 == 0:
                pass
            else:
                isEven = False
        if isEven == True:
            resultList.append(str(x))
    print(",".join(resultList))

numbers_digit_division()
