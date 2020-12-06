"""
Exercise 1.21: Membership tests
"""


def main():
    symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,CAT,GOOG'
    symlist = symbols.split(',')

    var1 = 'AIG' in symlist
    print(var1)
    var1 = 'AA' in symlist
    print(var1)
    var1 = 'CAT' in symlist
    print(var1)


if __name__ == '__main__':
    main()