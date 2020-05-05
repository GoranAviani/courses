# _35_ Write a Python program that will return true
# if the two given integer values are equal or their sum or difference is 5

def fun(sign, x, y):
    if sign == "equal":
        return x == y
    elif sign == "min":
        return (x - y) == 5
    elif sign == "plus":
        return (x + y) == 5


def test(x, y):
    try:
        areSame = fun("equal", x, y)
        if areSame == False:
            raise ValueError("not ok")
        return True
    except (ValueError, IndexError):
        try:
            areSum1 = fun("plus", x, y)
            if areSum1 == False:
                raise ValueError("not ok")
            return True
        except (ValueError, IndexError):
            try:
                areSum1 = fun("min", x, y)
                if areSum1 == False:
                    raise ValueError("not ok")
                return True
            except (ValueError, IndexError):
                return False

def main():
    assert test(2, 2) == True
    assert test(2, 3) == True
    assert test(6, 3) == False
    assert test(8, 3) == True
    assert test(-1, 6) == True
    print("Coding complete!")


if __name__ == '__main__':
    main()
