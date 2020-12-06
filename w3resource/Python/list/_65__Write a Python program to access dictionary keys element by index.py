# 65. Write a Python program to access dictionary keys element by index


def fun(item1, item2):
    result = list(item1)
    return result[item2]


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun({'physics': 80, 'math': 90, 'chemistry': 86}, 0) == "physics"

    print('Testing completed!')