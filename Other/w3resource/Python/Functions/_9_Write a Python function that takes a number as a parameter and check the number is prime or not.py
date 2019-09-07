def fun (num):
    if num == 1:
        return True
    elif num % 2 == 0:
        return False
    else:
        for x in range(2, num):
            if num % x == 0:
                return False
        return True