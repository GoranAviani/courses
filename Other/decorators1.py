def check_if_none(func):
    def internal(x, y):
        if not x or not y:
            return None
        else:
            return func(x, y)


    return internal

def main():
    res1 = sum_num(1, 2)
    print(res1)
    res1 = sum_num(1, None)
    print(res1)

@check_if_none
def sum_num(x, y):
    return x + y


if __name__ == '__main__':
    main()