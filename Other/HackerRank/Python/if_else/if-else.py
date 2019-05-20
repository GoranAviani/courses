
def main():
    userInput = input ("enter a number from 1 to 100: ")

    userInput = int(userInput)

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
