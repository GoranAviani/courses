#9. Write a Python program to remove the nth index character from a nonempty string.

def fun(word, n):
    result = ""
    counter = 0
    for x in word:
        counter += 1
        if counter == n:
            pass
        else:
            result += x

    return result



if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert fun('not,poor,is,he,poor', 4) == "notpoor,is,he,poor"
    assert fun('not,poor1,poor2,poor3', 15) == "not,poor1,poor,poor3"
    assert fun('kuca,mama,auto,mazda3', 1) == "uca,mama,auto,mazda3"


    print('Testing completed!')