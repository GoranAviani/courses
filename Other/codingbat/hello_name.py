"""
Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

hello_name('Bob') → 'Hello Bob!'
hello_name('Alice') → 'Hello Alice!'
hello_name('X') → 'Hello X!'
"""
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
    result = hello_name("Goran")
    print(result)