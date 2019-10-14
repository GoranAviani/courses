#18. Write a Python function to get a string made of its first three characters of a specified string. If the length of
# the string is less than 3 then return the original string. Go to the editor
#Sample function and result :
#first_three('ipy') -> ipy
#first_three('python') -> pyt


def fun(text):
    if len(text) < 4:
        return text
    else:
        return text[:3]

if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert fun("Po-sumama-i-gorama") == "Po-"
    assert fun("The") == "The"

    print('Testing completed!')
