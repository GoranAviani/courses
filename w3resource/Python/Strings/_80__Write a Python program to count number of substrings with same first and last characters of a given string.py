#80. Write a Python program to count number of substrings with
# same first and last characters of a given string.


def fun(text1, text2):
    text1 = text1.split(" ")
    fistLetter = text2[:1]
    lastLetter = text2[len(text2)-1: len(text2)]
    counter = 0
    for x in text1:
        if x[:1] == fistLetter and x[len(x)-1:len(x)] == lastLetter:
            counter += 1


    return counter



if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("abc abc ccc aaa abb", "abc") == 2
    assert fun("a123b1 a123 ccc aaa abb", "abc") == 0
    assert fun("there is a star on the skyr and that star is shiningr bright", "star") == 4


    print('Testing completed!')