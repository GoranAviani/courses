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

    print('Testing completed!')