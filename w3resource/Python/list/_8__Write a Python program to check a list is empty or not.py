# 8. Write a Python program to check a list is empty or not

def fun(text):
    if len(text) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun(["a", "b", "a", "c", "a", "b"]) == False
    assert fun([]) == True

    print('Testing completed!')