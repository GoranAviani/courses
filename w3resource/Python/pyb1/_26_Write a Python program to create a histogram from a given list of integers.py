#26. Write a Python program to create a histogram from a given list of integers
def get_user_input():
    """
    Funtction that fetches user input in a form of a single string and splits it by
    "," into a list
    :return: a list of items
    """
    user_input = input("Enter list of nums for histogram ex: x,y,z,m:\n")
    user_input = user_input.split(",")
    return user_input

def main():
    user_input = get_user_input()
    for x in user_input:
      result = ""
      for p in range (0,int(x)):
        result += "@"
      print(result)

if __name__ == "__main__":
  main()
