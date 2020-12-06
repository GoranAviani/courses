def check_string(func):
    def check(x):
        if type(x) is str:
            return func(x)
        else:
            return None

    return check

@check_string
def hello_name(name):
    return name


if __name__ == '__main__':
    result = hello_name(1)
    print(result)