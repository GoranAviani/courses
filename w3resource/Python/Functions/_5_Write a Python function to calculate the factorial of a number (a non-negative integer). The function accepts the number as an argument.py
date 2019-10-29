def fun(x):
    result = 1
    y = x
    for x in range(0,x):
        result *= y
        y -= 1

    return result

if __name__ == '__main__':
    #print('Example:')
    #print(checkio("Hello World hello"))

    assert fun(4) == 24
    assert fun(3) == 6

    print("Coding complete!")