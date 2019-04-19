#4. Write a Python program which accepts the radius of a circle from the user and compute the area

def calc_radius(userInput):
    result = 0
    result = 2 * float(userInput) * 3.14
    return result


while True:

    userInput = input("Enter the radius or X to exit: ")

    if userInput.upper() == "X":
        print("Good bye.")
        break
    else:
        result = calc_radius(userInput)
        print("Area is {}".format(result))



