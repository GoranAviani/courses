#30. Write a Python program that will accept the base
# and height of a triangle and compute the area.


def main():
  size = []
  result = 0
  userInput = input("Enther the base")
  size.append(userInput)
  userInput = input("Enther the height")
  size.append(userInput)

  result = float(size[0]) * float(size[1])/2
  print(str(result))
  
if __name__ == "__main__":
  main()
