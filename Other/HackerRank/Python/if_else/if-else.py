def input_check(userInput):
    if 1<= userInput <= 100:
        pass
    else:
        print("This number is not in a approved range.")
        return ("no")

def main():
    userInput = input ("")


    userInput = int(userInput)

    status = input_check(userInput)

    if status == "no":
        pass
    else:
        if userInput % 2 == 0:
            if 2 <= userInput <= 5:
                print("Not Weird")
            elif 6 <= userInput <= 20:
                print("Weird")
            elif userInput > 20:
                print("Not Weird")
        else:
            print("Weird")


if __name__ == "__main__":
    main()
