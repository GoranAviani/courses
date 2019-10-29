# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000

def num_within(n):
    result = ""
    if (n > 100 and n < 1000):
        result = "n is within 100 and 1000"
    elif n > 999:
        result = "n iswithin 2000"
    else:
        result = "n is not withing these ranges"
    return result


def main():
    userInput = input("Enter a number \n")
    result = num_within(int(userInput))
    print(result)


if __name__ == "__main__":
    main()