import time

def sleep(func):
    """
    Hardcoded sleep value and passin paramethers along the way, piggibacking them
    :param func:
    :return:
    """
    def sleep_now(x, y):
        time.sleep(3)
        return func(x, y)

    return sleep_now

@sleep
def calculate(x, y):
    return 5

if __name__ == '__main__':
    result = calculate(1, 99999999)
    print(result)