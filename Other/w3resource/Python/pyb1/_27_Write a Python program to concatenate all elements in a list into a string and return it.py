#27. Write a Python program to concatenate all elements in a list into a string and return it. 
def main():
  list1 = [1,2,3,4]
  result = ""
  for x in list1:
    result += str(x)
  print(result)

if __name__ == "__main__":
  main()
