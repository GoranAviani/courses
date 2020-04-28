#4. Write a Python program which accepts the radius of a circle from the user and compute the area

def calc_radius(userInput):
    result = 2 * float(userInput) * 3.14
    return result


while True:
    userInput = input("Enter the radius or X to exit: ")
    print("Good bye") if userInput.upper() == "X" else  print("Area is {}".format(calc_radius(userInput)))



