

def summa(x,y):
    if (((x+y)>14) and ((x+y) < 21)):
        return 20
    else:
        return (x+ y)


if __name__ == '__main__':
    #print('Example:')
    #print(checkio("Hello World hello"))

    assert summa(11, 6) == 20
    assert summa(3, 2) == 5
    assert summa(10, 5) == 20
    assert summa(6, 5) == 11
    print("Coding complete!")