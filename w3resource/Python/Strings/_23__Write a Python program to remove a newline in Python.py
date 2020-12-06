#23. Write a Python program to remove a newline in Python



def fun(text):
    return text.replace("\n","")

if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert fun("sumama \n") == "sumama "
    assert fun("\nsum\n") == "sum"
    assert fun("po-\nsumama\n-i-\ngorama--") == "po-sumama-i-gorama--"

    print('Testing completed!')
