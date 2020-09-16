def divide_by_zero(func):
    def check_if_zero(x, y):
        if y == 0:
            return None
        else:
            return func(x, y)
    return check_if_zero

@divide_by_zero
def divide(x, y):
    return x / y


def main():
    result = divide(6, 3)
    print(result)
    result = divide(6, 0)
    print(result)
if __name__ == '__main__':
    main()