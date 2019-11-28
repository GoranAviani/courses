# 19. Write a Python program to get the difference between the two lists

def fun(numbers1, numbers2):
    result = []
    if len(numbers1) == len(numbers2):
        for x in range(0, len(numbers1)):
            if numbers1[x] not in numbers2:
                result.append(numbers1[x])
            if numbers2[x] not in numbers1:
                result.append(numbers2[x])

    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun([1, 2, 3], [3, 4, 5]) == [1, 2, 4, 5]

    print('Testing completed!')