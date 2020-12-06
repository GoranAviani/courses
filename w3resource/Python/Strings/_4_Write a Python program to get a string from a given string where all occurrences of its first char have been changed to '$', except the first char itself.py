#4. Write a Python program to get a string from a given string where
# all occurrences of its first char have been changed to '$', except the first char itself.


def fun(word):
    firstLetter = word[:1]
    rest = word[1:]
    result = ""

    for x in rest:
        if x == firstLetter:
            result += "$"
        else:
            result += x


    result = firstLetter + result
    return result



if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert fun('aaa') == "a$$"
    assert fun('mama') == "ma$a"
    assert fun('sweden is the sup') == "sweden i$ the $up"
    print('Testing completed!')