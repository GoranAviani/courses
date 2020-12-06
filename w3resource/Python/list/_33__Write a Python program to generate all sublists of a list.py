# 33. Write a Python program to generate all sublists of a list

def fun(item1):
    result = []

    # first loop
    for x in range(len(item1) + 1):

        # second loop
        for y in range(x + 1, len(item1) + 1):
            # slice the subarray
            sublist = item1[x:y]
            result.append(sublist)

    print(result)
    return result


if __name__ == "__main__":
    #  These "asserts" are used for self-checking and not for testing
    assert fun([1, 2, 3]) == [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]

    print('Testing completed!')