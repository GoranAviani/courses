#14. Write a Python program that accepts a comma
# separated sequence of words as input and prints the unique words in sorted form (alphanumerically).


def fun(words):
    words = words.split(",")
    unique = []
    for x in words:
       if x not in unique and x.isalpha():
          unique.append(x)
    result = sorted(unique)
    return result


if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert fun("Po,sumama,i,gorama,gorama,i,gorama") == ["Po","gorama","i","sumama"]

    print('Testing completed!')