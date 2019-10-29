def fun(num):
    if num == 1:
        return True
    elif num % 2 == 0:
        return False
    else:
        for x in range(2, num):
            if num % x == 0:
                return False
        return True


if __name__ == '__main__':

    assert fun(2) == False
    assert fun(7) == True
    assert fun(6) == False


    print("Coding complete!")