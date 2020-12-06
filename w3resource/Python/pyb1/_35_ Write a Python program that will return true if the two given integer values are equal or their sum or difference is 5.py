# _35_ Write a Python program that will return true
# if the two given integer values are equal or their sum or difference is 5

def calculation(sign, x, y):
    if sign == "equal":
        return x == y
    elif sign == "minus":
        return (x - y) == 5
    elif sign == "plus":
        return (x + y) == 5


def check_numbers(x, y):
    all_checks = {1: "equal", 2: "minus", 3: "plus"}
    for check in range(1, len(all_checks)+1):
        result = calculation(all_checks[check], x, y)
        if result == True:
            return result
    return False
def main():
    assert check_numbers(2, 2) == True
    assert check_numbers(2, 3) == True
    assert check_numbers(6, 3) == False
    assert check_numbers(8, 3) == True
    assert check_numbers(-1, 6) == True
    print("Coding complete!")


if __name__ == '__main__':
    main()
