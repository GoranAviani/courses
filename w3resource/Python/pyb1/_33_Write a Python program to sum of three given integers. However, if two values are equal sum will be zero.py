
def summa(x, y, z):

    allNums = [x, y, z]

    for n in allNums:
        if allNums.count(n)> 1:
            return 0
    return x + y + z


if __name__ == '__main__':
    #print('Example:')
    #print(checkio("Hello World hello"))

    assert summa(3, 2, 1) == 6
    assert summa(2, 2, 2) == 0
    assert summa(2, 2, 1) == 0
    assert summa(2, 5, -1) == 6
    print("Coding complete!")
