#25. Write a Python program to check whether a specified value is contained in a group of values. Go to the editor
#Test Data :
#3 -> [1, 5, 8, 3] : True
#-1 -> [1, 5, 8, 3] : False




def main():
    groupOfValues = []
    for x in range(0, 4):
        userInput = input ("Enter a number for a group of values")
        if userInput.isnumeric():
            groupOfValues.append(int(userInput))
        else:
            print("That is not a number")

    userInput = input("Enter a number you are looking for")
    if int(userInput) in groupOfValues:
        print("num {} is there!" . format(userInput))
    else:
        print("Num is not there")


if __name__ == "__main__":
    main()