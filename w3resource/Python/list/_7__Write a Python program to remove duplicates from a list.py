# 7. Write a Python program to remove duplicates from a list.

def fun(text):
    result = []
    for x in text:
        if x in result:
            pass
        else:
            result.append(x)

    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun(["a", "b", "a", "c", "a", "b"]) == ["a", "b", "c"]
    assert fun(["a", "b", "a", "c", "a", "b", "a", "1", "bb"]) == ["a", "b", "c", "1", "bb"]
    assert fun(["a", "b", "a", "c", "a", "b", "a", "1", "bb", 1, 2, 1]) == ["a", "b", "c", "1", "bb", 1, 2]

    print('Testing completed!')