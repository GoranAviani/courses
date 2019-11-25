# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

def fun(text):
    result = []
    for x in text:
        if x[:1] == x[len(x) - 1:len(x)]:
            result.append(x)
    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun(["abba", "121", "cars"]) == ["abba", "121"]
    assert fun(["abba", "121", "test text", "noot good"]) == ["abba", "121", "test text"]

    print('Testing completed!')