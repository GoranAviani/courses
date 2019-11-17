#50. Write a Python program to split a string on the last occurrence of the delimiter.

def fun(text, delimeter):
    split1 = ""
    split2 = ""
    splited = False
    result = []
    for x in range(len(text)-1, -1, -1):

        if splited == True:
            split2 += text[x]

        if splited == False:
            split1 += text[x]
            if text[x] == delimeter:
                splited = True


    result.append(split2[::-1])
    result.append(split1[::-1])
    return result
if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("aebcedei", "e") == ['aebced', 'ei']

    print('Testing completed!')