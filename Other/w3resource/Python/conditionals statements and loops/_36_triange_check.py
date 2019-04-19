#36. Write a Python program to check a triangle is equilateral, isosceles or scalene. Go to the editor
#Note :
#An equilateral triangle is a triangle in which all three sides are equal.
#A scalene triangle is a triangle that has three unequal sides.
#An isosceles triangle is a triangle with (at least) two equal sides.
#Expected Output:

#Input lengths of the triangle sides:
#x: 6
#y: 8
#z: 12
#Scalene triangle

def inputs():
    statusMessage = ""
    userInput1 = input("enter size of 1. side: ")
    userInput2 = input("enter size of 2. side: ")
    userInput3 = input("enter size of 3. side: ")

    if ((userInput1.upper() == "X") or( userInput2.upper() == "X") or (userInput3.upper() == "X")):
        statusMessage = "EXIT"
    else:
        statusMessage = "OK"

    return statusMessage, userInput1, userInput2, userInput3


def checkTriangle(userInput1, userInput2, userInput3):

    if userInput1.isnumeric() and userInput2.isnumeric() and userInput3.isnumeric():

        if userInput1 == userInput2 == userInput3:
            triangleResult = "Equilateral triangle"
        elif userInput1 != userInput2 != userInput3:
            triangleResult = "Salene triangle"
        else:
            triangleResult = ("Isosceles triangle")


    else:
        triangleResult = "There are letters for sides instead of numbers"

    return triangleResult

while True:
    statusMessage, userInput1, userInput2, userInput3 = inputs()
    if statusMessage == "EXIT":
        print("good bye!")
        break
    elif statusMessage == "OK":
       triangleResult = checkTriangle(userInput1, userInput2, userInput3)
       print(triangleResult)