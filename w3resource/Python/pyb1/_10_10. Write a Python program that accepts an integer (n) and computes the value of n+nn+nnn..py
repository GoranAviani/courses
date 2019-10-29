'''
10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615
'''

def first(n):

    numStr = ""
    result1 = 0
    n = int(n)
    for x in range(0, 3):
        numStr += str(n)
        result1 += int(numStr)
    return result1



def main():
    userInput = input("Enter a value: ")

    result1 = first(userInput)


    print(result1)


if __name__ == "__main__":
    main()


