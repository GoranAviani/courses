def fun(name, age, address):
    result = name + "\n" + age + "\n" + address
    return result


if __name__ == '__main__':

    # These "asserts" are used for self-checking and not for testing
    assert fun('Goran', '32', 'Stockholm') == 'Goran\n32\nStockholm'
    print('Testing completed!')