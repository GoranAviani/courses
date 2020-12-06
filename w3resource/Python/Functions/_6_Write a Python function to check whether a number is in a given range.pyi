
def fun(n , x , y):
    if ((n >= x ) and ( n <= y)):
        return True
    else:
        return False


if __name__ == '__main__':
    #print('Example:')
    #print(checkio("Hello World hello"))

    assert fun(4,1, 5) == True
    assert fun(10, 15, 20) == False
    assert fun(-10, 15, 20) == False


    print("Coding complete!")