# 10. Write a Python program to find the list of words that are longer than n from a given list of words.

def fun(text, length):
    result = []
    for x in text:
        if len(x) > length:
            result.append(x)

    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun(["a", "bvv", "aaaa", "cqeqwe", "qeqw", "b"], 3) == ["aaaa", "cqeqwe", "qeqw"]
    assert fun(["a", "bvv", "aaaa", "cqeqwe", "qeqw", "b"], 2) == ["bvv", "aaaa", "cqeqwe", "qeqw"]

    print('Testing completed!')