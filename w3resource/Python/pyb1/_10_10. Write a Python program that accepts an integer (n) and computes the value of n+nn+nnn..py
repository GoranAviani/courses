'''
10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615
'''

def first(n):
    return int(n) + int(n + n) + int(n + n + n)

def second(n):
    number_string = ""
    result = 0
    n = int(n)

    for x in range(0, 3):
         number_string += str(n)
         result += int(number_string)
    return result

def main():
    userInput = input("Enter a value: ")
    result, result1 = first(userInput), second(userInput)
    print(result)
    print(result1)


if __name__ == "__main__":
    main()


