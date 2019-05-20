def input_check(userInput):
    if 1<= userInput <= 100:
        pass
    else:
        print("This number is not in a approved range.")
        return ("no")

def main():
    userInput = input ("enter a number from 1 to 100: ")


    userInput = int(userInput)

    status = input_check(userInput)

    if status == "no":
        pass
    else:
        if userInput % 2 == 0:
            if 2 <= userInput <= 5:
                print("not wierd")
            elif 6 <= userInput <= 20:
                print("weird")
            elif userInput > 20:
                print("not weird")
        else:
            print("wierd")


if __name__ == "__main__":
    main()
