#13. Write a Python program to generate a 3*4*6 3D array whose each element is *.


def fun():
  return [[ ['*' for col in range(6)] for col in range(4)] for row in range(3)]




if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun() == [[['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*']], [['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*']], [['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*']]]

    print('Testing completed!')