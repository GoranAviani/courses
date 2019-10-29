#26. Write a Python program to create a histogram from a given list of integers
def main():
    userInput = input ("Enter list of nums for histogram ex: x,y,z,m:\n")

    userInput = userInput.split(",")
    print(str(userInput))

    for x in userInput:
      result = ""
      for p in range (0,int(x)):
        result += "@"
      print(result)

if __name__ == "__main__":
  main()
