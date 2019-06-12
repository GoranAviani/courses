# 20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.

def calc(x):
    result = ""
    for n in range(0, len(x) + 1):
        result = result + x[0]
    return result


def main():
    data = []
    for x in range(0, 2):
        userInput = input("enter value: \n")
        data.append(userInput)

    result = calc(data)
    print(result)


if __name__ == "__main__":
    main()