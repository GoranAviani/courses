#13. Write a Python script that takes input from the user and displays that input back in upper and lower cases.

def fun(userInput):
    result=[]
    result.append(userInput.upper())
    result.append(userInput.lower())
    return result



if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert fun("Kuca") == ["KUCA", "kuca"]

    print('Testing completed!')