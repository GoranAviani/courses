#5. Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each

def fun(first, second):


    secondbckp = second
    firstbckp = first
    second = first[:1] + secondbckp[1:]
    first = secondbckp[:1] + firstbckp[1:]

    return first + " " + second



if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert fun('aaa', 'bbb') == "baa abb"
    assert fun('rnk', 'split') == "snk rplit"

    print('Testing completed!')