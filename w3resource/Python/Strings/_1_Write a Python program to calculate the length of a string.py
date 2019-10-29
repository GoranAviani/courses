#1. Write a Python program to calculate the length of a string.



def fun(words):
    count = 0
    for x in range (1,len(words)+1):
        count += 1

    count1 = 0
    words1 = list(words)
    for x in words1:
        count1 += 1


    return [len(words), count, count1]

if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert fun('goran') == [5, 5, 5]
    assert fun('stockholm') == [9, 9, 9]
    assert fun('anja') == [4, 4, 4]
    assert fun('ovo je sparta') == [13, 13, 13]

    print('Testing completed!')