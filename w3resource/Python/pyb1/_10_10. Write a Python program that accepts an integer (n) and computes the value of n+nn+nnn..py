'''
10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615
'''

def first(n):
    return int(n) + int(n + n) + int(n + n + n)

def main():
    userInput = input("Enter a value: ")
    result = first(userInput)
    print(result)


if __name__ == "__main__":
    main()


