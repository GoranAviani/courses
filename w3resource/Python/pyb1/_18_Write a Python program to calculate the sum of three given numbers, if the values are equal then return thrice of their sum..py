#18. Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return thrice of their sum.


def calcSum(calcSum):
    result = 0

    for x in calcSum:
        result += x

    if (result / 3 ==  calcSum[0]):
        result = result * 2
    return result

def main():
    numbers = []
    for x in range(1, 4):
        userInput = int(input("Enter the {}. number" . format(x)))
        numbers.append(userInput)

    result = calcSum(numbers)
    print(str(result))

if __name__ == "__main__":
    main()