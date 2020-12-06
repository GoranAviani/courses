#16. Write a Python function to insert a string in the middle of a string.

# Extra task:
# If there is no symmetrical middle then take 1 more sign from the start (left) side.
import math
def fun(string1, string2):
    string1, string2 = string1.lower()
    if len(string1) % 2 != 0:
        stringMid1 = math.ceil(len(string1)/2)
        stringMid2 = math.floor(len(string1) / 2)
        return string1[:stringMid1] + string2 + string1[len(string1)-stringMid2:]
    else:
        stringMid = int(len(string1)/2)
        return string1[:stringMid] + string2 + string1[stringMid:]





if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert fun("[[]]", "Python") == "[[Python]]"
    assert fun("**", "Python") == "*Python*"
    assert fun("[[<<>>]]", "Python") == "[[<<Python>>]]"
    assert fun("[[<<>]]", "Python") == "[[<<Python>]]"
    assert fun("[", "Python") == "[Python"

    print('Testing completed!')