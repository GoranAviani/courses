#56. Write a Python program to convert a string to a list

def fun(item1, item2):
   # return item1.split(" ")

# convert a string with a user inputed delimeter
  #  result = []
  #  for x in item1:
  #      if x != item2:
  #          result.append(x)

  #  return result

    return item1.split(item2)

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("1 2 3", " ") == ['1', '2', '3']
    assert fun("1-2-3", "-") == ['1', '2', '3']

    print('Testing completed!')