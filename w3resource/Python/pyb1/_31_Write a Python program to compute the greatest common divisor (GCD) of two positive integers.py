#31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.


def main():
  userInput = input("Enter 2 numbers separated by comma (,) ")
  userInput = userInput.split(",")

  if (int(userInput[0]) % int(userInput[1]) == 0):
    print(str(userInput[1]))

  


if __name__ == "__main__":
  main()
