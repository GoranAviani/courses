#38. Write a Python program to count occurrences of a substring in a string.


def fun(text, substring):
    substringLength = len(substring)
    counter = 0
    for x in range(0, len(text)):
        if text[x: x+substringLength] == substring:
            counter += 1
    return counter

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("kuca mama pas auto", "ma") == 2
    assert fun("kuca mama pas auto", "mam") == 1
    assert fun("draft messages, list you aaa messages", "a") == 6

    print('Testing completed!')