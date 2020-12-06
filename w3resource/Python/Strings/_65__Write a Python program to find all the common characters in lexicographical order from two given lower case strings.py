# 65. Write a Python program to find all the common characters in lexicographical order from two given lower case strings.

def fun(text1, text2):
    result = []
    for x in text1:
        if x in text2 and x not in result:
            result.append(x)
    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("kuca", "kuca") == ["k", "u", "c", "a"]
    assert fun("product information is", "description") == ['p', 'r', 'o', 'd', 'c', 't', 'i', 'n', 's']

    print('Testing completed!')