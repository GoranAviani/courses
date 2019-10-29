#10. Write a Python program to print the even numbers from a given list.


def fun(numbers):
    result = []
    for x in numbers:
        if x % 2 == 0:
            result.append(x)

    return result

if __name__ == "__main__":
    assert fun([1,2,3,4,4,4,5,6,7]) == [2,4,4,4,6]
    assert fun([1, 3, 7]) == []


    print("Testing completed!")