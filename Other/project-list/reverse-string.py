#Reverse a String - Enter a string and the program will reverse it and print it out.


def main():
    userInput = input("Enter a string: ")
    return userInput[::-1]

if __name__ == "__main__":
    print(main())