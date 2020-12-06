#58. Write a Python program to move spaces to the front of a given string.

def fun(text):
    result =""
    numOfSpaces = text.count(" ")
    spaces = numOfSpaces * " "
    for x in text:
        if x == " ":
          pass
        else:
          result+=x

    result = spaces + result
    return result



if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("auto 2 2") == "  auto22"
    assert fun("Stockholm is the capitol of Sweden.") == "     StockholmisthecapitolofSweden."


    print('Testing completed!')