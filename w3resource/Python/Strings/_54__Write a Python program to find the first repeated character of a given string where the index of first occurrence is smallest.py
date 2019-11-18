#54. Write a Python program to find the first repeated character
# of a given string where the index of first occurrence is smallest


# first found will always have the smallest index number.
def fun(text):
    allChars = list(text)
    for x in text:
         if allChars.count(x) > 1:
            return x



if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("aebcedei") == "a"
    assert fun("aebeqerewrewrecaedei") == "a"
    assert fun("ebqrwrwrcadi") == "w"

    print('Testing completed!')