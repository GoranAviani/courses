#40. Write a Python program to split a list based on first character of word.


def fun(item1):
    result = {}
    for x in item1:
        if x[:1] not in result:
            result[x[:1] ] = [x]
        else:
            result[x[:1]].append(x)


    return result


if __name__ == "__main__":
    #  These "asserts" are used for self-checking and not for testing
    assert fun(["hiiii", "aaa", "hello"]) == {'h': ['hiiii', 'hello'], 'a': ['aaa']}


    print('Testing completed!')