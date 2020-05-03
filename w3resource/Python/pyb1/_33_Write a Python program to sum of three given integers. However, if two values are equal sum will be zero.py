#_33_Write a Python program to sum of three given integers.
# However, if two values are equal sum will be zero
def summa(x, y, z):
    allNums = [x, y, z]
    for n in allNums:
        if allNums.count(n) > 1:
            return 0
    return x + y + z

def main():
    assert summa(3, 2, 1) == 6
    assert summa(2, 2, 2) == 0
    assert summa(2, 2, 1) == 0
    assert summa(2, 5, -1) == 6
    print("Coding complete!")


if __name__ == '__main__':
    main()
