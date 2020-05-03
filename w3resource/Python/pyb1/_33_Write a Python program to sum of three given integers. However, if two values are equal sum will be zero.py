#_33_Write a Python program to sum of three given integers.
# However, if two values are equal sum will be zero
def summa(x, y, z):
    allNums = [x, y, z]
    for n in allNums:
        #count() is an inbuilt function in
        # Python that returns count of how many times a
        # given object occurs in list
        if allNums.count(n) > 1:
            return 0
    return x + y + z

def check_for_duplicates(numbers):
    return True if len(numbers) != len(set(numbers)) else False

def summa_two(numbers):
    summ = 0
    are_duplicates = check_for_duplicates(numbers)
    if are_duplicates == True:
        return 0

    for number in numbers:
        summ += number
    return summ

def main():
    assert summa(3, 2, 1) == 6
    assert summa(2, 2, 2) == 0
    assert summa(2, 2, 1) == 0
    assert summa(2, 5, -1) == 6
    print("Coding complete!")
    result = summa_two([3, 2, 1])
    print(result)


if __name__ == '__main__':
    main()
