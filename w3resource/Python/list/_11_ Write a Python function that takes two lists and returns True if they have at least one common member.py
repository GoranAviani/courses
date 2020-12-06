# 11. Write a Python function that takes two lists and returns True if they have at least one common member.

def fun(text1, text2):
    for x in text1:
        if x in text2:
            return True

    return False


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun(["a", "bvv", "aaaa", "cqeqwe", "qeqw", "b"], ["3"]) == False
    assert fun(["a", "bvv", "aaaa"], ["2", "a"]) == True

    print('Testing completed!')